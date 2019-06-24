# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.sub_bankaccount import SubBankAccount

    sbacc = SubBankAccount()
    params = {
        'country': "HKG",
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

    sbacc.create_sub_bankaccount(params)
