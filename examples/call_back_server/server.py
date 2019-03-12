# -*- coding: utf-8 -*-
from examples.call_back_server import verify_signature
from flask import Flask, request, jsonify


app = Flask(__name__)
app_host = '0.0.0.0'
app_port = 8086

'''
验签方法：

1. 将收到的回调内容(request.body)按照参数名ASCII码从小到大排序（字典序）生成json字符串，得到query_string。
2. 将query_string以及header中的Signature值使用SHA-256验签。公钥请联系TransferEasy获取。
3. header中的Timestamp值为时间戳, 如有需要, 可以验证本次请求是否超时。
'''


@app.route('/notify_url', methods=['GET', 'POST'])
@verify_signature
def notify_url(**kwargs):
    try:
        return 'success'
    except Exception as e:
        raise e.message


if __name__ == '__main__':
    app.run(app_host, app_port)

