from data import users
from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.register(users.student_leo)
    # THEN
    registration_page.student_should_be_registered(users.student_leo)