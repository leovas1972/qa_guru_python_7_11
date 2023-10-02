from pathlib import Path
from selene.support.shared import browser
from  selene import have, command, be
import tests


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        '''
        # might be also needed:
        '''
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, name):
        browser.element('#firstName').type(name)

    def fill_last_name(self, name):
        browser.element('#lastName').type(name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type('Computer Science')
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(value)).should(
            be.visible)
        browser.element('#subjectsInput').press_tab()

    def fill_hobbies(self, hobby):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        # browser.element('[for=hobbies-checkbox-2]').click()
        browser.all('[id^=hobbies][type=checkbox]+label').element_by(
            have.exact_text(hobby)
        ).click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').set_value(
            str(Path(tests.__file__).parent.joinpath(
                f'resources/{file_name}').absolute()))

    def fill_current_address(self, address):
        browser.element('#currentAddress').with_(set_value_by_js=True).set_value(address)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_be_registered(self,full_name, email, gender, phone,
                             birthday, value, hobbies, picture, address, state ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                birthday,
                value,
                hobbies,
                picture,
                address,
                state,
            )
        )
