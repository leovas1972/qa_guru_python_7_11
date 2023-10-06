from selene.support.shared import browser
from  selene import have, command
from resource import resource_path


class RegistrationPage:

    def __init__(self):
        self.google_ads = browser.all('[id^=google_ads][id$=container__]')
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = lambda gender: browser.all('[name=gender]').element_by(
            have.value(gender.value)).element('..')
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth_element = browser.element('#dateOfBirthInput')
        self.date_of_birth_month = lambda month: browser.element(
            '.react-datepicker__month-select').type(month)
        self.date_of_birth_year = lambda year: browser.element(
            '.react-datepicker__year-select').type(year)
        self.date_of_birth_day = lambda day: browser.element(f'.react-datepicker__day--0{day}')

        self.subject = browser.element('#subjectsInput')
        self.hobbies = lambda hobbies: browser.all('[id^=hobbies][type=checkbox]+label').element_by(
                have.exact_text(hobbies.value)
            )
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.drop_down_list = browser.all('[id^=react-select][id*=option]')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = lambda: browser.element('#submit').press_enter()

        self.registration_confirmation = browser.element('.table').all('td').even



    def open(self):
        browser.open('/automation-practice-form')
        '''
        # might be also needed:
        '''
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
        self.google_ads.with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.google_ads.perform(command.js.remove)


    def register(self, student_leo):
        self.first_name.type(student_leo.first_name)
        self.last_name.type(student_leo.last_name)
        self.email.type(student_leo.email)
        self.gender(student_leo.gender).click()
        self.phone_number.type(student_leo.phone_number)
        self.date_of_birth_element.click()
        self.date_of_birth_month(student_leo.date_of_birth.strftime('%B'))
        self.date_of_birth_year(student_leo.date_of_birth.strftime('%Y'))
        self.date_of_birth_day(student_leo.date_of_birth.strftime('%d')).click()
        self.subject.type(student_leo.subjects).press_tab()
        self.hobbies(student_leo.hobbies).click()
        self.picture.set_value(resource_path(student_leo.picture_path))
        self.address.with_(set_value_by_js=True).set_value(student_leo.address)
        self.state.click()
        self.drop_down_list.element_by(have.exact_text(student_leo.state)).click()
        self.city.click()
        self.drop_down_list.element_by(have.exact_text(student_leo.city)).click()
        self.submit()

    def student_should_be_registered(self, student_leo):
        self.registration_confirmation.should(
            have.exact_texts(
                f'{student_leo.first_name} {student_leo.last_name}',
                student_leo.email,
                student_leo.gender.value,
                student_leo.phone_number,
                f"{student_leo.date_of_birth.strftime('%d')} {student_leo.date_of_birth.strftime('%B')},{student_leo.date_of_birth.strftime('%Y')}",
                student_leo.subjects,
                student_leo.hobbies.value,
                student_leo.picture_path,
                student_leo.address,
                f"{student_leo.state} {student_leo.city}"
            )
        )