#!/usr/bin/env python3
"""
Download PDF from Wiley TDM API

Required Arguments:
    key (string): Your Wiley TDM API Key
    doi (string): DOI of article to download
    
"""

__author__ = "Seth Erickson"
__version__ = "0.1.0"
__license__ = "MIT"


import requests
import argparse
import sys
from urllib.parse import quote_plus


def main(args):

    doi = args.doi
    key = args.key

    # Base URL of the Wiley API
    base_url = "https://api.wiley.com/onlinelibrary/tdm/v1/articles/"

    # Build request
    headers = {'Wiley-TDM-Client-Token': key}
    url = base_url + quote_plus(doi)

    # Make request
    r = requests.get(url, allow_redirects=True, headers=headers)

    # Parse response
    if r.status_code != 200:
        if r.status_code == 403:
            print("Download Failed (403): Unauthorized. Check that your API key is correct.", file=sys.stderr)
        elif r.status_code == 404:
            print("Download Failed (404): DOI not found.", file=sys.stderr)
        else:
            print("Download Failed (http status {0})".format(r.status_code), file=sys.stderr)
        return


    # name the pdf using DOI, replacing "/" with "_"
    filename = doi.replace("/","_") + ".pdf"
    print("downloaded", filename, file=sys.stderr)
    with open(filename, "wb") as fp:
        fp.write(r.content)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("doi", help="Article DOI")

    # # Optional argument flag which defaults to False
    parser.add_argument("-k", "--key", required=True, help="Wiley API Key")

    args = parser.parse_args()
    main(args)
