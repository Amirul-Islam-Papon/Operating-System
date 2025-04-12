def scan(requests, head, disk_size=200, direction="right"):
    requests = sorted(requests)
    sequence = []
    total_seek = 0
    current = head

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    if direction == "left":
        for r in reversed(left):
            sequence.append(r)
            total_seek += abs(current - r)
            current = r
        if current != 0:
            total_seek += current
            current = 0
        for r in right:
            sequence.append(r)
            total_seek += abs(current - r)
            current = r
    else:  
        for r in right:
            sequence.append(r)
            total_seek += abs(current - r)
            current = r
        if current != disk_size - 1:
            total_seek += abs(current - (disk_size - 1))
            current = disk_size - 1
        for r in reversed(left):
            sequence.append(r)
            total_seek += abs(current - r)
            current = r

    print("\nSCAN Disk Scheduling (Direction:", direction + ")")
    print("Sequence:", sequence)
    print("Total Seek Time:", total_seek)

requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head = 53

scan(requests, head, direction="right")  
