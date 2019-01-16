# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Others(object):
    def __init__(self):
        pass

    @transfereasy
    def escrow_accounts(self, params):

        param_schema = Schema({
            'currency': {'type': basestring, 'required': True},
            'country': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='escrow_accounts',
            method='GET',
        )

    @transfereasy
    def evidence(self, params):

        param_schema = Schema({
            'file_name': {'type': basestring, 'required': True},
            'memo': {'type': basestring, 'required': True},
            'transfer_no': {'type': basestring, 'required': False},
            'exchange_no': {'type': basestring, 'required': False},
            'deposit_no': {'type': basestring, 'required': False},
            'invoice_no': {'type': basestring, 'required': False},
            'iat_no': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='evidence',
            method='POST',
        )

