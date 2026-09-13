# Nested models
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    age: int
    address: Address


address_details = {"city": "gurgaon", "state": "haryana", "pin": "201012"}

address1 = Address(**address_details)

patient_details = {"name": "Saras", "age": 1, "address": address1}

patient1 = Patient(**patient_details)


def update_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.address.city)
    print("Patient details updated.")


update_patient_details(patient1)
