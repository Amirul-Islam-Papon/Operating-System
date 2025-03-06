def calculate_sjf():
    n = len(process_data)
    
    current_time = 0
    completed = []
    execution_order = []
    available = []
    
    while len(completed) < n:
        # Add newly arrived processes
        for process in process_data:
            if process[1] <= current_time and process not in completed and process not in available:
                available.append(process)
        
        if available:
            available.sort(key=lambda x: (x[2]))  # Sort by burst time
            current_process = available.pop(0)
            execution_order.append(current_process[0])
            current_time += current_process[2]
            completed.append(current_process)
        else:
            current_time += 1             # If no process is available, increment time
    
    # Calculate Completion, Turnaround, and Waiting times
    completion_times = {}
    waiting_times = {}
    turnaround_times = {}
    
    current_time = 0
    for process in execution_order:
        for p, at, bt in process_data:
            if p == process:
                if current_time < at:
                    current_time = at
                completion_times[p] = current_time + bt
                turnaround_times[p] = completion_times[p] - at
                waiting_times[p] = turnaround_times[p] - bt
                current_time = completion_times[p]
                break
    
    # Print results
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for p, at, bt in process_data:
        print(f"{p}\t\t{at}\t\t{bt}\t\t{completion_times[p]}\t\t\t{turnaround_times[p]}\t\t{waiting_times[p]}")

# Input data
process_data = [
    ('P1', 2, 6),
    ('P2', 5, 2),
    ('P3', 1, 8),
    ('P4', 0, 3),
    ('P5', 4, 4)
]

calculate_sjf()
