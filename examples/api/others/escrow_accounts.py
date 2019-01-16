# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.others import Others

    oth = Others()

    param = {
        'currency': 'HKD',
        'country': 'HKG',
    }
    oth.escrow_accounts(param)
