import random
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    random_number = random.randrange(0,1999)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gymlog.ru/")
    page.get_by_role("link", name="Регистрация").click()
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("1")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("f")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("а")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("kdgdgk@")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("@mail.ru")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("<script>alert('test')")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("SELECT * FROM users")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill(";;:123@^$#")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill(";;:123@mail")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill(";;:123@mail.ru")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("афыафаф")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("афыафаф@")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("афыафаф@mail")
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("тестпочта@mail.ru")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("testmail" + str(random_number) + "@mail.ru")
    page.get_by_role("button", name="Начать работу бесплатно").click()
    page.get_by_role("link", name="Выйти").click()
    page.goto("https://gymlog.ru/")
    page.get_by_role("link", name="Вход").click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Запомнить").click()
    page.get_by_role("button", name="Войти").click()
    page.locator("#email").click()
    page.locator("#email").fill("User492")
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Запомнить").click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Запомнить").click()
    page.get_by_label("Пароль *").click()
    page.get_by_label("Пароль *").fill("rbltJT")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Выйти").click()
    page.get_by_role("link", name="Вход").click()
    page.get_by_label("Пароль *").click()
    page.get_by_label("Пароль *").fill("rbltJT")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Пароль *").click()
    page.get_by_label("Пароль *").fill("")
    page.locator("#email").click()
    page.locator("#email").fill("lamap55129@fenxz.com")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("insertion").click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Пароль *").click()
    page.get_by_label("Пароль *").fill("rbltJT")
    page.get_by_role("button", name="Войти").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
