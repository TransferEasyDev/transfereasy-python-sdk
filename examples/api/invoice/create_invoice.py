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



a = {
  "data": {
    "created": "2018-11-14 16:48:11",
    "escrow_account": {
      "bank": {
        "address": "21/F, Bank of America Tower,12 Harcourt Road, Central, Hong Kong",
        "branch": "Hong Kong Branch",
        "bsb_code": "",
        "name": "China Merchants Bank",
        "routing_number": "",
        "sort_code": "",
        "swift_code": "CMBCHKHH"
      },
      "bank_account_name": "SINO ALLIED (HK) LIMITED",
      "bank_account_number": "20561677",
      "beneficiary_address": "RM 1842, 18/F, RADIO CITY, 505-511 HENNESSY ROAD, CAUSEWAY BAY, HONGKONG",
      "country": "HKG",
      "currency": "USD",
      "iban": null,
      "telephone": "00 852 9346 7950"
    },
    "fee_amount": null,
    "fee_currency": "",
    "invoice_amount": 420.0,
    "invoice_currency": "USD",
    "is_canceled": false,
    "is_credit": false,
    "memo": "Thank you for your business.",
    "no": "2018111416481125380",
    "out_trade_id": "2018080700361623156020079",
    "products": [
      {
        "name": "Zoom System wireless headphones",
        "quantity": 2,
        "unit_price": {
          "amount": 120.0,
          "currency": "USD"
        }
      },
      {
        "name": "Bluetooth speaker",
        "quantity": 4,
        "unit_price": {
          "amount": 45.0,
          "currency": "USD"
        }
      }
    ],
    "received_amount": 0,
    "received_currency": "",
    "recipient": {
      "address": {
        "city": "Anytown",
        "country": "USA",
        "line1": "1234 First Street",
        "postal_code": "98765",
        "state": "CA"
      },
      "bank_account_number": "432100001111",
      "bank_name": "HSBC (HongKong Branch)",
      "dob": "1976-08-26",
      "document_number": "E12345678",
      "document_type": "CHN/PASSPORT",
      "email": "bill-me@example.com",
      "entity_type": "INDIVIDUAL",
      "first_name": "John",
      "last_name": "Walker",
      "mobile": "1234567890"
    },
    "reference": "992602"
  },
  "meta": {
    "message": "Requset Success",
    "status_code": 200,
    "success": true
  }
}
