from pathlib import Path
from typing import Generator
from urllib.parse import ParseResult

from unfurl.provider import Provider


class FileProvider(Provider[None]):

    def context_for(self, parse_result: ParseResult) -> None:
        return None

    def extract(self, context: None, parse_result: ParseResult) -> Generator[Path, None, None]:
        yield Path(parse_result.path)

    def load(self, context: None, parse_result: ParseResult) -> Generator[Path, None, None]:
        yield Path(parse_result.path)
