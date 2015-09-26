def Valid_Email(email):
    """Check validity of an email string, trying to be as primitive as
    possible, trying to forget what Python can actually do.
    """

    # Validity tests
    # 1. Only contains letters, numbers, '@', '.', and '_'
    # 2. Only 1 '@' character
    # 3. Follows the format (local)@(site).(domain)[.(subdomain)]

    # 1.
    length = len(email)
    idx = 0
    valid_test_1 = True

    while idx <= length-1 and valid_test_1:
        valid_test_1 = False
        if ((email[idx] >= '0' and email[idx] <= '9')
            or (email[idx] >= 'a' and email[idx] <= 'z')
                or email[idx] == '@'
                or email[idx] == '.'
                or email[idx] == '_'):
            valid_test_1 = True
        idx = idx + 1

    if not valid_test_1:
        return False

    # 2.
    idx = 0
    at_count = 0
    valid_test_2 = True

    while idx <= length-1 and valid_test_2:
        if email[idx] == '@':
            at_count = at_count + 1
        if at_count > 1:
            valid_test_1 = False
        idx = idx + 1
    if at_count != 1:
        valid_test_2 = False

    if not valid_test_2:
        return False

    # 3.
    idx = 0
    valid_test_3 = True

    if (email[0] == '@' or email[0] == '.'
            or email[length-1] == '@' or email[length-1] == '@'):
        valid_test_3 = False

    prev = '\0'  # check no '.' before and after '@' and no consecutive '.'
    while idx <= length-1 and valid_test_3:
        if idx+1 <= length-1:
            after = email[idx+1]
        else:
            after = '\0'
        current = email[idx]
        if ((current == '@' or current == '.')
                and (prev == '.' or after == '.')):
            valid_test_3 = False
        prev = current
        idx = idx + 1

    if not valid_test_3:
        return False

    return True
