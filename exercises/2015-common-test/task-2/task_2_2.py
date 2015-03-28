def valid_cc_num(cc_num):
    summ = 0
    x2 = False

    for i in range(1, len(cc_num) + 1):
        if x2:
            double = int(cc_num[-i]) * 2

            if double >= 10:
                summ += int(str(double)[0]) + int(str(double)[1])
            else:
                summ += double

            x2 = False

        else:
            summ += int(cc_num[-i])

            x2 = True

    return summ % 10 == 0


ind_ID = '4'
issuer_ID = '26569'
# user_ID = ?
check_digit = '3'

user_ID_list = []

for user_ID in range(1000000):  # test only user IDs under 7 digits
    user_ID = str(user_ID).rjust(6, '0')
    cc_num = ind_ID + issuer_ID + user_ID + check_digit

    if valid_cc_num(cc_num):
        user_ID_list.append(user_ID)

    if len(user_ID_list) == 10:
        break

print("{0:^10}|{1:^20}".format("Count", "User ID"))
print('-'*30)
for count, user_ID in enumerate(user_ID_list):
    print("{0:^10}|{1:^20}".format(count+1, user_ID))
