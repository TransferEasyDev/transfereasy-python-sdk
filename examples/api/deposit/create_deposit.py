# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.deposit import Deposit
    dep = Deposit()

    param = {
        "currency": "HKD",
        "amount": "1000000",
        "payer_bank_acc_number": "TEST-666",
        # "payer_bank_acc_no": "TEST-666",
        "escrow_bank_acc_number": "20143304",
        "out_trade_id": "your_trade_id"
    }

    dep.create_deposit(param)
