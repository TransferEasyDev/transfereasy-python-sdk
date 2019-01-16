# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.statement import Statement

    statement = Statement()

    param = {
        'from_created_at': '2018-10-01 00:00:00',
        'to_created_at': '2018-10-31 23:59:59',
    }
    statement.download(param)
