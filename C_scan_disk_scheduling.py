def c_scan(requests, head, disk_size=200):
    requests = sorted(requests)
    sequence = []
    total_seek = 0
    current = head

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    for r in right:
        sequence.append(r)
        total_seek += abs(current - r)
        current = r

    if current != disk_size - 1:
        total_seek += abs(current - (disk_size - 1))
        current = 0
        total_seek += disk_size - 1

    for r in left:
        sequence.append(r)
        total_seek += abs(current - r)
        current = r

    print("\nC-SCAN Disk Scheduling:")
    print("Sequence:", sequence)
    print("Total Seek Time:", total_seek)

requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head = 53

c_scan(requests, head)
