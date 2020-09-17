import execjs
import requests

def get_password(file, func, var):
	'''
	file: js所在文件
	func: 所用到的js函数
	var: 传入的参数
	return： 加密的结果
	'''
	with open(file, encoding='utf-8') as fi:
		js = fi.read()
	pd = execjs.compile(js).call(func, var)

	return pd

if __name__ == '__main__':
	pd = '123456'
	password = get_password('一品威客-MD5.js', 'text', pd)
	print(password)