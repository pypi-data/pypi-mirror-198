from paystack import charges

# Run selected tests of the PayStack API endpoints
AUTHORIZATION_CODE = 'AUTH_ljdt4e4j'


def test_transaction_charge():
    response = charges.transaction_charge(
        email='',
        amount=1000,
        bank=dict(code='058', account_number='XXXXXXX')
    )
    data = response.json()
    print(data)
    assert data.get('status') is True


def test_initiate_bulk_charge():
    response = charges.initiate_bulk_charge(data=[dict(authorization=AUTHORIZATION_CODE, amount=1000)])
    data = response.json()
    print(data)
    assert data.get('status') is False


def test_list_bulk_charges():
    response = charges.list_bulk_charges(perPage=5, page=1)
    data = response.json()
    print(data)
    assert data.get('status') is True

