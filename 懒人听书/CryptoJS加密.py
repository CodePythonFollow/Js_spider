import requests
import execjs

accountName = '1284954990@qq.com'
password = '123456'

# 获取token
def get_token():
	url = 'http://www.lrts.me/user/login_token.do'

	data = {
		'accountName': accountName
	}

	response = requests.post(url, data=data)
	token = response.json()['data']

	return token

# 获取加密的密码
def get_password():
	with open('懒人听书token和password.js', encoding='utf-8') as fi:
		js = fi.read()
		pd = execjs.compile(js).call('text', password, token)
	return pd

if __name__ == "__main__":
	token = get_token()
	pd = get_password()
	print(token)
	print(pd)