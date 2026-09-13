# Serialization
from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


# pip install email-validator
class Patient(BaseModel):
    name: str
    gender: str = "Male"
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
temp = patient1.model_dump()
# model.dump() converting to python dictionaery
print(temp)
# {'name': 'Saras', 'email': 'saras@google.com', 'linkedin_profile': AnyUrl('https://www.linkedin.com/in/saras'), 'age': 1, 'weight': 76.8, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com','phone': '234567'}}
print(type(temp))
# <class 'dict'>


# model_dump_json() exports it to json
temp1 = patient1.model_dump_json()
print(temp)
# {'name': 'Saras', 'email': 'saras@google.com', 'linkedin_profile': AnyUrl('https://www.linkedin.com/in/saras'), 'age': 1, 'weight': 76.8, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com','phone': '234567'}}
print(type(temp1))
# <class 'str'>

temp = patient1.model_dump(include=["name"])
print(temp)

temp = patient1.model_dump(exclude=["name", "gender"])
print(temp)

temp = patient1.model_dump(exclude={"contact_details": ["email"]})
print(temp)

temp = patient1.model_dump(exclude_unset=True)
print(temp)
