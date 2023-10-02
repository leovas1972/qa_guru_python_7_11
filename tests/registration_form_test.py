from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Leo')
    registration_page.fill_last_name('VAS')

    registration_page.fill_email('name@example.com')

    registration_page.fill_gender('Male')

    registration_page.fill_phone_number('1234567891')

    registration_page.fill_date_of_birth('1972', 'September', 15 )

    registration_page.fill_subjects('Computer Science')

    registration_page.fill_hobbies('Reading')

    registration_page.upload_picture('foto_1.jpg')

    registration_page.fill_current_address('Moscowskaya Street 18')

    registration_page.fill_state('NCR')

    registration_page.fill_city('Delhi')

    registration_page.submit()

    # THEN
    registration_page.should_be_registered(
        'Leo VAS', 'name@example.com', 'Male', '1234567891',
        '15 September,1972', 'Computer Science','Reading','foto_1.jpg',
        'Moscowskaya Street 18','NCR Delhi')