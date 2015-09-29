from task_1_1 import get_chip_time, get_run_time


def main():
    # list of tuples, i.e. [(runner, run time, formatted run time)]
    runtimes = list()

    infile = open("RACE.txt", "r")
    for line in infile:
        runner, start, end = line[:5], line[5:13], line[13:-1]
        time = get_run_time(start, end)
        formatted_time = get_chip_time(start, end)
        runtimes.append((runner, time, formatted_time))
    infile.close()

    # sort by ascending order of run times
    for i in range(len(runtimes)-1):
        for j in range(len(runtimes)-1-i):
            if runtimes[j][1] > runtimes[j+1][1]:
                runtimes[j], runtimes[j+1] = runtimes[j+1], runtimes[j]

    # get the runners with the top 3 fastest times
    top_runners = list()
    prev_time = runtimes[0][1]
    rank = 1
    for runner in runtimes:
        if rank <= 3:
            runner_id, run_time, formatted_time = runner
            if run_time == prev_time:
                top_runners.append((rank, runner_id, formatted_time))
            else:
                rank += 1
                if rank <= 3:
                    top_runners.append((rank, runner_id, formatted_time))
                prev_time = run_time
        else:
            break

    for runner in top_runners:
        rank, runner_id, time = runner
        print("{0}. {1}    Chip time: {2}".format(rank, runner_id, time))


# main()
