def age_assignment(*args, **kwargs):
    name_and_age = {}
    for name in args:
        age = kwargs[name[0]]
        name_and_age[name] = age
    return name_and_age


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))