def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return ("frizz_buzz")
    elif number % 3 == 0:
        return ("fizz")
    elif number % 5 == 0:
        return ("buzz")


print(fizz_buzz(5))
