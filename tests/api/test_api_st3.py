import requests

def test_pt3_1():
    search_query = 'Saw'

    response = requests.get(
        'https://api.practicesoftwaretesting.com/products/search',
        params={
            'q': search_query})
    assert response.status_code == 200

    products = response.json()['data']
    assert len(products) > 0

    assert all(search_query.lower() in x['name'].lower() for x in products)

def test_pt3_2():
    category_query = 'Power Tools'

    category_response = requests.get(
        'https://api.practicesoftwaretesting.com/categories/search',
        params={
            'q': category_query})
    category_ids_str = ','.join(x['id'] for x in category_response.json()[0]['sub_categories'])

    response = requests.get(
        'https://api.practicesoftwaretesting.com/products',
        params={
            'by_category': category_ids_str})
    assert response.status_code == 200

    products = response.json()['data']
    assert len(products) > 0
    assert not any('pliers' in x['name'].lower() for x in products)

def test_pt3_3():
    price_min = 10
    price_max = 50

    response = requests.get(
        'https://api.practicesoftwaretesting.com/products',
        params={
            'between': f'price,{price_min},{price_max}'})
    assert response.status_code == 200

    products = response.json()['data']
    assert len(products) > 0
    assert all(price_min <= x['price'] <= price_max for x in products)