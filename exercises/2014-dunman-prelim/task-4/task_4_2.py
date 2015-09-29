def expand_ipv6(short_ipv6):
    groups = short_ipv6.split(':')

    # restore consecutive zero sections
    if short_ipv6.startswith("::") or short_ipv6.endswith("::"):
        no_of_zero_sections = 10 - len(groups)
    else:
        no_of_zero_sections = 9 - len(groups)

    parsed_groups = list()
    zero_section_found = False
    for group in groups:
        if not zero_section_found and group == "":
            parsed_groups += ["0"]*no_of_zero_sections
            zero_section_found = True
        else:
            if group != "":
                parsed_groups.append(group)

    # restore leading zeroes
    for index, group in enumerate(parsed_groups):
        parsed_groups[index] = group.rjust(4, '0')

    expanded = ':'.join(parsed_groups)

    return expanded


# infile = open("IPV6_SHORT.txt", "r")
# for line in infile:
#     print(expand_ipv6(line[:-1]))
# infile.close()
