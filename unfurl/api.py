"""
File URL API

"""
from contextlib import contextmanager
from pathlib import Path
from pkg_resources import iter_entry_points
from typing import Dict, Generator, Type
from urllib.parse import ParseResult, urlparse

from unfurl.provider import Provider


def load_providers() -> Dict[str, Type[Provider]]:
    return {
        entry_point.name: entry_point.load()
        for entry_point in iter_entry_points("unfurl.providers")
    }


def provider_for(parse_result: ParseResult) -> Provider:
    providers = load_providers()
    provider_class = providers.get(parse_result.scheme)
    if not provider_class:
        raise Exception(f"No unfurl provider found for scheme: {parse_result.scheme}")
    return provider_class()


@contextmanager
def unfurl(url: str) -> Generator[Path, None, None]:
    """
    """
    parse_result = urlparse(url)
    provider = provider_for(parse_result)
    with provider.unfurl(parse_result=parse_result) as path:
        yield path


@contextmanager
def furl(url: str) -> Generator[Path, None, None]:
    """
    """
    parse_result = urlparse(url)
    provider = provider_for(parse_result)
    with provider.furl(parse_result=parse_result) as path:
        yield path
