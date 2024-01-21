# py-shortly: URL Shortener Service

This project is a URL shortener service implemented in Python utilizing FastAPI and SQLAlchemy. Specifically crafted for educational purposes and experimentation.

## Features

- **URL Shortening**: The service provides a way to shorten URLs. The `shorten` function takes a `UrlRequest` object (which contains the original URL and the user ID) and returns a shortened URL.

- **URL Retrieval**: The service also provides a way to retrieve the original URL from the shortened URL. The `get_long_url` function takes a shortened URL ID and returns the original URL.

## Usage

To use the URL shortener service, you need to call the `shorten` function with a `UrlRequest` object. The function will return a `Url` object with the shortened URL.

To retrieve the original URL, you need to call the `get_long_url` function with the ID of the shortened URL. The function will return the original URL.

## Dependencies

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- SQLAlchemy: The Python SQL Toolkit and Object-Relational Mapper that gives application developers the full power and flexibility of SQL.

## TO-DOS:
- Unit tests
- Authorization (roles)
- Caching
- Dockerize
