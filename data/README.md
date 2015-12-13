# Build Status
[![Build Status](https://travis-ci.org/berkeley-stat159/project-kappa.svg?branch=master)](https://travis-ci.org/berkeley-stat159/project-kappa)

# Code Coverage
[![Coverage Status](https://coveralls.io/repos/berkeley-stat159/project-kappa/badge.svg?branch=master&service=github)](https://coveralls.io/github/berkeley-stat159/project-kappa?branch=master)

# project-template
Fall 2015 group project


Thanks to Jarrod Millman, Matthew Brett, J-B Poline, and Ross Barnowski it would not have been possible without you guys.

Special Thanks to Matthew Brett(https://github.com/matthew-brett) for meeting us pretty much everday during finals week.

## Steps to be followed

### Downloading Data

Change Directory to the data directory `cd data`

`Please make sure that you have atleast 13GB of disk space before running make data, please make sure you have uninterrupted internet to download the 12GB of data`

The Makefile supports four commands: `data`,`clean`,`test`,`validate` .
- `make data`: calls downloader.sh which downloads who compressed folder and uncompressing it, that is all the data we need
- `make test`: Tests the functions located in the `data` 
 




## Navigating the Repository 

The Makefile contains four commands: `clean`, `test`, `verbose`, and `coverage`. 
- `make clean`: Remove all extra files generated when compiling code. Does this recursively for all subdirectories. 
- `make test`: Tests the functions located in the `data` and `code` directories, to be used to validate and analyze the data, respectively. 
- `make verbose`: Performs the same actions as `make test`, but uses the verbose nosetests option. 

## Contributors 

- Imran Yousuf ([`imranyousuf`](https://github.com/imranyousuf))
- Zheng Chang ([`changzheng1993`](https://github.com/changzheng1993))
- Noel Pimentel ([`noelpimentel`](https://github.com/noelpimentel))
- Giancarlo Escobar ([`giancarloescobar`](https://github.com/giancarloescobar))