# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from kernel.api.invoice import Invoice

    inv = Invoice()

    param = {
        "recipient": {
            "dob": "1976-08-26",
            "entity_type": "INDIVIDUAL",
            "first_name": "John",
            "last_name": "Walker",
            "document_number": "E12345678",
            "document_type": "CHN/PASSPORT",
            "email": "bill-me@example.com",
            "mobile": "1234567890",
            "bank_account_number": "432100001111",
            "bank_name": "HSBC (HongKong Branch)",
            # "beneficiary_address": "RM 1842, 18/F, RADIO CITY, XXXX, HONGKONG",
            "address": {
                "line1": "1234 First Street",
                "city": "Anytown",
                "state": "CA",
                "postal_code": "98765",
                "country": "USA"
            }
        },
        "products": [
            {
                "name": "Zoom System wireless headphones",
                "quantity": 2,
                "unit_price": {
                    "currency": "USD",
                    "amount": 120
                }
            },
            {
                "name": "Bluetooth speaker",
                "quantity": 4,
                "unit_price": {
                    "currency": "USD",
                    "amount": 45
                }
            }
        ],
        "memo": "Thank you for your business.",
        "out_trade_id": "2018080700361623156020079",
        "currency": "USD",
        "amount": 420
    }
    inv.create_invoice(param)

