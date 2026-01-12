from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_adidas_flow(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open_sneakers()
    product.open_product()
    product.add_to_bag()
    cart.checkout()
