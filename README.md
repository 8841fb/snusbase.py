# snusbase.py - Unofficial Asynchronous Snusbase API Wrapper

[![PyPI - Downloads](https://img.shields.io/pypi/dm/snusbase.py?style=flat-square&label=PyPI%20downloads)](https://pypi.python.org/pypi/snusbase.py)
[![PyPI - Python](https://img.shields.io/pypi/pyversions/snusbase.py?style=flat-square&label=Python%20version)](https://python.org)
[![PyPI - License](https://img.shields.io/pypi/l/snusbase.py?style=flat-square&label=License)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/snusbase.py?style=flat-square&label=PyPI%20package%20version)](https://semver.org)
[![PyPI - Status](https://img.shields.io/pypi/status/snusbase.py?style=flat-square&&label=PyPI%20Status)](https://pypi.python.org/pypi/snusbase.py)

> `snusbase.py` is an unofficial asynchronous Python wrapper for the [Snusbase](https://snusbase.com/) API.

## Features

-   **Fast and Efficient:** Utilizes asynchronous programming for optimized performance.
-   **Fully Asynchronous:** Leverages asyncio to support concurrent operations.
-   **Easy to Use:** Provides a clean and intuitive interface for Snusbase API operations.
-   **Type Hinted:** Comes with type hints for improved code readability and IDE support.

## Installation

You can easily install `snusbase.py` using pip:

```bash
pip install snusbase.py
```

## Usage

```py
import asyncio
from snusbase import SnusbaseClient

snusbase = SnusbaseClient("YOUR_API_KEY")

async def main():
    results = await snusbase.ip_lookup("1.1.1.1")
    print(results)

asyncio.run(main())
```

## TODO:

-   [ ] Make documentation.
-   [ ] Proper error handling.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Credits

-   [Snusbase](https://snusbase.com/) for their amazing service.
