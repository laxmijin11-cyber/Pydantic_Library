from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


# pip install email-validator
class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_profile: Optional[AnyUrl] = None
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


patient_details = {
    "name": "Saras",
    "age": 1,
    "email": "saras@google.com",
    "linkedin_profile": "https://www.linkedin.com/in/saras",
    "weight": 76.8,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "abc@gmail.com", "phone": "234567"},
}

patient1 = Patient(**patient_details)


def insert_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.linkedin_profile)
    print("Patient details inserted.")


insert_patient_details(patient1)
