# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.invoice import Invoice

    invo = Invoice()

    param = {
        "no": "invoice_no",
        # "out_trade_id": "your_trade_id"
    }
    invo.get_invoice(param)
