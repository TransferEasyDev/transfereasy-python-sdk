# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.sub_bankaccount import SubBankAccount

    sbacc = SubBankAccount()
    params = {
        'sub_bank_account_number': 'sub_bank_account_number',
        'from_created_at': '2019-01-01',
        'to_created_at': '2019-02-01',
    }
    sbacc.get_transactions(params)
