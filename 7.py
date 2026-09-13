from pydantic import BaseModel, computed_field
from typing import List, Dict, Optional


# pip install email-validator
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi


patient_details = {"name": "Saras", "age": 1, "weight": 76.8, "height": 9.5}

patient1 = Patient(**patient_details)


def insert_patient_details(patient: Patient):
    print(patient.name)
    print("BMI:", patient.bmi)


insert_patient_details(patient1)
