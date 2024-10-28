import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given('Launch Chrome browser')
def launch_new(context):
    context.driver = webdriver.Chrome()


@when('Open github sign in page')
def open_new(context):
    context.driver.get("https://github.com/login")


@when('Enter a username "{user}" and a password "{pwd}"')
def enter_new(context, user, pwd):
    context.driver.find_element(By.ID, "login_field").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@when('Click on the Sign in button')
def click_new(context):
    context.driver.find_element(By.XPATH, "//body/div[1]/div[3]/main[1]/div[1]/div[4]/form[1]/div[1]/input[13]").click()


@then('Error messages should appear')
def error_new(context):
    text = context.driver.find_element(By.XPATH, "//body/div[1]/div[3]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]").text
    assert text == "Incorrect username or password."
