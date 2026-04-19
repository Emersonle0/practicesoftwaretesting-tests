import requests

# NOTE PT 1.3 is not testable (no documentation form endpoint /aut/login and no easy way to authenticate using Google without developer account)

def test_pt1_1(random_email: str):
    # arrange
    payload = {
        'first_name': 'foo',
        'last_name': 'bar',
        'address': {
            'street': 'test 4/20',
            'city': 'Łódź',
            'state': 'test',
            'country': 'Poland',
            'postal_code': '01-001'},
        'phone': '2137',
        'dob': '2000-01-01',
        'password': 'Poziomka13.',
        'email': random_email}
    
    # act
    response = requests.post(
        'https://api.practicesoftwaretesting.com/users/register',
        json=payload)
    
    # assert
    assert response.status_code == 201

def test_pt1_2(random_email: str):
    # arrange
    payload = {
        'first_name': 'foo',
        'last_name': 'bar',
        'address': {
            'street': 'test 4/20',
            'city': 'Łódź',
            'state': 'test',
            'country': 'Poland',
            'postal_code': '01-001'},
        'phone': '2137',
        'dob': '2000-01-01',
        'password': 'Poziomka13.',
        'email': random_email}
    requests.post(
        'https://api.practicesoftwaretesting.com/users/register',
        json=payload)
    
    # act
    response = requests.post(
        'https://api.practicesoftwaretesting.com/users/register',
        json=payload)

    # assert
    assert response.status_code == 409
    assert response.json().get('email') is not None