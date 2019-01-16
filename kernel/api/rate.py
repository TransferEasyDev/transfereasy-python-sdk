# -*- coding: utf-8 -*-
import json
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Rate(object):
    def __init__(self):
        pass

    @transfereasy
    def get_rate(self, params):

        param_schema = Schema({
            'sell_currency': {'type': basestring, 'required': True},
            'buy_currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='rate',
            method='GET',
        )
