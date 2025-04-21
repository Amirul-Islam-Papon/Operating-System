def sstf_disk_scheduling(requests, head):
    sequence = [head] 
    total_movement = 0
    pending = requests.copy()
    current = head

    while pending:
        next_request = min(pending, key=lambda x: abs(x - current))
        movement = abs(current - next_request)
        total_movement += movement
        sequence.append(next_request)
        current = next_request
        pending.remove(next_request)

    return sequence, total_movement

requests = [137, 240, 179, 75, 118, 29, 15, 51]
head = 55

order, total = sstf_disk_scheduling(requests, head)

print("Order of execution:", " -> ".join(map(str, order)))
print("Total head movement:", total)
