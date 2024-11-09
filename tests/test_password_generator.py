import pytest
from pages.password_generator_page import PasswordGeneratorPage
from playwright.sync_api import Page

@pytest.fixture
def password_generator_page(page: Page):
    page.goto("https://www.security.org/password-generator/")
    return PasswordGeneratorPage(page)

def test_generate_password_with_recommended_settings(password_generator_page):
    password_generator_page.set_password_length(12)
    password_generator_page.toggle_lowercase(True)
    password_generator_page.toggle_uppercase(True)
    password_generator_page.toggle_numbers(True)
    password_generator_page.toggle_symbols(True)
    password = password_generator_page.get_generated_password()
    assert len(password) == 12, "Password length should be 12"
    assert any(char.isupper() for char in password), "Password should contain uppercase letters"
    assert any(char.islower() for char in password), "Password should contain lowercase letters"
    assert any(char.isdigit() for char in password), "Password should contain numbers"
    assert any(char in password_generator_page.symbols_set for char in password), "Password should contain symbols"

def test_able_to_toggle_options(password_generator_page):
    #the default state is True, True, False, False
    password_generator_page.toggle_lowercase(True)
    password_generator_page.toggle_uppercase(True)
    password_generator_page.toggle_numbers(True)
    password_generator_page.toggle_symbols(True)

    password_generator_page.toggle_lowercase(False)
    password = password_generator_page.get_generated_password()
    assert not any(char.islower() for char in password), "Unable to generate password without lowercase"

    password_generator_page.toggle_uppercase(False)
    password = password_generator_page.get_generated_password()
    assert not any(char.isupper() for char in password), "Unable to generate password without uppercase"

    password_generator_page.toggle_numbers(False)
    password = password_generator_page.get_generated_password()
    assert not any(char.isdigit() for char in password), "Unable to generate password without numbers"

    #need to enable at least one before turning off symbols
    password_generator_page.toggle_lowercase(True)
    password_generator_page.toggle_symbols(False)
    password = password_generator_page.get_generated_password()
    assert not any(char in password_generator_page.symbols_set for char in password), "Unable to generate password without symbols"

def test_password_regenerate(password_generator_page):
    old_password = password_generator_page.get_generated_password()
    password_generator_page.generate_button.click()
    new_password = password_generator_page.get_generated_password()
    assert old_password != new_password, "Unable to regenerate password"

def test_generate_password_with_custom_length(password_generator_page):
    password_generator_page.set_password_length(12)
    password_generator_page.generate_button.click()
    password = password_generator_page.get_generated_password()
    assert len(password) == 12, "Unable to set password length between 6-32"

    password_generator_page.set_password_length(1)
    password_generator_page.generate_button.click()
    password = password_generator_page.get_generated_password()
    assert len(password) == 6, "User was able to set password length to less than min of 6"

    password_generator_page.set_password_length(33)
    password_generator_page.generate_button.click()
    password = password_generator_page.get_generated_password()
    assert len(password) == 32, "User was able to set password length to more than max of 32"

def test_copy_password_to_clipboard(password_generator_page):
    # Grant necessary clipboard permissions
    context = password_generator_page.page.context
    context.grant_permissions(["clipboard-read"])  

    password = password_generator_page.get_generated_password()
    password_generator_page.copy_button.click()
    clipboard = password_generator_page.get_clipboard_content()

    assert password == clipboard, "Copy to clipboard does not work"
