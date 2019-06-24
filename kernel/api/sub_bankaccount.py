# -*- coding: utf-8 -*-
import json
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class SubBankAccount(object):
    def __init__(self):
        pass


    @transfereasy
    def create_sub_bankaccount(self, params):

        return KeyVariables(
            params=json.dumps(params),
            url='account/sub_bank_account',
            method='POST',
        )

    @transfereasy
    def update_sub_bankaccount(self, params):

        return KeyVariables(
            params=json.dumps(params),
            url='account/sub_bank_account',
            method='PUT',
        )

    @transfereasy
    def get_progress(self, params):
        param_schema = Schema({
            'apply_no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='account/sub_bank_account/progress',
            method='GET',
        )

    @transfereasy
    def get_transactions(self, params):
        param_schema = Schema({
            'sub_bank_account_number': {'type': basestring, 'required': True},
            'from_created_at': {'type': basestring, 'required': False},
            'to_created_at': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='account/sub_bank_account/transactions',
            method='GET',
        )

