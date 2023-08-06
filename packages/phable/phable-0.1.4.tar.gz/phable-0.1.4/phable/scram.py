import hashlib
import hmac
import logging
import re
from base64 import urlsafe_b64decode, urlsafe_b64encode
from binascii import hexlify, unhexlify
from dataclasses import dataclass
from hashlib import pbkdf2_hmac
from random import getrandbits
from time import time_ns
from typing import Union

from proj_haystack.utils import request

from .utils import Response

logger = logging.getLogger(__name__)

gs2_header = "n,,"

# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------


def get_auth_token(host_url: str, username: str, password: str):

    sc = ScramClient(username, password)

    # send hello msg & set the response
    hello_resp = request(host_url, headers=sc.get_hello_req())
    sc.set_hello_resp(hello_resp)

    # send first msg & set the response
    first_resp = request(host_url, headers=sc.get_first_req())
    sc.set_first_resp(first_resp)

    # send last msg & set the response
    last_resp = request(host_url, headers=sc.get_last_req())
    sc.set_last_resp(last_resp)

    # return the auth token
    return sc.auth_token


# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------


class ScramException(Exception):
    def __init__(self, message: str, server_error: str = None):
        super().__init__(message)
        self.server_error = server_error

    def __str__(self):
        s_str = "" if self.server_error is None else f": {self.server_error}"
        return super().__str__() + s_str


# # -----------------------------------------------------------------------
# # Parsing support - general
# # -----------------------------------------------------------------------


@dataclass
class NotFoundError(Exception):
    help_msg: str


class ScramClient:
    def __init__(self, username: str, password: str, hash: str = "sha256"):
        if hash not in ["sha100?", "sha256"]:
            raise ScramException(
                "The 'hash' parameter must be a str equal to 'sha256' or 'sha100?'"
            )

        self.username = username
        self.password = password
        self.hash = hash  # does the server or the client determine the hash?

    def get_hello_req(self) -> dict[str, str]:
        """Return the HTTP headers required for the client's hello message.  Note:  There is no data required for the client's hello message."""
        headers = {"Authorization": f"HELLO username={to_base64(self.username)}"}
        return headers

    def set_hello_resp(self, resp: Response) -> None:
        """Save server's response data as class attributes to be able to get other request messages."""
        auth_msg = fetch_auth_msg(resp.headers.as_string())
        self.handshake_token = fetch_handshake_token(auth_msg)
        self.hash = fetch_hash(
            auth_msg
        )  # Should I raise an exception if these don't line up?

    def get_first_req(self) -> dict[str, str]:
        self.c_nonce: str = gen_nonce()
        self.c1_bare: str = f"n={self.username},r={self.c_nonce}"
        headers = {
            "Authorization": f"scram handshakeToken={self.handshake_token}, hash={self.hash}, data={to_base64(gs2_header+self.c1_bare)}"
        }
        return headers

    def set_first_resp(self, resp: Response) -> None:
        # can we go straight to _fetch_scram_data?
        auth_msg = fetch_auth_msg(resp.headers.as_string())
        scram_data = fetch_scram_data(auth_msg)
        r, s, i = split_scram_data(scram_data)
        self.s_nonce: str = r
        self.salt: str = s
        self.iter_count: int = i

    def get_last_req(self):
        # define the client final no proof
        #   note: We want to send the s_nonce
        client_final_no_proof = f"c={to_base64('n,,')},r={self.s_nonce}"
        logger.debug(f"client-final-no-proof:\n{client_final_no_proof}\n")

        # define the auth msg
        auth_msg = f"{self.c1_bare},r={self.s_nonce},s={self.salt},i={self.iter_count},{client_final_no_proof}"
        logger.debug(f"auth-msg:\n{auth_msg}\n")

        # define the client key
        client_key = hmac.new(
            unhexlify(
                salted_password(
                    self.salt,
                    self.iter_count,
                    self.hash,
                    self.password,
                )
            ),
            "Client Key".encode("UTF-8"),
            self.hash,
        ).hexdigest()
        logger.debug(f"client-key:\n{client_key}\n")

        # find the stored key
        hashFunc = hashlib.new(self.hash)
        hashFunc.update(unhexlify(client_key))
        stored_key = hashFunc.hexdigest()
        logger.debug(f"stored-key:\n{stored_key}\n")

        # find the client signature
        client_signature = hmac.new(
            unhexlify(stored_key), auth_msg.encode("utf-8"), self.hash
        ).hexdigest()
        logger.debug(f"client-signature:\n{client_signature}\n")

        # find the client proof
        client_proof = hex(int(client_key, 16) ^ int(client_signature, 16))[2:]
        logger.debug(f"Here is the length of the client proof: {len(client_proof)}")

        # may need to do some padding before converting the hex to its
        # binary representation
        while len(client_proof) < 64:
            client_proof = "0" + client_proof

        client_proof_encode = to_base64(unhexlify(client_proof))
        logger.debug(f"client-proof:\n{client_proof}\n")

        client_final = client_final_no_proof + ",p=" + client_proof_encode
        client_final_base64 = to_base64(client_final)

        final_msg = (
            f"scram handshaketoken={self.handshake_token},data={client_final_base64}"
        )
        logger.debug(f"Here is the final msg being sent: {final_msg}")

        headers = {"Authorization": final_msg}
        return headers

    def set_last_resp(self, resp: Response) -> None:
        self.auth_token = fetch_auth_token(resp.headers.as_string())


# -
# define helper funcs used in ScramClient
# -


