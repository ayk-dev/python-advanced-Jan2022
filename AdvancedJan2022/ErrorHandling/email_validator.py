class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ['.com', '.bg', '.org', '.net', '.co.uk']


def is_domain_valid(d, valid_domains):
    for domain in valid_domains:
        if d.endswith(domain):
            return True
    return False


email_to_validate = input()

while email_to_validate != 'End':

    if '@' not in email_to_validate:
        raise MustContainAtSymbolError("Email must contain @")

    name = email_to_validate.split('@')[0]
    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email_to_validate.split('@')[1]
    if not is_domain_valid(domain, VALID_DOMAINS):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")

    print('Email is valid')
    email_to_validate = input()