# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.transfer import Transfer

    tran = Transfer()

    param = {
        'no': 'transfer_no',
        # "ex_out_trade_id": "your_trade_id",
        # "new_out_trade_id": "your_trade_id"
    }
    tran.repetition_transfer(param)
