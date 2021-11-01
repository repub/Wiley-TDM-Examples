#!/usr/bin/env python3
"""
Lists DOIs of articles in a journal.

Required Argument:
    ISSN of journal

Optional Arguments:
    from (yyyy-mm-dd): filter articles published after date
    to (yyyy-mm-dd): filter articles published before date
    
"""

__author__ = "Seth Erickson"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import sys
from habanero import Crossref
from requests.exceptions import HTTPError

def main(args):
    cr = Crossref()
    filter = {
            'type': 'journal-article'#
    }

    max = 100000

    if args.frm != None:
        filter['from-print-pub-date'] = args.frm

    if args.to != None:
        filter['to-print-pub-date'] = args.to

    try:
        res = cr.journals(
            ids= args.issn,
            works = True,
            limit = 1000,
            filter = filter,
            select = "DOI",
            cursor="*",
            cursor_max=max,
            progress_bar = args.progress
        )
    except HTTPError as err:
        print(err)
        return
         
    items = [ z['message']['items'] for z in res ]
    items = [ item for sublist in items for item in sublist ]
    for d in items:
        print(d['DOI'])

    if len(items) == max:
        print("Warning: DOI limit reached. Results may be incomplete.", file = sys.stderr )


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("issn", help="ISSN of journal")

    # # Optional argument flag which defaults to False
    parser.add_argument("-p", "--progress", action="store_true", default=False, help="show progress bar")

    # From parameter
    parser.add_argument("-f", "--from", action="store", dest="frm", default=None, help="from published date (yyyy-mm-dd)")
    parser.add_argument("-t", "--to", action="store", dest="to", default=None,  help="to published date (yyyy-mm-dd)")

    args = parser.parse_args()
    main(args)
