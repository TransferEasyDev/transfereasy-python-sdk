# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Exchange(object):
    def __init__(self):
        pass

    @transfereasy
    def enquiry(self, params):

        param_schema = Schema({
            'sell_amount': {'type': numbers.Number, 'required': True},
            'sell_currency': {'type': basestring, 'required': True},
            'buy_amount': {'type': numbers.Number, 'required': True},
            'buy_currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='exchange/enquiry',
            method='POST',
        )

    @transfereasy
    def create_exchange(self, params):

        param_schema = Schema({
            'sell_amount': {'type': numbers.Number, 'required': True},
            'sell_currency': {'type': basestring, 'required': True},
            'buy_amount': {'type': numbers.Number, 'required': True},
            'buy_currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='exchange',
            method='POST',
        )

    @transfereasy
    def get_exchange(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='exchange',
            method='GET',
        )

    @transfereasy
    def get_exchanges(self, params):

        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': False},
            'to_created_at': {'type': basestring, 'required': False},
            'send_currency': {'type': basestring, 'required': False},
            'receive_currency': {'type': basestring, 'required': False},
            'status': {'type': basestring, 'required': False, 'validates': one_of('PAYMENT', 'CONVERSION', 'REPAYMENT')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='exchanges',
            method='GET',
        )

    @transfereasy
    def payment(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='exchange/payment',
            method='POST',
        )
