import dataclasses
from datetime import date
from  enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: date
    subjects: str
    hobbies: Hobbies.reading
    picture_path: str
    address: str
    state: str
    city: str

student_leo = User(
    first_name='Leo',
    last_name='VAS',
    email='name@example.com',
    gender=Gender.male,
    phone_number='1234567891',
    date_of_birth=date(1972,9,15),
    subjects='Computer Science',
    hobbies=Hobbies.reading,
    picture_path='foto_1.jpg',
    address='Moscowskaya Street 18',
    state='NCR',
    city='Delhi'
)

