# WARNING: This code is sufficient for most but not all test cases.
# e.g. incorrect result given for INPUT3.txt

# NOTE: we will always have stamps with a value of 1

# get stamp data from file
infile = open("INPUT1.txt", 'r')
n, m = infile.readline()[:-1].split()
values = reversed(infile.readline()[:-1].split())
n, m, values = int(n), int(m), [int(i) for i in values]
infile.close()

# int:n => no. of stamp values we have
# int:m => max no. of stamps we can use at once (limit)
# list:values => array of stamp values available, ascending order

next_result = 1   # results we want (1, 2, 3, ...)
have_more = True  # we still have another combination to try

while have_more:
    # if one of our stamps has the same value as the result we want...
    if next_result in values:
        print("{0} = {0}".format(next_result))
        stamps = [next_result]

    # otherwise, let's +1 and see if we can get the result we want
    else:
        stamps.append(1)  # +1 to our current stamps

        # merge our smaller stamps into bigger stamps, if possible
        for index in range(len(stamps)):
            if sum(stamps[index:]) in values:
                stamps = stamps[:index] + [sum(stamps[index:])]

        # did we manage to merge our stamps and still keep the no. of stamps
        # within the limit?
        if len(stamps) <= m:  # success!
            summation = ' + '.join(str(i) for i in stamps)
            print("{0} = {1}".format(next_result, summation))
        else:
            have_more = False  # not successful... it's the end

    next_result += 1
