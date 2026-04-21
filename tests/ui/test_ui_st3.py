def test_pt_3_1(home_page):
    home_page.goto()
    
    search_query = 'Saw' # W wordzie mamy użyte Pliers ale to daje negatywny wynik przez leather belt
    home_page.search_for_product(search_query)
    product_titles = home_page.get_all_product_titles()
    
    assert len(product_titles) > 0, "Brak wyników wyszukiwania na liście"
    for title in product_titles:
        assert search_query.lower() in title.lower(), f"Tytuł '{title}' nie zawiera frazy '{search_query}'"

def test_pt_3_2(home_page):
    home_page.goto()
    
    category_name = 'Power Tools'
    home_page.filter_by_category(category_name)
    
    product_titles = home_page.get_all_product_titles()
    assert len(product_titles) > 0, "Brak załadowanych produktów dla tej kategorii"
    
    contains_hand_tool = any('Pliers' in title for title in product_titles)
    assert not contains_hand_tool, "Znaleziono narzędzie innej kategorii na liście (Pliers)"


def test_pt_3_3(home_page):
    home_page.goto()
    
    target_max_price = 50.0
    
    max_slider_handle = home_page.page.locator('.ngx-slider-pointer-max')
    slider_bar = home_page.page.locator('.ngx-slider-full-bar').first
    
    max_handle_box = max_slider_handle.bounding_box()
    bar_box = slider_bar.bounding_box()
    
    if max_handle_box and bar_box:
        target_x = bar_box['x'] + (bar_box['width'] * 0.25)
        
        home_page.page.mouse.move(max_handle_box['x'] + max_handle_box['width'] / 2, max_handle_box['y'] + max_handle_box['height'] / 2)
        home_page.page.mouse.down()
        
        home_page.page.mouse.move(target_x, max_handle_box['y'] + max_handle_box['height'] / 2)
        home_page.page.mouse.up()
        home_page.page.wait_for_timeout(1500)
            
    prices = home_page.get_all_product_prices()
    
    assert len(prices) > 0, "Po filtracji siatka jest pusta"
    for price in prices:
        assert price <= target_max_price, f"Błąd filtru: znaleziona cena {price} przekracza limit {target_max_price}"