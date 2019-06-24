# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.account import Account

    acc = Account()
    params = {
        'account': 'your_portal_account',  # 商户平台登录账号
        'password': 'your_portal_password'  # 商户平台登录密码
    }
    acc.development(params)
