.PHONY: analysis eda all clean coverage test depends

analysis:
	python Analysis.py

eda:
	python eda.py

all:
	python Analysis.py
	python eda.py

depends:
	sudo pip install dipy
	sudo pip install pyyaml

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

test:
	nosetests utils

coverage:
	nosetests utils --with-coverage --cover-package=utils 
