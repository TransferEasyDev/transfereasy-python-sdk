# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.account import Account

    acc = Account()
    params = {
        'org_name': 'Example LTD.',
        'office_op_address': '北京',
        'contact_name': '负责人',
        'contact_email': '1@2.com',
        'contact_phone': '18866669999',
        'contact_country': '中国',
        'contact_address': '北京',
        'contact_position': '法人',
        'website': 'www.example.com',
        'company_type': '有限责任公司 (LLC)',
        'industry': '互联网计算机及电子服务',
        'major_funds_source': '营业收入，住宿及物流',
        'year_transfer_amount': '10000000',
        'piece_transfer_amount': '100000',
        # 'credit_code': '001002003',
        'business_code': '001002003',
        'business_country': 'CHN',
        'register_country': 'HKG',
        'issue_bearer_share': 'true'
    }
    files = {
        'license_file': open('/file_path/upload.png', 'r'),
        'office_reg_addr_evd_file': open('/file_path/upload.png', 'r'),
        'beneficiary_evd_file': open('/file_path/upload.png', 'r'),
        'bank_cert_evd_file': open('/file_path/upload.png', 'r'),
        'ownership_structure_file': open('/file_path/upload.png', 'r')
    }
    acc.company_identification(params, files)
