# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.sub_bankaccount import SubBankAccount

    sbacc = SubBankAccount()
    params = {
        'apply_no': 'apply_no',
    }
    sbacc.get_progress(params)
