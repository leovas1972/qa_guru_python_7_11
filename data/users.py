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
    hobbies: Hobbies
    picture_path: str
    address: str
    state: str
    city: str
