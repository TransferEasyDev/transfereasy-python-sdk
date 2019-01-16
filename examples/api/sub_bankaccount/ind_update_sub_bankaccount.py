# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import json
    from kernel.api.sub_bankaccount import SubBankAccount

    sbacc = SubBankAccount()

    datas = {
        'no': '4TDLPMTRMDEJWTFCWYG2JE',
        'individual': {
            'name': 'name',
            'country_code': 'USA',
            'mobile': 'mobile',
            'doc_type': 'ID',
            'doc_number': 'doc_number',
            'address': 'address',
        },
        'sub_bank_account': {
            'currency': 'USD',
            'country': 'USA',
        },
        'shop': {
            'type': 'AMAZON',
            'name': 'name',
            'industry': '旅行，运输，住宿及物流',
            'url': 'url',
            'piece_transfer_amount': 1000,
            'week_transfer_amount': 1000,
            'amazon_site': 'USA',
            'business_description': 'business_description',
            'seller_id': 'seller_id',
            'access_key': 'access_key',
            'secret_key': 'secret_key',
        }
    }

    params = {'apply_data': json.dumps(datas)}
    files = {
        'id_file_front': open('/file_path/upload.png', 'r'),
        'id_file_back': open('/file_path/upload.png', 'r'),
        'passport_file': open('/file_path/upload.png', 'r'),
        'address_evd_file': open('/file_path/upload.png', 'r'),
    }
    sbacc.ind_update_sub_bankaccount(params, files)
