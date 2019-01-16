# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify


app = Flask(__name__)
app_host = '0.0.0.0'
app_port = 8086


@app.route('/notify_url', methods=['GET', 'POST'])
def notify_url(**kwargs):
    import json
    params = dict(
    )
    print json.dumps(params, ensure_ascii=False, indent=2)
    d = {'meta': {
        'success': True, 'status_code': 200,
        'message': "Requset Successes"
    }}
    return jsonify(d)


