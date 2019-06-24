# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.iat import IAT

    iat = IAT()

    param = {
        "no": "iat_no",
        # "out_trade_id": "your_trade_id",
    }
    iat.get_iat(param)
