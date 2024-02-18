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
        self.session = session or AsyncClient(headers=self.headers, timeout=30)

    async def _request(
        self, method: str, endpoint: str, params: dict = None, data: dict = None
    ) -> dict:
        """
        Send a request to the Snusbase API.

        Args:
            method (str): The HTTP method for the request (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to access.
            params (dict, optional): Query parameters for the request.
            data (dict, optional): JSON data for the request payload.

        Returns:
            dict: The response data as a dictionary.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{self.base_url}{endpoint}"
        request = await self.session.request(method, url, params=params, json=data)
        return request.json()

    async def search(self, term: str, search_type: str) -> dict:
        """
        Search Snusbase for data related to a term.

        Args:
            term (str): The term to search for.
            search_type (str): The type of search to perform.

        Returns:
            dict: The response data containing the search results.
        """
        endpoint = "/data/search"
        data = {"terms": [term], "types": [search_type]}
        return await self._request("POST", endpoint, data=data)

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
        return await self._request("POST", endpoint, data=data)

    async def ip_lookup(self, ip: str) -> dict:
        """
        Search Snusbase for data related to an IP address.

        Args:
            ip (str): The IP address to lookup.

        Returns:
            dict: The response data containing the IP address lookup results.
        """
        endpoint = "/tools/ip-whois"
        data = {
            "terms": [ip],
        }
        return await self._request("POST", endpoint, data=data)

    async def search_by_username(self, username: str) -> dict:
        """
        Search Snusbase for data related to a username.

        Args:
            username (str): The username to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(username, "username")

    async def search_by_password(self, password: str) -> dict:
        """
        Search Snusbase for data related to a password.

        Args:
            password (str): The password to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(password, "password")

    async def search_by_email(self, email: str) -> dict:
        """
        Search Snusbase for data related to an email address.

        Args:
            email (str): The email address to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(email, "email")

    async def search_by_ip(self, ip: str) -> dict:
        """
        Search Snusbase for data related to an IP address.

        Args:
            ip (str): The IP address to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(ip, "lastip")

    async def search_by_name(self, name: str) -> dict:
        """
        Search Snusbase for data related to a name.

        Args:
            name (str): The name to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(name, "name")

    async def search_by_hash(self, _hash: str) -> dict:
        """
        Search Snusbase for data related to a hash.

        Args:
            hash (str): The hash to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(_hash, "hash")

    async def search_by_wildcard(self, wildcard: str) -> dict:
        """
        Search Snusbase for data related to a wildcard.

        Args:
            wildcard (str): The wildcard to search for.

        Returns:
            dict: The response data containing the search results.
        """
        return await self.search(wildcard, "wildcard")
