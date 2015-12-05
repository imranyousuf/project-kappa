#!/bin/sh
wget http://openfmri.s3.amazonaws.com/tarballs/ds105_raw.tgz > ds105_raw.tgz && \
tar zxvf ds105_raw.tgz                           && \
rm ds105_raw.tgz