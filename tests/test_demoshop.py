import allure
from utils.base_session import demoshop
from models import helpers

@allure.parent_suite('API')
@allure.suite('Авторизация')
@allure.title(f"Вход с помощью логин/пароля")
def test_login():
    response = demoshop.post('/login', data=helpers.user_login(), allow_redirects=False)
    assert response.status_code == 302

@allure.parent_suite('API')
@allure.suite('Корзина')
@allure.title(f"Добавление товара в корзину")
def test_add_cart():
    response = demoshop.post('/addproducttocart/catalog/31/1/1')
    assert response.status_code == 200

@allure.parent_suite('API')
@allure.suite('Корзина')
@allure.title(f"Добавление товара и удаление ее из корзины")
def test_delete_cart(register):
    register.open('')
    resource = demoshop.post('/addproducttocart/catalog/31/1/1')
    register.element('.ico-cart').click()
    register.element('.qty-input').clear().send_keys(0).press_enter()
    assert resource.status_code == 200


@allure.parent_suite('API')
@allure.suite('Авторизация')
@allure.title(f"Выход из аккаунта")
def test_logout(register):
    register.open('')
    register.element('.ico-logout').click()
    response = demoshop.get('/logout', allow_redirects=False)
    assert response.status_code == 302
