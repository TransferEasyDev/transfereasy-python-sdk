# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.exchange import Exchange

    exc = Exchange()

    param = {
        'no': 'exchange_no',
    }
    exc.payment(param)
