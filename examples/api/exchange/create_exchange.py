# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.exchange import Exchange

    exc = Exchange()

    param = {
        "buy_amount": 0,
        "sell_currency": "CNH",
        "sell_amount": 1000,
        "buy_currency": "USD",
        "out_trade_id": "your_trade_id",
    }

    exc.create_exchange(param)
