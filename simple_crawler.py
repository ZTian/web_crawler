import requests

def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status() # Throw exception when status is not 200
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "Error!"

if __name__ == "__main__":
	url = "www.baidu.com"
	print(getHTMLText(url))