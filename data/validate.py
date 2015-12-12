from __future__ import print_function, division
import hashlib
import os
import yaml

hashList=[]
with open('checksums.txt', 'r') as f:
	for line in f:
		elements = line.rstrip().split()
		kossop = line.rstrip().split()
		hashList.append(dict(zip(kossop[1:],elements)))



o = hashList


o = hashList
def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def check_hashes(o):
	all_good = True
	with open('hash.txt', 'r') as f:
		for line in f:
			hashDict=line.rstrip()
			m = yaml.load(hashDict)
			for k, v in m.items():
				digest = generate_file_md5(k)
				if v == digest:
					print("The file {0} has the correct hash.".format(k))
				else:
					print("ERROR: The file {0} has the WRONG hash!".format(k))
					all_good = False
	if all_good == True:
		print("Everything is Fine")
	else:
		print("Failure: Check log")




if __name__ == "__main__":
    check_hashes(o)
