# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.bank_account import BankAccount
    bacc = BankAccount()

    param = {
        'bank_account_number': 'TEST-777',
        'purpose': 'PAYER',
        'currency': 'HKD',
    }

    bacc.get_bacc(param)
