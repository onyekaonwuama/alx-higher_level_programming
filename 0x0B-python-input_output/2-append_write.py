
#!/usr/bin/python3

"""Defines a file-writing function."""


def append_write(filename="", text=""):
    """to append a string to a UTF8 text file.
    Args:
        filename (str): Name of the file to append.
        text (str): The text to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
