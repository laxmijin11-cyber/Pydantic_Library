from pydantic import BaseModel
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


patient_details = {
    "name": "Saras",
    "age": 1,
    "weight": 76.8,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "abc@gmail.com", "phone": "234567"},
}

patient1 = Patient(**patient_details)


def insert_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient details inserted.")


insert_patient_details(patient1)
