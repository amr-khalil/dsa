
def capitalize(string):
    """
    a lazy fox -> A Lazy Fox
    """
    words = string.split()
    words = [word.capitalize() for word in words]
    return " ".join(words)


if __name__ == "__main__":
    print(capitalize("a lazy fox"))