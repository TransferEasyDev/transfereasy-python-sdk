# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.account import Account

    acc = Account()
    params = {
        'name': 'Example',
        'country': 'USA',
        'mobile': '18866669999',
        'doc_type': 'ID',
        'doc_number': '010101199909091010',
        'address': '北京',
    }
    files = {
        'id_file_front': open('/file_path/upload.png', 'r'),
        'id_file_back': open('/file_path/upload.png', 'r'),
        'passport_file': open('/file_path/upload.png', 'r'),
        'address_evd_file': open('/file_path/upload.png', 'r'),
    }
    acc.individual_reidentification(params, files)
