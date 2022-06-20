def sorting_cheeses(**kwargs):
    result = ''
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    for cheese, values in sorted_cheeses:
        result += cheese + '\n'
        for v in sorted(values, reverse=True):
            result += str(v) + '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)



