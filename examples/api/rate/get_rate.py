# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.rate import Rate
    rate = Rate()

    param = {
        'sell_currency': 'USD',
        'buy_currency': 'CNY',
    }

    rate.get_rate(param)
