# Field:
# 1.set default values
# 2.constraints like age between 0 to 100, weight between 0 to 200
# 3.metadata add-title,description,example in fastapi swagger ui docs
# 4.used for both numeric and str data types


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# pip install email-validator
class Patient(BaseModel):
    name: str = Field(
        ...,
        json_schema_extra={
            "title": "Patient Name",
            "max_length": 100,
            "description": "Name of the patient",
            "example": ["Saras", "Vineeta"],
        },
    )
    linkedin_profile: Optional[AnyUrl] = None
    age: int = Field(gt=0, lt=60)
    weight: Annotated[float, Field(gt=0, lt=200, strict=True)]
    married: Annotated[
        Optional[bool],
        Field(
            json_schema_extra={"description": "if person is married or not"},
            default=None,
        ),
    ]
    # Trailing comma is optional — Python allows it. It's just a style choice.
    allergies: Optional[List[str]] = Field(max_length=5, default=None)
    contact_details: Annotated[
        Dict[str, str],
        Field(
            max_length=2,
            description="Contact details of the patient",
            json_schema_extra={"example": {"email": "abc@gmail.com"}},
        ),
    ]


patient_details = {
    "name": "Saras",
    "age": 1,
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
    print(patient.weight)
    print(patient.linkedin_profile)
    print("Patient details inserted.")


insert_patient_details(patient1)

#  pip show pydantic

"""
The output is correct:
```
Saras
1
True
https://www.linkedin.com/in/saras
Patient details inserted.
```

The yellow warning is **not an error** — it's just a deprecation notice.

---

## ⚠️ About the Warning

| **Issue** | **Fix** |
|-----------|---------|
| `Using extra keyword arguments on Field is deprecated` | Use `json_schema_extra` instead of `example` |

### ❌ Old Way (Deprecated)
```python
name: str = Field(..., example="Saras")
```

### ✅ New Way (Pydantic V2)
```python
name: str = Field(..., json_schema_extra={"example": "Saras"})
```

---

## 🔍 Why It's Just a Warning

| **Term** | **Meaning** |
|----------|-------------|
| **Deprecated** | Still works, but will be removed in future |
| **Warning** | Not an error — code runs fine |
| **V2 Migration** | Pydantic is upgrading syntax; old syntax still supported |

---

## ✅ Action

| **If You...** | **Do This** |
|---------------|-------------|
| Just learning | ✅ Ignore the warning — code works |
| Building production | ✅ Update to `json_schema_extra` |
| Want clean output | ✅ Fix it in 10 seconds |

---

## 🚀 One-Line Summary

> **"Your code works! The warning is just Pydantic telling you to use `json_schema_extra` instead of `example`."** 😊🚀

------------------------------------------------

ques:instead of annotated we use json_schema_extra now?

ANSWER:
# `Annotated` vs `json_schema_extra` – Clear Answer

**No — they are not replacements for each other. They do different things.**

| **Feature** | **`Annotated`** | **`json_schema_extra`** |
|-------------|-----------------|-------------------------|
| **Purpose** | Adds metadata/validation to a type | Adds extra JSON schema info (examples, descriptions) |
| **Used For** | Constraints like `gt`, `lt`, `max_length` | Adding `example`, `description`, custom schema keys |
| **Replacement For** | Nothing — it's a wrapper | The old `Field(..., example="...")` syntax |

---

## ✅ Correct Usage

### `Annotated` – For Type-Level Metadata
```python
from typing import Annotated
from pydantic import Field

age: Annotated[int, Field(gt=0, lt=60)]
```

### `json_schema_extra` – For Adding Schema Info
```python
from pydantic import Field

name: str = Field(json_schema_extra={"example": "Saras"})
```

---

## 🔍 What Changed in Pydantic V2

| **Old (V1)** | **New (V2)** |
|--------------|--------------|
| `Field(..., example="Saras")` | `Field(..., json_schema_extra={"example": "Saras"})` |
| `Field(..., description="...")` | `Field(..., description="...")` ✅ Still works |

---

## ✅ Your Code – Corrected

```python
contact_details: Annotated[
    Dict[str, str],
    Field(
        max_length=2,
        description="Contact details of the patient",
        json_schema_extra={"example": {"email": "abc@gmail.com"}}
    )
]
```

---

## 🚀 One-Line Summary

> **"`Annotated` wraps the type; `json_schema_extra` adds example/schema info. Use both together — not instead of each other."** 😊🚀
------------------------------------------------
ques:age: Annotated[int, Field(gt=0, lt=60)]
age: int= Field(gt=0, lt=60) it can work as well
ANSWER:

**Yes, both work identically.** 

Both apply the same constraints (`gt=0`, `lt=60`) to the `age` field.

| **Syntax** | **How It Works** | **When to Use** |
|------------|------------------|-----------------|
| `age: int = Field(gt=0, lt=60)` | Default value + constraints in one line | **Simple, cleaner** |
| `age: Annotated[int, Field(gt=0, lt=60)]` | Type-level metadata, separated from default | **Reusable, complex cases** |

---

## ✅ Example (Both Work)

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Patient(BaseModel):
    # Method 1
    age: int = Field(gt=0, lt=60)
    
    # Method 2
    weight: Annotated[float, Field(gt=0, lt=200)]
```

Both are valid.

---

## 🎯 When to Prefer `Annotated`

| **Use `Annotated` when...** | **Use `Field()` directly when...** |
|-----------------------------|-----------------------------------|
| You want to reuse the type elsewhere | It's a one-off field |
| You're combining multiple validators | Simple constraints |
| You want to separate type from default | You want concise code |

---

## 🚀 One-Line Summary

> **"Both work. `Annotated` is better for reuse; `Field()` directly is cleaner for one-off fields."** 😊🚀
"""