def fetch_auth_msg(resp_msg: str) -> str:
    exclude_msg = "WWW-Authenticate: "
    s = re.search(f"({exclude_msg})[^\n]+", resp_msg)

    # TODO:  add some handling here
    return s.group(0)[len(exclude_msg) :]


def fetch_scram_data(auth_msg: str) -> str:
    exclude_msg = "scram data="
    s = re.search(f"({exclude_msg})[a-zA-Z0-9]+", auth_msg)  # TODO confirm this

    if s is None:
        raise NotFoundError(f"Acceptable handshake token not found:\n{auth_msg}")

    return from_base64(s.group(0)[len(exclude_msg) :])


def split_scram_data(scram_data: str) -> tuple[str, str, int]:

    # define s_nonce - ASCII characters excluding ','
    r = re.search("(r=)[^,]+", scram_data)

    # define salt - base 64 encoded str
    s = re.search("(s=)[a-zA-Z0-9+/=]+", scram_data)

    # define iteration count
    i = re.search("(i=)[0-9]+", scram_data)

    if r == None or s == None or i == None:
        raise NotFoundError(f"Invalid scram data:\n{scram_data}")

    s_nonce: str = r.group(0).replace("r=", "")
    salt: str = s.group(0).replace("s=", "")
    iteration_count: int = int(i.group(0).replace("i=", ""))

    return (s_nonce, salt, iteration_count)


# def _fetch_date_time(date_str: str) -> datetime:
#     format = "%a, %d %b %Y %H:%M:%S %Z"
#     return datetime.strptime(date_str, format)


def fetch_handshake_token(auth_msg: str) -> str:
    exclude_msg = "handshakeToken="
    s = re.search(f"({exclude_msg})[a-zA-Z0-9]+", auth_msg)

    if s is None:
        raise NotFoundError(f"Acceptable handshake token not found:\n{auth_msg}")

    return s.group(0)[len(exclude_msg) :]


def fetch_hash(auth_msg: str) -> str:
    exclude_msg = "hash="
    s = re.search(f"({exclude_msg})(SHA-256)", auth_msg)

    if s is None:
        raise NotFoundError(f"Acceptable hash method not found:\n{auth_msg}")

    s_new = s.group(0)[len(exclude_msg) :]

    if s_new == "SHA-256":
        s_new = "sha256"

    return s_new


def fetch_auth_token(headers: str) -> str:
    exclude_msg = "authToken="
    s = re.search(f"({exclude_msg})[^,]+", headers)

    if s is None:
        raise NotFoundError(f"Acceptable auth token not found:\n{headers}")

    return s.group(0)[len(exclude_msg) :]


# --------------------------------------------------------------------
# Nonce & related helper funcs
# --------------------------------------------------------------------


def to_custom_hex(x: int, length: int) -> str:
    """Convert an integer x to hexadecimal string representation without a prepended '0x' str.  Prepend leading zeros as needed to ensure the specified number of nibble characters."""

    # Convert x to a hexadecimal number
    x_hex = hex(x)

    # Remove prepended 0x used to describe hex numbers
    x_hex = x_hex.replace("0x", "")

    # Prepend 0s as needed
    if len(x_hex) < length:
        x_hex = "0" * (length - len(x_hex)) + x_hex

    return x_hex


# Define nonce random mask for this VM
nonce_mask: int = getrandbits(64)


def gen_nonce() -> str:
    """Generate a nonce."""
    # Notes:
    #   getrandbits() defines a random 64 bit integer
    #   time_ns() defines ticks since the Unix epoch (1 January 1970)
    rand = getrandbits(64)
    ticks = time_ns() ^ nonce_mask ^ rand
    return to_custom_hex(rand, 16) + to_custom_hex(ticks, 16)


# --------------------------------------------------------------------
# Misc
# --------------------------------------------------------------------


def salted_password(salt: str, iterations: int, hash_func: str, password: str) -> bytes:
    # Need hash_func to be a str here
    dk = pbkdf2_hmac(hash_func, password.encode(), urlsafe_b64decode(salt), iterations)
    encrypt_password = hexlify(dk)
    return encrypt_password


# --------------------------------------------------------------------
# Base64uri conversions & related helper funcs
# --------------------------------------------------------------------


def to_base64(msg: Union[str, bytes]) -> str:
    """Encode a str or byte in base64uri format as defined by RFC 4648."""

    # Convert str inputs to bytes
    if isinstance(msg, str):
        msg = msg.encode("utf-8")

    # Encode using URL and filesystem-safe alphabet.
    # This means + is encoded as -, and / is encoded as _.
    output = urlsafe_b64encode(msg)

    # Decode the output as a str
    output = output.decode("utf-8")

    # Remove padding
    output = output.replace("=", "")

    return output


def from_base64(msg: Union[str, bytes]) -> str:
    """Decode a base64uri encoded str or bytes defined by RFC 4648 into its binary contents. Decode a URI-safe RFC 4648 encoding."""

    # Convert str inputs to bytes
    if isinstance(msg, str):
        msg = to_padded_bytes(msg)

    # Decode base64uri
    msg = urlsafe_b64decode(msg)

    # Decode bytes obj as a str
    msg = msg.decode("utf-8")

    return msg


def to_padded_bytes(s: str) -> bytes:
    """If needed, apply padding to make var s a multiple of 4.  Then convert to bytes obj."""
    r = len(s) % 4
    if r != 0:
        s += "=" * (4 - r)

    return s.encode("utf-8")
