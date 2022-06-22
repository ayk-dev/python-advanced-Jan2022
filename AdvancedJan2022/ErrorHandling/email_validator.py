class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ['.com', '.bg', '.org', '.net']

email_to_validate = input()

while email_to_validate != 'End':

    if '@' not in email_to_validate:
        raise MustContainAtSymbolError("Email must contain @")

    name = email_to_validate.split('@')[0]
    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email_to_validate.split('.')[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
    email_to_validate = input()