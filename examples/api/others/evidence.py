# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.others import Others

    oth = Others()

    param = {
        "url": "https://www.baidu.com/img/bd_logo1.png",
        "file_name": "材料.pdf",
        "transfer_no": "transfer_no",
        "memo": "这⾥⾯包含了本次交易的所有信息"
    }
    oth.evidence(param)
