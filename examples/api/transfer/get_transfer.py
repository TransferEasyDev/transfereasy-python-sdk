# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.transfer import Transfer

    tran = Transfer()

    param = {
        "no": "transfer_no"
    }
    tran.get_transfer(param)
