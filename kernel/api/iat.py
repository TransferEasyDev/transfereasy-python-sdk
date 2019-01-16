# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class IAT(object):
    def __init__(self):
        pass

    @transfereasy
    def create_iat(self, params):

        param_schema = Schema({
            'beneficiary_account_name': {'type': basestring, 'required': True},
            'beneficiary_account_no': {'type': basestring, 'required': True},
            'send_amount': {'type': numbers.Number, 'required': True},
            'send_currency': {'type': basestring, 'required': True},
            'purpose': {'type': basestring, 'required': True},
            'memo': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='iat',
            method='POST',
        )

    @transfereasy
    def get_iat(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='iat',
            method='GET',
        )

    @transfereasy
    def get_iats(self, params):

        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': False},
            'to_created_at': {'type': basestring, 'required': False},
            'send_currency': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='iats',
            method='GET',
        )

    @transfereasy
    def repetition_iat(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='iat/repetition',
            method='POST',
        )
