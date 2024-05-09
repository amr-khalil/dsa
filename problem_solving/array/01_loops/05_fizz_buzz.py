
def fizz_buzz(num):
    """Return 'Fizz' if num is divisible by 3,
    'Buzz' if num is divisible by 5,
    'FizzBuzz' if num is divisible by both 3 and 5,
    or num itself otherwise.
    """
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        


if __name__ == "__main__":
    fizz_buzz(15)