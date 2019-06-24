# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.bank_account import BankAccount
    bacc = BankAccount()

    param = {
        'currency': 'HKD',
        'bank_account_number': 'TEST-99999',
        'purpose': 'PAYER',
    }

    bacc.delete_bacc(param)
