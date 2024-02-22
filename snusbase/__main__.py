from httpx import AsyncClient


class SnusbaseClient:
    """A class for interacting with the Snusbase API."""

    def __init__(self, api_key: str, session: AsyncClient = None):
        """
        Initialize the SnusbaseClient instance.

        Args:
            api_key (str): The API key for authentication.
            session (AsyncClient, optional): An HTTP client session to use for requests.
        """
        self.api_key = api_key
        self.base_url = "https://api-experimental.snusbase.com"
        self.headers = {
            "Auth": self.api_key,
            "Content-Type": "application/json",
        }
        self.session = session or AsyncClient(headers=self.headers, timeout=15)

    async def request(
        self, method: str, endpoint: str, params: dict = None, data: dict = None
    ) -> dict:
        """
        Send a request to the Snusbase API.

        Args:
            method (str): The HTTP method to use for the request.
            endpoint (str): The endpoint to send the request to.
            params (dict, optional): The query parameters to include in the request.
            data (dict, optional): The JSON data to include in the request.

        Returns:
            dict: The response data from the request.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{self.base_url}{endpoint}"
        request = await self.session.request(method, url, params=params, json=data)
        return request.json()

    async def search(self, term: str, search_type: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to a term.

        Args:
            term (str): The term to search for.
            search_type (str): The type of data to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        endpoint = "/data/search"
        data = {"terms": [term], "types": [search_type], "wildcard": wildcard}
        return await self.request("POST", endpoint, data=data)

    async def hash_lookup(self, _hash: str) -> dict:
        """
        Search Snusbase for data related to a hash.

        Args:
            hash (str): The hash to lookup.

        Returns:
            dict: The response data containing the hash lookup results.
        """
        endpoint = "/tools/hash-lookup"
        data = {
            "terms": [_hash],
            "types": ["hash"],
        }
        return await self.request("POST", endpoint, data=data)

    async def ip_lookup(self, ip: str) -> dict:
        """
        Search Snusbase for data related to an IP address.

        Args:
            ip (str): The IP address to lookup.

        Returns:
            dict: The response data containing the IP lookup results.
        """
        endpoint = "/tools/ip-whois"
        data = {
            "terms": [ip],
        }
        return await self.request("POST", endpoint, data=data)

    async def search_by_username(self, username: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to a username.

        Args:
            username (str): The username to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(username, "username", wildcard)

    async def search_by_password(self, password: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to a password.

        Args:
            password (str): The password to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(password, "password", wildcard)

    async def search_by_email(self, email: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to an email address.

        Args:
            email (str): The email address to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(email, "email", wildcard)

    async def search_by_ip(self, ip: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to an IP address.

        Args:
            ip (str): The IP address to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(ip, "lastip", wildcard)

    async def search_by_name(self, name: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to a name.

        Args:
            name (str): The name to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(name, "name", wildcard)

    async def search_by_hash(self, _hash: str, wildcard: bool = False) -> dict:
        """
        Search Snusbase for data related to a hash.

        Args:
            hash (str): The hash to search for.
            wildcard (bool, optional): Whether to use a wildcard search.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(_hash, "hash", wildcard)
