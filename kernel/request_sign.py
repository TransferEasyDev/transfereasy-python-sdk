# -*- coding: utf-8 -*-
import json
import traceback
from functools import wraps

import requests
from config import ACCOUNT_NO, SECRET, TE_HOST


def te_request(params, url, files, request_type='GET'):
    print TE_HOST.format(url='oauth/token')
    auth_response = requests.post(
        TE_HOST.format(url='oauth/token'),
        data={'account_no': ACCOUNT_NO, 'secret': SECRET},
        verify=False
    )
    print auth_response.content
    token = json.loads(auth_response.content)['data']['token']
    if isinstance(params, dict):
        print 'param is not json'
        headers = {"Authorization": 'Bearer {0}'.format(token)}
    else:
        print 'param is json'
        headers = {"Authorization": 'Bearer {0}'.format(token), "Content-Type": 'application/json; charset=utf-8'}

    api_url = TE_HOST.format(url=url)
    print api_url

    if request_type == 'GET':
        r = requests.get(api_url, params=params, headers=headers, verify=False)
    elif request_type == 'POST':
        r = requests.post(api_url, data=params, headers=headers, files=files, verify=False)
    elif request_type == 'DELETE':
        import urllib
        r = requests.delete(api_url + '?' + urllib.urlencode(params), headers=headers, verify=False)
    elif request_type == 'PUT':
        r = requests.put(api_url, data=params, headers=headers, files=files, verify=False)
    else:
        raise Exception('暂不支持的方式')
    return r


def transfereasy(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        key_variables = f(*args, **kwargs)
        try:
            if key_variables.url == 'account' and key_variables.method == 'POST':
                response = requests.post(TE_HOST.format(url=key_variables.url), data=key_variables.params, verify=False)
            else:
                response = te_request(key_variables.params, key_variables.url, key_variables.files, key_variables.method)

            print response.content

            if key_variables.url == 'statement':
                result = response.content
                print response.content
                return result
            else:
                result = json.loads(response.content)
                if result.get('meta').get('status_code') == 200:
                    print json.dumps(result, ensure_ascii=False)
                    return result
                else:
                    print json.dumps(result, ensure_ascii=False)
                    raise Exception(result)
        except Exception as e:
            traceback.print_exc(limit=5)
            raise e

    return decorated_function
