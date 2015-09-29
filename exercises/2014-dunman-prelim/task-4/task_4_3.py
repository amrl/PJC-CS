from task_4_2 import expand_ipv6


def hexa_to_dec(hexa):
    hexa = hexa[::-1]
    dec = 0
    hexa_d = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    power = 0
    for digit in hexa:
        if digit.isalpha():
            dec += hexa_d[digit.upper()] * 16**power
        else:
            dec += int(digit) * 16**power
        power += 1

    return dec


def ipv6_hex2dec(short_ipv6):
    if "::" in short_ipv6:
        short_ipv6 = expand_ipv6(short_ipv6)

    groups = short_ipv6.split(':')
    parsed_groups = list()
    for group in groups:
        if group != "":
            parsed_groups.append(group)

    if len(parsed_groups) == 1:
        return str(hexa_to_dec(parsed_groups[0]))
    else:
        mid = len(parsed_groups) // 2
        return ipv6_hex2dec(':'.join(parsed_groups[:mid])) + ":" + ipv6_hex2dec(':'.join(parsed_groups[mid:]))


# print(ipv6_hex2dec("2001:db8::ff00:42:8329"))
