def find_sum_positives(*args):
    result = 0
    for num in args:
        if num > 0:
            result += num
    return result


def find_sum_negatives(*args):
    result = 0
    for num in args:
        if num < 0:
            result += num
    return result


def find_the_stronger(*args):
    negatives = find_sum_negatives(*args)
    positives = find_sum_positives(*args)

    result = ''
    if positives > abs(negatives):
        result = 'The positives are stronger than the negatives'
    else:
        result = 'The negatives are stronger than the positives'
    return result


numbers = [int(x) for x in input().split()]

print(find_sum_negatives(*numbers))
print(find_sum_positives(*numbers))
print(find_the_stronger(*numbers))
