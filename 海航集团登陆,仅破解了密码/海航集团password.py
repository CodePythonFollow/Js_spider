import requests
import execjs

# 获取中间参数
def get_key_iv():
	url = 'http://hr.hnagroup.com/User/Account/GetEncryptionKey'

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
	}

	response = requests.get(url, headers=headers)
	key = response.json()["ValidataCode"]
	iv = response.json()["IPAddess"]

	return key, iv


# 获取加密的密码
def get_pd(file, func, valiable):
	'''
	file: js文件名
	func: 需要用到的js函数
	valiable： 传入的参数
	return: pd加密的密码
	'''
	key = valiable[0]
	iv = valiable[1]
	password = valiable[2]
	with open(file, encoding='utf-8') as fi:
		js = fi.read()
	pd = execjs.compile(js).call(func, key, iv, password)

	return pd


if __name__ == '__main__':
	key, iv = get_key_iv()
	password = '123456'
	valiable = [key, iv, password]

	pd = get_pd('登陆-DES加密.js', 'text', valiable) 
	print(pd)


