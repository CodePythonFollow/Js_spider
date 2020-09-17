import execjs


# 获取加密的password
def get_pd(file, func, variable):
	'''
	file: js文件名
	func： 调用的函数名
	return: pd得到加密后的密码
	'''
	with open(file, encoding='utf-8') as fi:
		js = fi.read()

	pd = execjs.compile(js).call(func, variable)
	return pd


if __name__ == '__main__':
	pd = get_pd('登陆——MD5.js', 'text', '123456')
	print(pd)