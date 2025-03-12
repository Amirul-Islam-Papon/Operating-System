def fcfs_disk_scheduling(requests, head):
    total_seek_time = 0
    sequence = [head]  
    
    for request in requests:
        seek_distance = abs(request - head)
        total_seek_time += seek_distance
        head = request
        sequence.append(head)
    
    return total_seek_time, sequence

requests = [60, 100, 30, 150, 20]
initial_head = 50  

seek_time, movement_sequence = fcfs_disk_scheduling(requests, initial_head)

print(f"Total Seek Time: {seek_time}")
print(f"Head Movement Sequence: {' -> '.join(map(str, movement_sequence))}")