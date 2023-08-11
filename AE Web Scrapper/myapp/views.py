from flask import render_template, Blueprint, url_for, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from .models import AmericanEagleProduct, db, URLForm

views = Blueprint('views', __name__)

# add a home page
@views.route('/', methods=['GET', 'POST'])
def home():
    form = URLForm()
    if form.validate_on_submit():
        url = form.AEWeb_url.data
        # Call the search_url function with the submitted URL to perform web scraping
        search_url(url)
        # Redirect to the /table_one URL to display the scraped data
        return redirect(url_for('views.display_table_one'))
    return render_template("home.html", form=form)


def create_driver():
    return webdriver.Chrome()

def find_element_safe(locator, by, value):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            element = locator.find_element(by, value)
            return element
        except StaleElementReferenceException:
            attempts += 1
    return None

def check_if_sale_exists(locator):
    try:
        price_with_sale = locator.find_element(By.XPATH, './/div[contains(@class, "product-sale-price")]')
        zero = price_with_sale.text
        one = True
        return zero, one
    except NoSuchElementException:
        zero = 'null'
        one = False
        return zero, one

def check_if_promo_exists(locator):
    try:
        promo_element = locator.find_element(By.XPATH, './/span[contains(@class, "product-promotional")]')
        zero = promo_element.text
        one = True
        return zero, one
    except NoSuchElementException:
        zero = 'null'
        one = False
        return zero, one

product_type_categories = {
                    "Shirt","Boxer Short","Boxer Brief","Pant",
                    "Jogger","Hoodie","Sweater","Henley","Jean",
                    "Khakis","Utility Pant","Boot","Tee", "Shacket",
                    "Jacket","Legging"
} 


def search_url(url):
    driver = create_driver()
    driver.get(url)
    driver.implicitly_wait(3)
    products = driver.find_elements(By.CLASS_NAME,'product-tile.qa-product-tile.__eadf2')
    for product in products:
        product_name = find_element_safe(product, By.XPATH, './/h3[contains(@class, "product-name")]').text
        product_type = next((category for category in product_type_categories if category in product_name), "null")
        price = product.find_element(By.XPATH, './/div[contains(@class, "product-list-price")]').text
        discount_price, on_sale = check_if_sale_exists(product)
        promo, has_promo = check_if_promo_exists(product)
        new_data = AmericanEagleProduct(product_name=product_name,product_type=product_type,price=price,discount_price=discount_price,on_sale=on_sale,promo=promo,has_promo=has_promo)
        db.session.add(new_data)
    db.session.commit()
    driver.quit()
    return redirect(url_for('views.display_table_one'))

@views.route('/table_one', methods=['GET','POST'])
def display_table_one():
    ae_data_list = AmericanEagleProduct.query.all()
    return render_template('table_one.html', ae_data_list=ae_data_list, product_type_categories=product_type_categories)




