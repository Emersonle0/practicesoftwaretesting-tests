import requests

def test_pt2_1(shopping_cart: str):
    # arrange
    product_id = requests.get('https://api.practicesoftwaretesting.com/products').json()['data'][0]['id']

    # act
    response = requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product_id,
            'quantity': 1,
        })
    
    # assert
    assert response.status_code == 200

    cart_response = requests.get(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}')
    cart_items = cart_response.json()['cart_items']
    assert any(x['product_id'].lower() == product_id.lower() for x in cart_items)

def test_pt2_2(shopping_cart: str):
    # arrange
    product_id = requests.get('https://api.practicesoftwaretesting.com/products').json()['data'][0]['id']
    requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product_id,
            'quantity': 1,
        })
    
    # act
    response = requests.delete(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}/product/{product_id}')

    # assert
    assert response.status_code == 204

    cart_response = requests.get(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}')
    cart_items = cart_response.json()['cart_items']

    assert len(cart_items) == 0

def test_pt2_3(shopping_cart: str):
    # NOTE POST /carts/{cartId} route probably has a bug which results in a wrong error being returned
    
    # arrange
    product_id = requests.get('https://api.practicesoftwaretesting.com/products').json()['data'][0]['id']

    # act
    response = requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product_id,
            'quantity': -1,
        })
    
    # assert
    assert response.status_code == 422
    assert response.json()['message']['errors'].get('quantity') is not None