class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative("Number must be greater than or equal to zero")