import email
import time


from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch Chrome browser')
def launch(context):
    context.driver = webdriver.Chrome()


@when('I open github sign up page')
def open(context):
    context.driver.get("https://github.com/signup")
    time.sleep(3)


@when('I enter and email address "{email}"')
def enter_email(context, email):
    context.driver.find_element(By.ID, "email").send_keys(email)
    wait_for_continue_button(context)


def wait_for_continue_button(context):
    continue_button_locator = (By.CSS_SELECTOR, "#email-container button")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(continue_button_locator)
    )

@when('I click on the Continue button')
def click(context):
    click_button = context.driver.find_element(By.CSS_SELECTOR, "#email-container button").click()


@when('I enter a password "{pwd}"')
def enter_pwd(context, pwd):
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    wait_for_error(context)

def wait_for_error(context):
    error_mesages_locator = (By.CSS_SELECTOR, "#password-err .password-validity-summary")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(error_mesages_locator)
    )


@then('Invalid password error should be visible')
def close(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "#password-err .password-validity-summary").text
    assert text == "Password is too short"
