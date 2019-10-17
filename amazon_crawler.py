import requests

def getHTMLText(url):
	try:
		kv = {'user-agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=kv)
		r.raise_for_status() # Throw exception when status is not 200
		r.encoding = r.apparent_encoding
		return r.text[1000:2000]
	except:
		return "Error!"

if __name__ == "__main__":
	url = "https://www.amazon.com/gp/product/0321751043/ref=ox_sc_saved_title_1?smid=ATVPDKIKX0DER&psc=1"
	print(getHTMLText(url))