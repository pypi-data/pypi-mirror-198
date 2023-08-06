from paystack import account

ACCOUNT_CODE = 'ERROR_CODE'


def test_create_subaccount():
    response = account.create_subaccount(business_name='Bitmast C2F', settlement_bank='058',
                                         account_number='XXXXXXX',
                                         percentage_charge=2.0, description='Test account for the C2F application')
    data = response.json()
    assert data.get('status') is True


def test_list_subaccounts():
    response = account.list_subaccounts(perPage=10, page=1)
    data = response.json()
    assert data.get('status') is True


def test_fetch_subaccount():
    response = account.fetch_subaccount(id_or_code=ACCOUNT_CODE)
    data = response.json()
    print(data)
    assert data.get('status') is True


def test_update_subaccount():
    response = account.update_subaccount(
        headers=dict(id_or_code=ACCOUNT_CODE),
        business_name='Bitmast Paygies',
        settlement_bank='058',
        active=False,
        primary_contact_email='friday@duck.com'
    )
    data = response.json()
    assert data.get('status') is True
