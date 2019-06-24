# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.bank_account import BankAccount
    bacc = BankAccount()

    bank = {
        'name': '招商银行',
        'branch': '北京分行',
        'swift_code': 'CMBCXXXX',
    }

    holder = {
        'name': 'TestHolder',
        'doc_type': 'ID',
        'doc_number': '110101199001010001',
        'contact': '18888888888',
        'type': 'INDIVIDUAL',
        # 'dob': {'type': basestring, 'required': False},
        # 'country': {'type': basestring, 'required': False},
        # 'address': {'type': basestring, 'required': False},
    }

    param = {
        'no': "target-no",
        'bank': bank,
        'country': 'HKG',
        'currency': 'HKD',
        'bank_account_number': 'TEST-99999',
        'holder': holder,
        'purpose': 'PAYER',

        'iban': '00',
    }

    bacc.update_bacc(param)
