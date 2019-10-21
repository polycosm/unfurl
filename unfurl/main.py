"""
Example usage that copies data from one location to another.

"""
from click import argument, command, echo

from unfurl.api import furl, unfurl


@command()
@argument("from_url")
@argument("to_url")
def main(from_url, to_url):
    echo(f"Copying file from {from_url} to {to_url}...")
    with unfurl(from_url) as from_path:
        with furl(to_url) as to_path:
            with from_path.open('rb') as infile:
                with to_path.open('wb') as outfile:
                    outfile.write(infile.read())
