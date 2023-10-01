from selene.support.shared import browser
from selene import have, be
from selene import command
import os
import tests


def test_registration_form():
    browser.open('/automation-practice-form')
    '''
    # might be also needed:
    '''
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Leo')
    browser.element('#lastName').type('VAS')

    browser.element('#userEmail').type('name@example.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    browser.element('#userNumber').type('1234567891')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('September')
    browser.element('.react-datepicker__year-select').type('1972')
    browser.element(f'.react-datepicker__day--0{15}').click()

    browser.element('#subjectsInput').type('Computer Science')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Computer Science')).should(be.visible)
    browser.element('#subjectsInput').press_tab()

    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto_1.jpg')
        )
    )

    browser.element('#currentAddress').with_(set_value_by_js=True).set_value('Moscowskaya Street 18')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#submit').press_enter()

    # THEN

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Leo VAS',
            'name@example.com',
            'Male',
            '1234567891',
            '15 September,1972',
            'Computer Science',
            'Reading',
            'foto_1.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )