.PHONY: data testing_data validate testing_validate test coverage
data:
	sh downloader.sh

testing_data:


validate:
	wget https://www.ocf.berkeley.edu/~imran/checksums.txt
	python validate.py
	

testing_validate: 
	

test:
	nosetests tests -w ..

coverage:
	nosetests tests -w .. 

clean:
	find . -name "*.tar" -o -name "*.zip" -o -name "*.pyx.md5" -o -name "*.pyc"| xargs rm -f
	rm -rf __MACOSX
	rm checksums.txt
	echo "to remove ds105, please do rm -rf ds105, it will remove 12GB"