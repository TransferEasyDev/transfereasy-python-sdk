# -*- coding: utf-8 -*-
import rsa
import json
import time
import base64
from functools import wraps
from flask import request
from config import PUBLIC_KEY


def json_verify(json_data, signature, timestamp, public_key):
    """
    :param json_data: 表单数据
    :param signature: 签名
    :param timestamp: 时间戳
    :param public_key: 公钥
    :return: 验签结果
    """
    signature_time = time.time() - float(timestamp)
    if signature_time > 100:
        raise Exception("请求已过时")

    # 用 utf-8 编码
    signature_str = json_data.encode("utf-8")
    # base64解码签名
    signature = base64.b64decode(signature)

    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
    try:
        return rsa.verify(signature_str, signature, pub_key)
    except:
        return False


def verify_signature(f):
    """ 验证签名 """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('Signature')
        timestamp = request.headers.get('Timestamp')

        print signature
        print timestamp

        try:
            payload = json.dumps(request.json, sort_keys=True)
            print signature
            print timestamp
            print payload

            if not json_verify(payload, signature, timestamp, PUBLIC_KEY):
                raise Exception("Signature Can't Verify")

            return f(*args, **kwargs)
        except:
            raise

    return decorated_function
