# Wiley TDM & CrossRef API scripts

This repository includes example python scripts for using the [Wiley TDM](https://onlinelibrary.wiley.com/library-info/resources/text-and-datamining) and [CrossRef APIs](https://github.com/CrossRef/rest-api-doc)

## Scripts

- `dois.py`: lists DOIs for articles in a journal using journal ISSN (uses CrossRef API)
- `download.py`: downloads PDF from Wiley TDM using article DOI

## Installation

The scripts require Python v3.x and [habanero](https://github.com/sckott/habanero) (for CrossRef support).

```sh
#clone this repository
git clone https://github.com/repub/Wiley-TDM-Examples.git
cd Wiley-TDM-Examples

# install habanero (if necessary)
pip3 install habanero

# enjoy!
./dois --help
./download.py --help
```