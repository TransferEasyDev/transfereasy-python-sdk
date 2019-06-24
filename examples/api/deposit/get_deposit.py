# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.deposit import Deposit
    dep = Deposit()

    param = {
        "no": "deposit_no",
        # "out_trade_id": "your_trade_id"
    }
    dep.get_deposit(param)
