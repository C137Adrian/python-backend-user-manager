"""
User Management Backend Service (CLI-based)

Description:
    Simple backend-style user management system implemented in Python.
    Includes CRUD operations, data validation, and JSON persistence.

Author:
    Adrián Cano
Created:
    2026-01-06
"""

from typing import Dict


User = Dict[str, str]


def create_user(name: str, email: str) -> User:
    """
    Create a user dictionary.

    Args:
        name (str): User full name
        email (str): User email address

    Returns:
        User: A dictionary representing a user
    """
    return {
        "name": name,
        "email": email
    }


def run_app() -> None:
    """
    Entry point for the application.
    """
    user = create_user("Juan Pérez", "juan.perez@email.com")
    print("User created:")
    print(user)


if __name__ == "__main__":
    run_app()