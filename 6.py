# Model validator

from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
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

    @model_validator(mode="after")
    def validate_patients(self):
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError(
                "Patients older than 60 years of age must have emergency contact details."
            )
        return self


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

"""
# ⚠️ Deprecation Warning – Fix (Brief)

You're using `@model_validator(mode="after")` as a **classmethod** — but Pydantic now wants it as an **instance method**.

---

## ❌ Old Way (Deprecated)

```python
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    name: str
    age: int

    @model_validator(mode="after")
    @classmethod
    def validate(cls, model):
        return model
```

---

## ✅ New Way (Pydantic 2.12+)

```python
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    name: str
    age: int

    @model_validator(mode="after")
    def validate(self):
        return self
```

---

## 🔍 Key Change

| **Old** | **New** |
|---------|---------|
| `@classmethod` + `model` argument | **No** `@classmethod` + `self` |
| `def validate(cls, model)` | `def validate(self)` |

---

## 🚀 One-Line Summary

> **"Remove `@classmethod` and use `self` instead of `model` — warning gone."** 😊🚀
"""
