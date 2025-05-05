def round_robin(processes, time_quantum):
    queue = []  
    time = 0 
    result = []
    remaining_bt = {p[0]: p[2] for p in processes}  
    arrival_times = {p[0]: p[1] for p in processes} 
    completion_time = {}  
    turn_around_time = {} 
    waiting_time = {}  
    processes.sort(key=lambda x: x[1])  
    
    i = 0
    while i < len(processes) and processes[i][1] <= time:
        queue.append(processes[i][0])
        i += 1
    
    while queue:
        process = queue.pop(0)  
        if remaining_bt[process] > time_quantum:
            result.append((process, time, time + time_quantum))
            time += time_quantum
            remaining_bt[process] -= time_quantum
        else:
            result.append((process, time, time + remaining_bt[process]))
            time += remaining_bt[process]
            completion_time[process] = time
            remaining_bt[process] = 0
        
        while i < len(processes) and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1
        
        if remaining_bt[process] > 0:
            queue.append(process)
    
    for process, arrival, burst in processes:
        turn_around_time[process] = completion_time[process] - arrival
        waiting_time[process] = turn_around_time[process] - burst
    
    print("Process  Arrival Time  Burst Time  Completion Time  Turn Around Time  Waiting Time")
    for process, arrival, burst in processes:
        print(f"{process}\t\t\t{arrival}\t\t\t{burst}\t\t\t{completion_time[process]}\t\t\t\t{turn_around_time[process]}\t\t\t\t\t{waiting_time[process]}")
    
    print("Sequence:", result)

process_data = [
    ('P1', 0, 7),
    ('P2', 1, 4),
    ('P3', 2, 15),
    ('P4', 3, 11),
    ('P4', 4, 20),
    ('P4', 4, 9),

]
time_quantum = 5

round_robin(process_data, time_quantum)