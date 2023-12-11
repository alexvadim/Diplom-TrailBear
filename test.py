import allure
from TrailBearPage import TrailBearHelper
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from allure_commons.types import AttachmentType


@allure.title('Тест mywork')
@allure.feature('Проверка click mywork')
@allure.story('Проверка ссылки Мои работы ')
def test_click_mywork(browser):
    with allure.step('Открыть сайт'):
        mywork = TrailBearHelper(browser)
        mywork.go_to_site()
    with allure.step('Кликнуть Мои работы'):
        mywork.click_mywork()
    mywork.mens_bag()
    allure.attach(mywork.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert mywork.mens_bag() == "Сумка мужская", "Ошибка!"


@allure.title('Тест reviews')
@allure.feature('Проверка click reviews')
@allure.story('Проверка ссылки Отзывы ')
def test_click_reviews(browser):
    with allure.step('Навести на кнопку отзывы'):
        reviews = TrailBearHelper(browser)
    with allure.step('Кликнуть Отзывы'):
        reviews.click_reviews()
    reviews.consultation()
    allure.attach(reviews.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert reviews.consultation() == "Есть вопросы? Нужна консультация?", "Ошибка!"


@allure.title('Тест feedback')
@allure.feature('Проверка click feedback')
@allure.story('Проверка ссылки Контакты ')
def test_click_feedback(browser):
    with allure.step('Навести на кнопку контакты'):
        feedback = TrailBearHelper(browser)
    with allure.step('Кликнуть Контакты'):
        feedback.click_feedback()
    feedback.trail_bear()
    allure.attach(feedback.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert feedback.trail_bear() == "TrailBear", "Ошибка!"


@allure.title('Тест vk')
@allure.feature('Проверка ссылки на сайт vk.com')
@allure.story('Проверка ссылки vk ')
def test_click_vk(browser):
    with allure.step('Навести на кнопку vk'):
        vk = TrailBearHelper(browser)
    with allure.step('Кликнуть vk'):
        vk.click_vk()
    url = browser.current_url
    allure.attach(vk.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert url != 'https://vk.com/misha0382'

@allure.title('Тест whatsapp')
@allure.feature('Проверка ссылки на сайт api.whatsapp.com')
@allure.story('Проверка ссылки whatsapp ')
def test_click_whatsapp(browser):
    with allure.step('Навести на кнопку whats app'):
        whatsapp = TrailBearHelper(browser)
    with allure.step('Кликнуть whatsapp'):
        whatsapp.click_whatsapp()
    url = browser.current_url
    allure.attach(whatsapp.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert url != 'https://api.whatsapp.com/send/?phone=79969574045&text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C+%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE+%D1%83%D0%B7%D0%BD%D0%B0%D1%82%D1%8C+%D0%BE+%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B5&type=phone_number&app_absent=0'

@allure.title('Тест TrailBear')
@allure.feature('Проверка кнопки TrailBear')
@allure.story('Проверка кнопки TrailBear ')
def test_click_trailbear(browser):
    with allure.step('Навести на кнопку trailbear'):
        trailbear = TrailBearHelper(browser)
    with allure.step('Кликнуть trailbear'):
        trailbear.click_trailbear()
    allure.attach(trailbear.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

@allure.title('Тест подачи заявки')
@allure.feature('Проверка подачи заявки')
@allure.story('Проверка подачи заявки ')
def test_application(browser):
    with allure.step('Навести на поля для заполнения заявки'):
        application = TrailBearHelper(browser)
    with allure.step('Ввод данных и клик по кнопке оставить заявку'):
        application.submityourapplication()
    allure.attach(application.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест заказа товара')
@allure.feature('Проверка заказа товара')
@allure.story('Проверка заказа товара ')
def test_order(browser):
    with allure.step('Навести на товар сумка мужская'):
        order = TrailBearHelper(browser)
    with allure.step('Клик по кнопке заказать ввод данных и клик по кнопке оформить'):
        order.order_a_product()
    allure.attach(order.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert order.form_order() == "Заказать товар", "Ошибка!"

@allure.title('Тест кнопки вверх')
@allure.feature('Проверка кнопки вверх')
@allure.story('Проверка кнопки вверх ')
def test_click_button(browser):
    with allure.step('Навести на кнопку вверх'):
        button = TrailBearHelper(browser)
    with allure.step('Кликнуть кнопку вверх'):
        button.click_button()
    allure.attach(button.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert button.handmade_products() == "TrailBear\nИзделия\nручной работы\nиз кожи", "Ошибка!"
