# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Transfer(object):
    def __init__(self):
        pass

    @transfereasy
    def enquiry(self, params):

        beneficiary_schema = Schema({
            'bank_account_number': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
            'currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema = Schema({
            'send_amount': {'type': numbers.Number, 'required': True},
            'send_currency': {'type': basestring, 'required': True},
            'beneficiaries': {'type': Array(beneficiary_schema), 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='transfer/enquiry',
            method='POST',
        )

    @transfereasy
    def create_transfer(self, params):

        beneficiary_schema = Schema({
            'bank_account_number': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
            'currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema = Schema({
            'send_amount': {'type': numbers.Number, 'required': True},
            'send_currency': {'type': basestring, 'required': True},
            'beneficiaries': {'type': Array(beneficiary_schema), 'required': True},
            'purpose': {'type': basestring, 'required': True},
            'memo': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='transfer',
            method='POST',
        )

    @transfereasy
    def get_transfer(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='transfer',
            method='GET',
        )

    @transfereasy
    def get_transfers(self, params):

        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': False},
            'to_created_at': {'type': basestring, 'required': False},
            'send_currency': {'type': basestring, 'required': False},
            'receive_currency': {'type': basestring, 'required': False},
            'status': {'type': basestring, 'required': False, 'validates': one_of('RISK', 'PAYMENT', 'CONVERSION', 'DELIVERY')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='transfers',
            method='GET',
        )

    @transfereasy
    def cancel_transfer(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='transfer',
            method='DELETE',
        )

    @transfereasy
    def repetition_transfer(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='transfer/repetition',
            method='POST',
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
            url='transfer/payment',
            method='POST',
        )
