import requests
import bs4
import base64
import urllib.request

try:
	
	fp = urllib.request.urlopen("https://www.flipkart.com/")
	data = fp.read()

	# wa = "https://www.amazon.in/"
	# res = requests.get(wa)
	# print(res)

	# data = bs4.BeautifulSoup(res.text, "html.parser")
	# print(data)

	temp = base64.b64encode(data)
	temp = str(temp)[2:-1]
	# decoded = base64.decodebytes(temp)
	# # print(decoded)
	# print(len(decoded)*8)

	# temp = "".join(["{:08b}".format(x) for x in decoded])
	file1 = open('fk1.bin', 'w')
	file1.write(temp)
	file1.close()

	# print(decoded)

	
except Exception as e:
	print("Issue ",e)
