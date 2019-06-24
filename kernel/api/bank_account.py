# -*- coding: utf-8 -*-
import json
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class BankAccount(object):
    def __init__(self):
        pass

    @transfereasy
    def create_bacc(self, params):

        bank_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'branch': {'type': basestring, 'required': False},
            'swift_code': {'type': basestring, 'required': True},
            'routing_number': {'type': basestring, 'required': False},
            'bsb_code': {'type': basestring, 'required': False},
        }, strict=False)

        holder_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'doc_type': {'type': basestring, 'required': False, 'validates': one_of('ID', 'PASSPORT', 'DRIVER_LICENSE', 'CI', 'BR')},
            'doc_number': {'type': basestring, 'required': False},
            'contact': {'type': basestring, 'required': False},
            'type': {'type': basestring, 'required': True, 'validates': one_of('COMPANY', 'INDIVIDUAL')},
            'dob': {'type': basestring, 'required': False},
            'country': {'type': basestring, 'required': False},
            'address': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema = Schema({
            'bank': {'type': bank_schema, 'required': True},
            'country': {'type': basestring, 'required': True},
            'currency': {'type': basestring, 'required': True},
            'bank_account_number': {'type': basestring, 'required': True},
            'holder': {'type': holder_schema, 'required': True},
            'purpose': {'type': basestring, 'required': True, 'validates': one_of('PAYER', 'BENEFICIARY')},

            'iban': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='account/bank_account',
            method='POST',
        )

    @transfereasy
    def update_bacc(self, params):

        bank_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'branch': {'type': basestring, 'required': False},
            'swift_code': {'type': basestring, 'required': True},
            'routing_number': {'type': basestring, 'required': False},
            'bsb_code': {'type': basestring, 'required': False},
        }, strict=False)

        holder_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'doc_type': {'type': basestring, 'required': False, 'validates': one_of('ID', 'PASSPORT', 'DRIVER_LICENSE', 'CI', 'BR')},
            'doc_number': {'type': basestring, 'required': False},
            'contact': {'type': basestring, 'required': False},
            'type': {'type': basestring, 'required': True, 'validates': one_of('COMPANY', 'INDIVIDUAL')},
            'dob': {'type': basestring, 'required': False},
            'country': {'type': basestring, 'required': False},
            'address': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
            'bank': {'type': bank_schema, 'required': True},
            'country': {'type': basestring, 'required': True},
            'currency': {'type': basestring, 'required': True},
            'bank_account_number': {'type': basestring, 'required': True},
            'holder': {'type': holder_schema, 'required': True},
            'purpose': {'type': basestring, 'required': True, 'validates': one_of('PAYER', 'BENEFICIARY')},

            'iban': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='account/bank_account',
            method='PUT',
        )

    @transfereasy
    def delete_bacc(self, params):

        param_schema = Schema({
            'currency': {'type': basestring, 'required': True},
            'bank_account_number': {'type': basestring, 'required': True},
            'purpose': {'type': basestring, 'required': True, 'validates': one_of('PAYER', 'BENEFICIARY')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='account/bank_account',
            method='DELETE',
        )

    @transfereasy
    def create_baccs(self, params):
        bank_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'branch': {'type': basestring, 'required': False},
            'swift_code': {'type': basestring, 'required': True},
            'routing_number': {'type': basestring, 'required': False},
            'bsb_code': {'type': basestring, 'required': False},
        }, strict=False)

        holder_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'doc_type': {'type': basestring, 'required': False,
                         'validates': one_of('ID', 'PASSPORT', 'DRIVER_LICENSE', 'CI', 'BR')},
            'doc_number': {'type': basestring, 'required': False},
            'contact': {'type': basestring, 'required': False},
            'type': {'type': basestring, 'required': True, 'validates': one_of('COMPANY', 'INDIVIDUAL')},
            'dob': {'type': basestring, 'required': False},
            'country': {'type': basestring, 'required': False},
            'address': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema = Schema({
            'bank': {'type': bank_schema, 'required': True},
            'country': {'type': basestring, 'required': True},
            'currency': {'type': basestring, 'required': True},
            'bank_account_number': {'type': basestring, 'required': True},
            'holder': {'type': holder_schema, 'required': True},
            'purpose': {'type': basestring, 'required': True, 'validates': one_of('PAYER', 'BENEFICIARY')},

            'iban': {'type': basestring, 'required': False},
        }, strict=False)

        for bacc in params:
            param_schema.validate(bacc)  # 检测不通过直接抛异常
            param_schema.apply_defaults(bacc)  # attach 默认值

        return KeyVariables(
            params=json.dumps(params),
            url='account/bank_accounts',
            method='POST',
        )

    @transfereasy
    def get_bacc(self, params):
        param_schema = Schema({
            'bank_account_number': {'type': basestring, 'required': True},
            'purpose': {'type': basestring, 'required': True, 'validates': one_of('PAYER', 'BENEFICIARY')},
            'currency': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='account/bank_account',
            method='GET',
        )

    @transfereasy
    def get_baccs(self, params):
        param_schema = Schema({
            'purpose': {'type': basestring, 'required': False, 'validates': one_of('PAYER', 'BENEFICIARY')},
            'status': {'type': basestring, 'required': False, 'validates': one_of('NEW', 'APPROVED', 'PENDING', 'DENIED')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        return KeyVariables(
            params=params,
            url='account/bank_accounts',
            method='GET',
        )
