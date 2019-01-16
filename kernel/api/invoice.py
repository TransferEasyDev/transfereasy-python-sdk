# -*- coding: utf-8 -*-
import json
import numbers
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Invoice(object):
    def __init__(self):
        pass

    @transfereasy
    def create_invoice(self, params):
        address_schema = Schema({
            'line1': {'type': basestring, 'required': True},
            'city': {'type': basestring, 'required': False},
            'state': {'type': basestring, 'required': False},
            'postal_code': {'type': basestring, 'required': False},
            'country': {'type': basestring, 'required': False},
        })

        recipient_schema = Schema({
            'dob': {'type': basestring, 'required': True},
            'entity_type': {'type': basestring, 'required': True, 'validates': one_of('INDIVIDUAL', 'COMPANY')},
            'first_name': {'type': basestring, 'required': True},
            'last_name': {'type': basestring, 'required': True},
            'document_type': {'type': basestring, 'required': True},
            'document_number': {'type': basestring, 'required': True},
            'email': {'type': basestring, 'required': False},
            'mobile': {'type': basestring, 'required': False},
            'address': {'type': address_schema, 'required': False},
            'bank_account_number': {'type': basestring, 'required': False},
            'bank_name': {'type': basestring, 'required': False},
        }, strict=False)

        unit_price_schema = Schema({
            'currency': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
        })

        products_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'quantity': {'type': int, 'required': True},
            'unit_price': {'type': unit_price_schema, 'required': True}
        })

        param_schema = Schema({
            'recipient': {'type': recipient_schema, 'required': True},
            'products': {'type': Array(products_schema), 'required': True},
            'memo': {'type': basestring, 'required': False},
            'out_trade_id': {'type': basestring, 'required': False},
            'currency': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='invoice',
            method='POST',
        )

    @transfereasy
    def update_invoice(self, params):
        address_schema = Schema({
            'line1': {'type': basestring, 'required': True},
            'city': {'type': basestring, 'required': False},
            'state': {'type': basestring, 'required': False},
            'postal_code': {'type': basestring, 'required': False},
            'country': {'type': basestring, 'required': False},
        })

        recipient_schema = Schema({
            'dob': {'type': basestring, 'required': True},
            'entity_type': {'type': basestring, 'required': True, 'validates': one_of('INDIVIDUAL', 'COMPANY')},
            'first_name': {'type': basestring, 'required': True},
            'last_name': {'type': basestring, 'required': True},
            'document_type': {'type': basestring, 'required': True},
            'document_number': {'type': basestring, 'required': True},
            'email': {'type': basestring, 'required': False},
            'mobile': {'type': basestring, 'required': False},
            'address': {'type': address_schema, 'required': False},
            'bank_account_number': {'type': basestring, 'required': False},
            'bank_name': {'type': basestring, 'required': False},
        }, strict=False)

        unit_price_schema = Schema({
            'currency': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
        })

        products_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'quantity': {'type': int, 'required': True},
            'unit_price': {'type': unit_price_schema, 'required': True}
        })

        param_schema = Schema({
            'recipient': {'type': recipient_schema, 'required': True},
            'products': {'type': Array(products_schema), 'required': True},
            'memo': {'type': basestring, 'required': False},
            'out_trade_id': {'type': basestring, 'required': False},
            'currency': {'type': basestring, 'required': True},
            'amount': {'type': numbers.Number, 'required': True},
            'ex_invoice_no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=json.dumps(params),
            url='invoice',
            method='PUT',
        )

    @transfereasy
    def get_invoice(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='invoice',
            method='GET',
        )

    @transfereasy
    def get_invoices(self, params):

        param_schema = Schema({
            'from_created_at': {'type': basestring, 'required': False},
            'to_created_at': {'type': basestring, 'required': False},
            'currency': {'type': basestring, 'required': False},
            'status': {'type': basestring, 'required': False, 'validates': one_of('CREDITED', 'PROCESSING', 'CANCELED')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='invoices',
            method='GET',
        )

    @transfereasy
    def cancel_invoice(self, params):

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='invoice',
            method='DELETE',
        )
