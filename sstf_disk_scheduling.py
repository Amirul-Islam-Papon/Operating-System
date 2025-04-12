def sstf(requests, head):
    requests = requests[:]
    sequence = []
    total_seek = 0
    current = head

    while requests:
        closest = min(requests, key=lambda x: abs(x - current))
        sequence.append(closest)
        total_seek += abs(current - closest)
        current = closest
        requests.remove(closest)

    print("SSTF Disk Scheduling:")
    print("Sequence:", [head] + sequence)
    print("Total Seek Time:", total_seek)

requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head = 53

sstf(requests, head)
