#!/bin/sh
if [ -d ds105 ]; then
	echo "ds105 direcotry already exists, please remove the directory and run make again"
else
	wget http://openfmri.s3.amazonaws.com/tarballs/ds105_raw.tgz > ds105_raw.tgz && \
	tar zxvf ds105_raw.tgz                           && \
	rm ds105_raw.tgz
fi