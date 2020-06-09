from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
gb_link = 'https://geekbrains.ru/'
browser.get(gb_link)
wait = WebDriverWait(browser, 10)

# Authorisation on Geekbrains
user_name = input("Enter your username: ")
user_password = input("Enter your password: ")
link_for_search = input("Enter a link for search: ")

# enter your email
user_name_input = WebDriverWait(browser, 100, 1).until(expect.visibility_of_element_located(
    (By.XPATH, "//input[@placeholder='Email']")))
user_name_input.send_keys(user_name)

# enter your password
user_password_input = WebDriverWait(browser, 100, 1).until(expect.visibility_of_element_located(
    (By.XPATH, "//input[@placeholder='Пароль']")))
user_password_input.send_keys(user_password)

# press button to login
press_button_login = browser.find_element_by_id('registration-form-button').click()

# switch to a required page with a teacher's feedbacks
browser.get(link_for_search)

# click on the button to expend list of student's feedbacks
while True:
    try:
        expand_feedbacks_button = wait.until(
            expect.element_to_be_clickable((By.CLASS_NAME, 'feedbacks-get-more-feedbacks-button')))
        actions = ActionChains(browser)
        actions.move_to_element(expand_feedbacks_button)
        expand_feedbacks_button.click()
    except Exception as e:
        print(e, 'Looks like there are no more feedbacks')
        print("Now you can read ALL feedbacks")
        break
