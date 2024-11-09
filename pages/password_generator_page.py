from playwright.sync_api import Page

class PasswordGeneratorPage:
    def __init__(self, page: Page):
        self.page = page
        self.password_length_input = page.locator("#passwordLength")
        self.lowercase_checkbox = page.locator("#option-lowercase")
        self.lowercase_label = page.locator("label[for='option-lowercase']")
        self.uppercase_checkbox = page.locator("#option-uppercase")
        self.uppercase_label = page.locator("label[for='option-uppercase']")
        self.numbers_checkbox = page.locator("#option-numbers")
        self.numbers_label = page.locator("label[for='option-numbers']")
        self.symbols_checkbox = page.locator("#option-symbols")
        self.symbols_label = page.locator("label[for='option-symbols']")
        self.generate_button = page.get_by_title("Generate password")
        self.copy_button = page.locator('button[title="Copy Password"]')
        self.password_output = page.locator("#password")
        self.symbols_set = set(r"! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~")

    def set_password_length(self, length: int):
        self.password_length_input.fill(str(length))

    def get_generated_password(self) -> str:
        return self.password_output.input_value()

    def get_clipboard_content(self) -> str:
        return self.page.evaluate("navigator.clipboard.readText()")

    def toggle_uppercase(self, enable: bool):
        if self.uppercase_checkbox.is_checked() != enable:
            self.uppercase_label.click()

    def toggle_lowercase(self, enable: bool):
        if self.lowercase_checkbox.is_checked() != enable:
            self.lowercase_label.click()

    def toggle_numbers(self, enable: bool):
        if self.numbers_checkbox.is_checked() != enable:
            self.numbers_label.click()
            
    def toggle_symbols(self, enable: bool):
        if self.symbols_checkbox.is_checked() != enable:
            self.symbols_label.click()