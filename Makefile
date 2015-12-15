.PHONY: all data validate eda analysis clean coverage test

all:
	cd data && make data
	cd data && make validate
	cd paper && make all

data:
	cd data && make data 

validate:
	cd data && make validate 

eda:
	cd code/utils && make eda

analysis:
	cd code/utils && make analysis

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests code/utils data --with-coverage --cover-package=data  --cover-package=utils

test:
	nosetests data/tests

verbose:
	nosetests -v code/utils data
