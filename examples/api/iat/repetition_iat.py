# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.iat import IAT

    iat = IAT()

    param = {
        'no': 'iat_no',
        # "ex_out_trade_id": "your_trade_id",
        # "new_out_trade_id": "your_trade_id"
    }
    iat.repetition_iat(param)
