# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.exchange import Exchange

    exc = Exchange()

    param = {
        "no": "exchange_no",
        # "out_trade_id": "your_trade_id",

    }
    exc.get_exchange(param)
