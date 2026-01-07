"""
User Management Backend Service (CLI-based)

Description:
    Backend-style user management system implemented in Python.
    This project focuses on core backend concepts such as data modeling,
    clean architecture, and maintainable code structure.

Author:
    Tu Nombre
Created:
    2026-01-XX
"""

from typing import Dict, List


User = Dict[str, str]

# In-memory storage (simulates a database)
users: List[User] = []


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


def add_user(user: User) -> None:
    """
    Add a user to the in-memory storage.

    Args:
        user (User): User dictionary
    """
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
    add_user(create_user("Juan Pérez", "juan.perez@email.com"))
    add_user(create_user("Ana Gómez", "ana.gomez@email.com"))

    print("Current users:")
    for user in get_all_users():
        print(user)


if __name__ == "__main__":
    run_app()