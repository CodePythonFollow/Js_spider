import hashlib
import time
import random
import requests
import tkinter as tk

# 返回表单加密数据 
def get_d():
    # 接收输入框的输入
    e = t1.get(0.0, 'end')

    # 制造表单所需数据
    navigator_appVersion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    r = int(time.time() * 1000)
    ts = str(r)
    bv = hashlib.md5(navigator_appVersion.encode(encoding='utf-8')).hexdigest()
    salt = str(r * 10 + random.randint(0, 9))
    sign = hashlib.md5(f"fanyideskweb{e}{salt}n%A-rKaT5fb[Gy?;N5@Tj".encode(encoding='utf-8')).hexdigest()
    return salt, sign, ts, bv


def get_data():
    salt, sign, ts, bv = get_d()
    # 接收输入框的输入
    e = t1.get(0.0, 'end')
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-785285661@10.168.8.61; JSESSIONID=aaaJimLXqG6AIhSo0MW8w; OUTFOX_SEARCH_USER_ID_NCOO=272794459.17733103; ___rl__test__cookies=1577068552212',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    response = requests.post(url, headers=headers, data=data)

    if response.json()['smartResult']['entries'][1]:
        text1 = ''
        for i in response.json()['translateResult'][0][0].values():
            text1 += i
        t1.delete(0.0, 'end')  # 因为这种框是滚动显示，所以先删除再插入
        t1.insert(0.0, text1 + '\n')

    if response.json()['translateResult'][0][0].values():
        text2 = response.json()['smartResult']['entries'][1]

        t1.insert(tk.INSERT, text2)

# 删除输入框
def delete_data():
    t1.delete(0.0, 'end')

if __name__ == '__main__':

    # 窗口化
    fan = tk.Tk()
    fan.title('翻译君')
    fan.geometry('750x620')
    t1 = tk.Text(fan, font=('微软雅黑', 10))
    t1.pack()
    b1 = tk.Button(fan, text='一键翻译', font=('微软雅黑', 12), fg='Purple', width=10, height=3, command=get_data)
    b1.pack()
    b2 = tk.Button(fan, text='一键清除', font=('微软雅黑', 12), fg='Purple', width=10, height=3, command=delete_data)
    b2.pack()

    fan.mainloop()

