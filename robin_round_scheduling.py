def round_robin(processes, time_quantum):
    queue = []  # Ready queue
    time = 0  # Current time
    result = []  # Store execution order
    remaining_bt = {p[0]: p[2] for p in processes}  # Remaining burst time
    arrival_times = {p[0]: p[1] for p in processes}  # Arrival times
    completion_time = {}  # Completion time
    turn_around_time = {}  # Turnaround time
    waiting_time = {}  # Waiting time
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    
    i = 0
    while i < len(processes) and processes[i][1] <= time:
        queue.append(processes[i][0])
        i += 1
    
    while queue:
        process = queue.pop(0)  # Fetch first process in queue
        if remaining_bt[process] > time_quantum:
            result.append((process, time, time + time_quantum))
            time += time_quantum
            remaining_bt[process] -= time_quantum
        else:
            result.append((process, time, time + remaining_bt[process]))
            time += remaining_bt[process]
            completion_time[process] = time
            remaining_bt[process] = 0
        
        # Add new processes that have arrived by now
        while i < len(processes) and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1
        
        # Re-add the process if it's not finished yet
        if remaining_bt[process] > 0:
            queue.append(process)
    
    # Calculate turnaround time and waiting time
    for process, arrival, burst in processes:
        turn_around_time[process] = completion_time[process] - arrival
        waiting_time[process] = turn_around_time[process] - burst
    
    # Print full process table
    print("Process  Arrival Time  Burst Time  Completion Time  Turn Around Time  Waiting Time")
    for process, arrival, burst in processes:
        print(f"{process}\t\t\t{arrival}\t\t\t{burst}\t\t\t{completion_time[process]}\t\t\t\t{turn_around_time[process]}\t\t\t\t\t{waiting_time[process]}")

# Given process data
process_data = [
    ('P1', 0, 5),
    ('P2', 1, 4),
    ('P3', 2, 2),
    ('P4', 4, 1),
]
time_quantum = 2

round_robin(process_data, time_quantum)
