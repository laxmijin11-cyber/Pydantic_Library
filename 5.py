# Field Validators in Pydantic

from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_profile: Optional[AnyUrl] = None
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    # single field validation
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be out of {valid_domains}")
        return value

    @field_validator("name", mode="after")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        raise ValueError("age must be between 1 to 100")


patient_details = {
    "name": "Saras",
    "age": "1",
    "email": "saras@hdfc.com",
    "linkedin_profile": "https://www.linkedin.com/in/saras",
    "weight": 76.8,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "abc@hdfc.com", "phone": "234567"},
}

patient1 = Patient(**patient_details)


def insert_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.linkedin_profile)
    print("Patient details inserted.")


insert_patient_details(patient1)
