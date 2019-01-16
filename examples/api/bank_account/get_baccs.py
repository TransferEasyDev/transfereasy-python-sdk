# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.bank_account import BankAccount
    bacc = BankAccount()

    param = {
        # 'purpose': 'PAYER',
        # 'status': 'PENDING',
    }

    bacc.get_baccs(param)
