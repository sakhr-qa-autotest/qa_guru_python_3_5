import os

from selene import have
from selene.support.shared import browser

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, './photos/user1.jpg')


def test_filling_form_personal_data():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Pavel')
    browser.element('#lastName').type('Durov')
    browser.element('#userEmail').type('durov@vk.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(99999999999)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1984"]').click()
    browser.element('.react-datepicker__month-select>[value="10"]').click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('Karnal')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Pavel Durov',
        'durov@vk.com',
        'Male',
        '9999999999',
        '10 November,1984',
        'Physics',
        'Reading',
        'user1.jpg',
        'Karnal',
        'Haryana Karnal'
    )
    )
