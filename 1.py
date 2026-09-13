from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int


# patient_details = {
#     "name": "Saras",
#     "age": True,
# }
# This will raise a validation error because age should be an int, not a bool
# True=1

patient_details = {
    "name": "Saras",
    "age": 1.75,
}


patient1 = Patient(**patient_details)


def insert_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient details inserted.")


insert_patient_details(patient1)
