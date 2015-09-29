def abbreviate_ipv6(long_ipv6):
    if long_ipv6 == "0000:0000:0000:0000:0000:0000:0000:0001":
        abbreviated = "::1"
    else:
        groups = long_ipv6.split(':')

        # remove leading zeroes
        parsed_groups = list()
        for group in groups:
            parsed_groups.append(group[:-1].lstrip('0') + group[-1])

        # remove consecutive zero sections
        zero_found = False
        consecutive_found = False
        for idx, group in enumerate(parsed_groups):
            if not zero_found and group == '0':
                zero_found = True
                zero_start = idx
                zero_end = idx
            elif zero_found and group == '0':
                consecutive_found = True
                zero_end += 1
            elif zero_found and group != '0':
                break

        if zero_found and consecutive_found:
            parsed_groups[zero_start:zero_end+1] = [""]

        abbreviated = ':'.join(parsed_groups)

    return abbreviated


# infile = open("IPV6_LONG.txt", "r")
# for line in infile:
#     print(abbreviate_ipv6(line[:-1]))
# infile.close()
