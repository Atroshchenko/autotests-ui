from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
              wait_until = 'networkidle'
              )

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.is_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    u_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    u_name_input.fill("username")

    pass_input = page.get_by_test_id('registration-form-password-input').locator('input')
    pass_input.fill("password")

    reg_button.is_enabled()

    page.wait_for_timeout(3000)  # используется только для этого теста для понимания что происходит