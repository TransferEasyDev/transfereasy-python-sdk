# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Statement(object):
    def __init__(self):
        pass

    @transfereasy
    def download(self, params):

        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': True},
            'to_created_at': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='statement',
            method='GET',
        )
