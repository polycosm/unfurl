"""
Interface for a file url provider.

"""
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Generic, TypeVar
from urllib.parse import ParseResult


Context = TypeVar("Context")


class Provider(Generic[Context]):

    @contextmanager
    def unfurl(self, parse_result: ParseResult) -> Generator[Path, None, None]:
        context = self.context_for(parse_result)
        yield from self.extract(context, parse_result)

    @contextmanager
    def furl(self, parse_result: ParseResult) -> Generator[Path, None, None]:
        context = self.context_for(parse_result)
        yield from self.load(context, parse_result)

    def context_for(self, parse_result: ParseResult) -> Context:
        raise NotImplementedError("Provider must implement `context_for`")

    def extract(self, context: Context, parse_result: ParseResult) -> Generator[Path, None, None]:
        raise NotImplementedError("Provider must implement `extract`")

    def load(self, context: Context, parse_result: ParseResult) -> Generator[Path, None, None]:
        raise NotImplementedError("Provider must implement `load`")
