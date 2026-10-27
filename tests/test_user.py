import pytest
from models.User import User


@pytest.fixture(autouse=True)
def reset_users():
    """Reset shared class data before each test."""
    User._users_list.clear()
    User._next_id = 1000


def test_user_initialization():
    user = User("Hope", "hope@email.com")
    assert user.name == "Hope"
    assert user.email == "hope@email.com"
    assert user.projects == []


def test_add_project():
    user = User("Hope", "hope@email.com")
    user.add_projects("Project A")
    assert user.projects == ["Project A"]


def test_add_duplicate_project():
    user = User("Hope", "hope@email.com")
    user.add_projects("Project A")
    user.add_projects("Project A")

    assert user.projects == ["Project A"]


def test_add_multiple_projects():
    user = User("Hope", "hope@email.com")
    user.add_projects("Project A")
    user.add_projects("Project B")
    assert user.projects == ["Project A", "Project B"]


def test_add_user_to_list():
    user = User("Hope", "hope@email.com")
    user.add_user_to_list(user)
    assert "Hope" in User._users_list
    assert User._users_list["Hope"] is user


def test_add_duplicate_user_name():
    first_user = User("Hope", "hope@email.com")
    second_user = User("Hope", "hope2@email.com")
    first_user.add_user_to_list(first_user)
    second_user.add_user_to_list(second_user)

    assert len(User._users_list) == 1
    assert User._users_list["Hope"] is first_user


def test_to_dict():
    user = User("Hope", "hope@email.com")
    user.add_projects("Project A")
    result = user.to_dict()

    assert result == {
        "name": "Hope",
        "email": "hope@email.com",
        "projects": ["Project A"]
    }


def test_create_user():
    user = User.create_user("Hope", "hope@email.com")

    assert isinstance(user, User)
    assert user.name == "Hope"
    assert user.email == "hope@email.com"
    assert user.projects == []
    assert User._users_list["Hope"] is user


def test_create_user_does_not_replace_existing_user():
    first_user = User.create_user("Hope", "hope@email.com")
    second_user = User.create_user("Hope", "hope2@email.com")

    assert User._users_list["Hope"] is first_user
    assert second_user.email == "hope2@email.com"


def test_repr():
    user = User("Hope", "hope@email.com")

    assert repr(user) == "User('Hope', 'hope@email.com')"
