# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.deposit import Deposit
    dep = Deposit()

    param = {
        "no": "deposit_no",
    }
    dep.cancel_deposit(param)
