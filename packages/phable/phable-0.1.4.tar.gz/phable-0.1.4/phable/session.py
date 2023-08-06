from proj_haystack.scram import ScramClient
from proj_haystack.utils import request


class HaystackSession:
    """
    Models the network session to a Project Haystack compliant web
    server from a client's perspective.
    """

    def __init__(self, host_url: str, project: str, username: str, password: str):
        self.host_url = host_url
        self.project = project
        self.username = username
        self.password = password

        # create a scram object
        scram = ScramScheme(host_url, username, password)

        # try to get the auth token - TODO add a try/catch block here
        self.auth_token = scram.get_auth_token()

    def exec_query(self, query: str, format: str):
        """
        An acceptable format is "text/csv"
        """
        url = f"{self.host_url}/api/{self.project}/{query}"
        header = {
            "Authorization": f"BEARER authToken={self.auth_token}",
            "Accept": format,
        }
        response = requests.get(url, headers=header)

        return response.text
