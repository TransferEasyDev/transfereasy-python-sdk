# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import json
    from kernel.api.sub_bankaccount import SubBankAccount

    sbacc = SubBankAccount()
    datas = {
        'company': {
                'org_name': 'org_name',
                'office_op_address': 'office_op_address',
                'contact_name': 'contact_name',
                'contact_email': 'contact_email',
                'contact_phone': 'contact_phone',
                'contact_country': 'contact_country',
                'contact_address': 'contact_address',
                'contact_position': 'contact_position',
                'website': 'website',
                'company_type': u'有限责任公司 (LLC)',
                'industry': u'旅行，运输，住宿及物流',
                'major_funds_source': u'营业收入，住宿及物流',
                'year_transfer_amount': 'year_transfer_amount',
                'piece_transfer_amount': 'piece_transfer_amount',
                'credit_code': 'credit_code',
                'business_code': 'business_code',
                'business_country': 'HKG',
                'register_country': 'HKG',
            },
        'sub_bank_account': {
                'currency': 'USD',
                'country': 'USA',
        },
        'shop': {
                'type': 'AMAZON',
                'name': 'name',
                'industry': u'旅行，运输，住宿及物流',
                'url': 'https://www.amazon.com/xxxx',
                'piece_transfer_amount': 1000,
                'week_transfer_amount': 1000,
                'amazon_site': 'USA',
                'business_description': 'business_description',
                'seller_id': 'seller_id',
                'access_key': 'access_key',
                'secret_key': 'secret_key',
        }
    }

    params = {
        'apply_data': json.dumps(datas)
    }

    files = {
        'license_file': open('/file_path/upload.png', 'r'),
        'office_reg_addr_evd_file': open('/file_path/upload.png', 'r'),
        'beneficiary_evd_file': open('/file_path/upload.png', 'r'),
        'bank_cert_evd_file': open('/file_path/upload.png', 'r'),
        'contact_doc_file': open('/file_path/upload.png', 'r'),
        'contact_address_file': open('/file_path/upload.png', 'r'),
    }
    sbacc.com_create_sub_bankaccount(params, files)
