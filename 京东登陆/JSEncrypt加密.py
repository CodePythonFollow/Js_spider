import execjs

def get_text(fill_name, def_name, var):
    with open(fill_name, encoding='utf-8') as fi:
        js = fi.read()
        data = execjs.compile(js)
    return data.call(def_name, var)

if __name__ == "__main__":
    passwd = get_text('password.js', 'getEntryptPwd', '666666')
    print(passwd)