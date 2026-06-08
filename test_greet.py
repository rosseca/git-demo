from greet import greet


def test_default_greeting():
    assert greet("World") == "Hello, World!"


def test_custom_greeting():
    assert greet("Vlad", greeting="Hi") == "Hi, Vlad!"
