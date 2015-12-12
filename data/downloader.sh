#!/bin/sh
if [ -d ds105 ]; then
	echo "ds105 direcotry already exists, please remove the directory and run make again"
else
	wget https://www.ocf.berkeley.edu/~imran/ds105.zip && \
	unzip ds105.zip                          && \
	rm ds105.zip							   && \
	wget https://nipy.bic.berkeley.edu/rcsds/ds105_mnifunc.tar --no-check-certificate > temp.tar && \
	tar -xvf temp.tar && \
	rm temp.tar
fi