# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.exchange import Exchange

    exc = Exchange()

    param = {
        'from_created_at': '2018-10-01 00:00:00',
        'to_created_at': '2018-10-31 23:59:59',
        'sell_currency': 'CNH',
        'buy_currency': 'HKD',
        'status': 'PAYMENT',
    }
    exc.get_exchanges(param)
