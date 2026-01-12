"""
User Management Backend Service (CLI-based)

Description:
    Backend-style user management system implemented in Python.
    This project focuses on core backend concepts such as data modeling,
    validation, error handling, and data persistence.

Author:
    Tu Nombre
Created:
    2026-01-XX
"""

from typing import Dict, List
from pathlib import Path
import json


User = Dict[str, str]

DATA_FILE = Path("data.json")

# In-memory storage (simulates a database)
users: List[User] = []


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


# ----------------------
# Persistence Layer
# ----------------------

def load_users() -> None:
    """Load users from JSON file into memory."""
    global users

    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            users = json.load(file)


def save_users() -> None:
    """Save users from memory to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


# ----------------------
# Validation
# ----------------------

def validate_name(name: str) -> None:
    if not name or len(name.strip()) < 2:
        raise ValidationError("Name must contain at least 2 characters")


def validate_email(email: str) -> None:
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format")


def user_exists(email: str) -> bool:
    return any(user["email"] == email for user in users)


# ----------------------
# Business Logic
# ----------------------

def create_user(name: str, email: str) -> User:
    validate_name(name)
    validate_email(email)

    return {
        "name": name.strip(),
        "email": email.lower().strip()
    }


def add_user(user: User) -> None:
    if user_exists(user["email"]):
        raise ValidationError("User with this email already exists")

    users.append(user)


def get_all_users() -> List[User]:
    return users


# ----------------------
# Application
# ----------------------

def run_app() -> None:
    load_users()

    try:
        add_user(create_user("Juan Pérez", "juan.perez@email.com"))
        add_user(create_user("Ana Gómez", "ana.gomez@email.com"))
    except ValidationError as error:
        print(f"Validation error: {error}")

    print("\nCurrent users:")
    for user in get_all_users():
        print(user)

    save_users()


if __name__ == "__main__":
    run_app()
