from paystack import bank


def test_list_banks():
    response = bank.list_banks(country='nigeria', perPage=100)
    data = response.json()
    assert data.get('status')
