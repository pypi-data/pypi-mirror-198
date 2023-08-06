from paystack import transaction

DUMMY_PAYMENT_REF = 'BSID-48759'
AUTHORIZATION_CODE = 'AUTH_xxxxx'


def test_initialize_transaction():
    response = transaction.initialize_transaction(
        amount=1000,
        currency='NGN',
        email='friday@duck.com',
        reference=DUMMY_PAYMENT_REF,
        channels='card'
    )
    data = response.json()
    assert data.get('status')
    assert data.get('authorization_url')


def test_verify_transaction():
    response = transaction.verify_transaction(reference=DUMMY_PAYMENT_REF)
    data = response.json()
    print(data)
    assert data.get('status')


def test_check_authorization():
    response = transaction.check_authorization(
        email='friday@duck.com',
        amount=1000,
        authorization_code=AUTHORIZATION_CODE
    )
    data = response.json()
    assert data.get('status')
