# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.iat import IAT

    iat = IAT()

    param = {
        'no': 'iat_no',
    }
    iat.repetition_iat(param)
