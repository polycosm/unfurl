from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Generator, Tuple
from urllib.parse import ParseResult

from boto3 import Session

from unfurl.provider import Provider


def to_bucket_info(parse_result: ParseResult) -> Tuple[str, str]:
    return parse_result.netloc, parse_result.path.lstrip("/")


class S3Provider(Provider[Session]):

    def context_for(self, parse_result: ParseResult) -> Session:
        return Session()

    def extract(self, context: Session, parse_result: ParseResult) -> Generator[Path, None, None]:
        s3 = context.client("s3")
        bucket, key = to_bucket_info(parse_result)

        with NamedTemporaryFile() as tempfile:
            s3.download_fileobj(bucket, key, tempfile)
            tempfile.seek(0)
            yield Path(tempfile.name)

    def load(self, context: Session, parse_result: ParseResult) -> Generator[Path, None, None]:
        s3 = context.client("s3")
        bucket, key = to_bucket_info(parse_result)

        with NamedTemporaryFile() as tempfile:
            yield Path(tempfile.name)
            s3.upload_fileobj(bucket, key, tempfile)
