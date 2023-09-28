from selene.support.shared import browser
from selene import have, command
import os


def test_registration_form(open_browser):
    browser.open('/automation-practice-form')

    browser.element('#firstName').set_value('Vasilii')
    browser.element('#lastName').set_value('Leontev')

    browser.element('#userEmail').set_value('obirvalg@gmail.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    browser.element('#userNumber').set_value('1234567899')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('September')
    browser.element('.react-datepicker__year-select').type('1972')
    browser.element(f'.react-datepicker__day--0{15}').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#hobbies-checkbox-1 + label').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/foto_1.jpg'))

    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
    browser.element('#currentAddress').set_value('Novomoscovskay Street 99')

    browser.element('#submit').click()

    browser.element('.table').all('td').even.should(
        have.texts('Vasilii Leontev',
            'obirvalg@gmail.com',
            'Male',
            '1234567899',
            '15 September,1972',
            'Computer Science',
            'Sports',
            'foto_1.jpg',
            'Novomoscovskay Street 99',
            '',))