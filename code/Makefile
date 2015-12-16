.PHONY: analysis eda all clean coverage test depends

analysis:
	cd utils && python Analysis.py

eda:
	cd utils && python eda.py

all:
	cd utils && python eda.py
	cd utils && python Analysis.py

depends:
	sudo pip install dipy
	sudo pip install pyyaml

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

test:
	nosetests utils

coverage:
	nosetests utils --with-coverage --cover-package=utils 
