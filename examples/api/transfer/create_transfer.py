# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.transfer import Transfer

    tran = Transfer()

    param = {
        "beneficiaries": [
            {
                "currency": "HKD",
                "amount": 200,
                "bank_account_number": "TEST-777"
            },
            {
                "currency": "HKD",
                "amount": 1000,
                "bank_account_number": "TEST-777"
            }
        ],
        "send_amount": 0,
        "send_currency": "CNH",
        "purpose": "留学",
        "memo": "测试"
    }
    tran.create_transfer(param)
