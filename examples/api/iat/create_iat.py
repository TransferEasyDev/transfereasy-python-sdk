# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.iat import IAT

    iat = IAT()

    param = {
        'beneficiary_account_name': 'benefi@example.com',
        'beneficiary_account_no': 'beneficiary_account_no',
        'send_amount': 1000,
        'send_currency': 'USD',
        "purpose": "留学",
        "memo": "测试"
    }
    iat.create_iat(param)
