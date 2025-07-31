def format_greeting(name: str) -> str:
    """Creates a greeting string."""
    return f"Hello, {name}!"


def test_greeting_with_name():
    """Tests the function with a standard name."""
    assert format_greeting("World") == "Hello, World!"


def test_greeting_with_empty_string():
    """Tests the function with an empty string."""
    assert format_greeting("") == "Hello, !"