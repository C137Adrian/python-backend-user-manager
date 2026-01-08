"""
User Management Backend Service (CLI-based)

Description:
    Backend-style user management system implemented in Python.
    This project focuses on core backend concepts such as data modeling,
    validation, error handling, and maintainable code structure.

Author:
    Tu Nombre
Created:
    2026-01-XX
"""

from typing import Dict, List


User = Dict[str, str]

# In-memory storage (simulates a database)
users: List[User] = []


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def create_user(name: str, email: str) -> User:
    """
    Create a validated user dictionary.

    Args:
        name (str): User full name
        email (str): User email address

    Returns:
        User: A validated user dictionary

    Raises:
        ValidationError: If user data is invalid
    """
    validate_name(name)
    validate_email(email)

    return {
        "name": name.strip(),
        "email": email.lower().strip()
    }


def validate_name(name: str) -> None:
    if not name or len(name.strip()) < 2:
        raise ValidationError("Name must contain at least 2 characters")


def validate_email(email: str) -> None:
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format")


def user_exists(email: str) -> bool:
    return any(user["email"] == email for user in users)


def add_user(user: User) -> None:
    """
    Add a user to the in-memory storage.

    Args:
        user (User): User dictionary

    Raises:
        ValidationError: If user already exists
    """
    if user_exists(user["email"]):
        raise ValidationError("User with this email already exists")

    users.append(user)


def get_all_users() -> List[User]:
    """
    Retrieve all users from storage.

    Returns:
        List[User]: List of users
    """
    return users


def run_app() -> None:
    """
    Entry point for the application.
    """
    try:
        add_user(create_user("Juan Pérez", "juan.perez@email.com"))
        add_user(create_user("Ana Gómez", "ana.gomez@email.com"))

        # Intentional duplicate to demonstrate validation
        add_user(create_user("Juan Pérez", "juan.perez@email.com"))

    except ValidationError as error:
        print(f"Validation error: {error}")

    print("\nCurrent users:")
    for user in get_all_users():
        print(user)


if __name__ == "__main__":
    run_app()
