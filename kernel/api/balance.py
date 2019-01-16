# -*- coding: utf-8 -*-
from schemer import Schema

from kernel.request_sign import transfereasy
from kernel.key_variables import KeyVariables


class Balance(object):
    def __init__(self):
        pass

    @transfereasy
    def get_balance(self, params):
        # 校验数据
        return KeyVariables(
            params=params,
            url='account/wallet/balance',
            method='GET',
        )
