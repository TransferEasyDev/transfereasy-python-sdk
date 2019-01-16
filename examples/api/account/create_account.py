# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.account import Account
    acc = Account()
    params = {
        'account': 'example@test.com',
        'password': '123456',
        'entity_type': 'COMPANY',
        # 'entity_type': 'INDIVIDUAL',
        'secret': 'your_secret',
        'partner': 'your_partner_id',
        'callback_url': 'http://your_callback_url',
    }
    acc.create_acc(params)
