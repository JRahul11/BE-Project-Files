import requests
import bs4
import base64
import urllib.request

try:
	# Legit Webpage
	htmlPage1 = urllib.request.urlopen("https://www.flipkart.com/")
	binaryData1 = str(base64.b64encode(htmlPage1.read()))[2:-1]
	file1 = open('binaryData1.bin', 'w')
	file1.write(binaryData1)
	file1.close()

	# Phishing Webpage
	htmlPage2 = urllib.request.urlopen("https://www.flipkart.com/")
	binaryData2 = str(base64.b64encode(htmlPage2.read()))[2:-1]
	file2 = open('binaryData2.bin', 'w')
	file2.write(binaryData2)
	file2.close()
	
	

	
except Exception as e:
	print("Issue ",e)

# Visualize any file as PNG image
# created by Benjamin Flesch on 12 Jan 2021

import sys
import os
import hashlib
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

input_file = sys.argv[1]

# see https://gist.github.com/cbwar/d2dfbc19b140bd599daccbe0fe925597
def sizeof_fmt(num, suffix='b'):
    """Readable file size
    :param num: Bytes value
    :type num: int
    :param suffix: Unit suffix (optionnal) default = o
    :type suffix: str
    :rtype: str
    """
    for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
md5 = hashlib.md5()
sha1 = hashlib.sha1()
with open(input_file, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
md5 = md5.hexdigest()
sha1 = sha1.hexdigest()
print("file", input_file)
print("MD5: {0}".format(md5))
print("SHA1: {0}".format(sha1))
arr = np.fromfile(input_file, dtype=np.ubyte)
filesize = len(arr)
filesize_text = sizeof_fmt(filesize)
print("size:", filesize_text)
linelength = math.ceil(math.sqrt(len(arr)))
len_missing = (linelength**2 - len(arr))
arr_padded = np.pad(arr, (0, len_missing), mode="constant", constant_values=0)
del arr
matrix = arr_padded.reshape(linelength, linelength)
del arr_padded
input_filename = os.path.basename(input_file)
output_filename = input_filename + ".png"
fig, ax = plt.subplots()
ax.matshow(matrix)
del matrix
ax.set_xlabel("SHA1: " + sha1 + "\nMD5: " + md5)
plt.title(input_filename + " (" + sizeof_fmt(filesize) + ")", loc="left", fontweight="bold")
plt.savefig(output_filename)
