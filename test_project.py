import pytest
from project import validate_name, validate_amount, existing_user


def test_validate_name():
    assert validate_name("robert lewandowski") == "Robert Lewandowski"
    assert validate_name("robert", "first") == "Robert"
    assert validate_name("lewandowski", "last") == "Lewandowski"

    # Testing for ValueError scenario
    with pytest.raises(ValueError):
        validate_name("", "first")

    with pytest.raises(ValueError):
        validate_name("     ", "last")


def test_validate_amount():
    assert validate_amount('350') == 350
    assert validate_amount('3,500') == 3500

    # Test for invalid inputs
    assert validate_amount('-5') == None

    with pytest.raises(AttributeError):
        validate_amount(5)


def test_existing_user():
    # Creating a dummy data
    existing_user_data = {
        "_username": "lone",
        "_first": "John Daniel",
        "_last": "Garan",
        "_monthly_budget": 3500,
        "_expenses": {},
        "_remaining_balance": 3150,
        "date": "2023-08-16",
        "last_updated": 8
    }

    # Retrieve the existing user's information to facilitate signing in and prevent registration
    user = existing_user(existing_user_data)

    # Perfoming the assertions to validate the created user
    assert user.username == "lone"
    assert user.first == "John Daniel"
    assert user.last == "Garan"
    assert user.monthly_budget == 3500
    assert user.remaining_balance == 3150
    assert user.expenses == {}
