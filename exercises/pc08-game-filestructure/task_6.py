from task_4 import HashKey
from task_5 import HandleCollision

# converting sequential MASTER.DAT to random access FASTER.DAT

master = open("MASTER.DAT", 'r')
raf = open("FASTER.DAT", 'w+')

for record in master:
    # generate address for record
    username = record[:15].rstrip()
    address = HashKey(username)

    raf.seek((address-1) * 57)
    if raf.read(1).isalpha():  # collision detected at address
        HandleCollision(record[:-1], raf)
    else:
        raf.seek((address-1) * 57)
        raf.write(record[:-1])

master.close()
raf.close()
