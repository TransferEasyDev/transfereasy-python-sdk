# -*- coding: utf-8 -*-
import json
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Deposit(object):
    def __init__(self):
        pass

    @transfereasy
    def create_deposit(self, params):
        param_schema = Schema({
            'payer_bank_acc_number': {'type': basestring, 'required': False},
            'payer_bank_acc_no': {'type': basestring, 'required': False},
            'escrow_bank_acc_number': {'type': basestring, 'required': False},
            'currency': {'type': basestring, 'required': True},
            'amount': {'type': basestring, 'required': True},
            'out_trade_id': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='deposit',
            method='POST',
        )

    @transfereasy
    def get_deposit(self, params):
        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='deposit',
            method='GET',
        )

    @transfereasy
    def cancel_deposit(self, params):
        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='deposit',
            method='DELETE',
        )

    @transfereasy
    def get_deposits(self, params):
        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': True},
            'to_created_at': {'type': basestring, 'required': True},
            'currency': {'type': basestring, 'required': True},
            'status': {'type': basestring, 'required': True, 'validates': one_of('CREDITED', 'PROCESSING', 'CANCELED')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='deposits',
            method='GET',
        )
