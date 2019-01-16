# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.invoice import Invoice

    invo = Invoice()

    param = {
        "no": "invoice_no"
    }
    invo.get_invoice(param)
