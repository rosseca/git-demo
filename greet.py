def greet(name, greeting="Hello"):
    """Return a greeting for the given name.

    Args:
        name: The person to greet.
        greeting: The salutation to use (default "Hello").
    """
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))
