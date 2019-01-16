# -*- coding: utf-8 -*-
import json
from schemer import Schema
from schemer.validators import one_of
from schemer import Schema, Array

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Account(object):
    def __init__(self):
        pass

    @transfereasy
    def create_acc(self, params):
        param_schema = Schema({
            'account': {'type': basestring, 'required': False},
            'password': {'type': basestring, 'required': False},
            'entity_type': {'type': basestring, 'required': True, 'validates': one_of('COMPANY', 'INDIVIDUAL')},
            'secret': {'type': basestring, 'required': False},
            'partner': {'type': basestring, 'required': True},
            'callback_url': {'type': basestring, 'required': False},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

        # 校验数据
        return KeyVariables(
            params=params,
            url='account',
            method='POST',
        )

    def __individual_identification_schema(self, params):
        param_schema = Schema({
            'name': {'type': basestring, 'required': True},
            'country': {'type': basestring, 'required': True},
            'mobile': {'type': basestring, 'required': True},
            'doc_type': {'type': basestring, 'required': True, 'validates': one_of('ID', 'PASSPORT')},
            'doc_number': {'type': basestring, 'required': True},
            'address': {'type': basestring, 'required': True},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

    @transfereasy
    def individual_identification(self, params, files):
        self.__individual_identification_schema(params)
        # 校验数据
        return KeyVariables(
            params=params,
            url='account/individual/identification',
            method='POST',
            files=files
        )

    @transfereasy
    def individual_reidentification(self, params, files):
        self.__individual_identification_schema(params)
        # 校验数据
        return KeyVariables(
            params=params,
            url='account/individual/identification',
            method='PUT',
            files=files
        )

    def __company_identification_schema(self, params):
        param_schema = Schema({
            'org_name': {'type': basestring, 'required': True},
            'office_op_address': {'type': basestring, 'required': True},
            'contact_name': {'type': basestring, 'required': True},
            'contact_email': {'type': basestring, 'required': True},
            'contact_phone': {'type': basestring, 'required': True},
            'contact_country': {'type': basestring, 'required': True},
            'contact_address': {'type': basestring, 'required': True},
            'contact_position': {'type': basestring, 'required': True},
            'website': {'type': basestring, 'required': False},
            'company_type': {'type': basestring, 'required': True,
                             'validates': one_of('有限责任公司 (LLC)', '股份有限公司 (INC)',
                                                 '合伙人', '个人独资', '上市公司',
                                                 '非政府组织/慈善机构', '国有企业')
                             },

            'industry': {'type': basestring, 'required': False,
                         'validates': one_of('旅行，运输，住宿及物流', '办公，工业，汽车以药品器械灯专用品商店',
                                             '生活方式及零售类商店', '互联网计算机及电子服务',
                                             '医疗、教育、咨询等专业服务',
                                             '商业及其他类服务', '国有企业')
                         },

            'major_funds_source': {'type': basestring, 'required': False,
                                   'validates': one_of('营业收入，住宿及物流', '股东出资',
                                                       '投资收益', '借款/贷款', '政府投资',
                                                       '慈善捐款', '其它')
                                   },
            'year_transfer_amount': {'type': basestring, 'required': True},
            'piece_transfer_amount': {'type': basestring, 'required': True},
            'credit_code': {'type': basestring, 'required': False},
            'business_code': {'type': basestring, 'required': True},
            'business_country': {'type': basestring, 'required': True},
            'register_country': {'type': basestring, 'required': True},
            'issue_bearer_share': {'type': basestring, 'required': True, 'validates': one_of('true', 'false')},
        }, strict=False)

        param_schema.validate(params)  # 检测不通过直接抛异常
        param_schema.apply_defaults(params)  # attach 默认值

    @transfereasy
    def company_identification(self, params, files):
        self.__company_identification_schema(params)
        # 校验数据
        return KeyVariables(
            params=params,
            url='account/company/identification',
            method='POST',
            files=files
        )

    @transfereasy
    def company_reidentification(self, params, files):
        self.__company_identification_schema(params)
        # 校验数据
        return KeyVariables(
            params=params,
            url='account/company/identification',
            method='PUT',
            files=files
        )

    @transfereasy
    def get_acc(self):
        return KeyVariables(
            params={},
            url='account',
            method='GET',
        )
