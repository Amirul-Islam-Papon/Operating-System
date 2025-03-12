class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling_preemptive_time_quantum(processes, time_quantum=2):
    time = 0
    completed = 0
    n = len(processes)
    queue = []  
    sequence = []
    
    while completed < n:
        for p in processes:
            if p.arrival_time == time and p not in queue and p.remaining_time > 0:
                queue.append(p)
                queue.sort(key=lambda x: (-x.priority, x.arrival_time)) 
        
        if queue:
            current_process = queue.pop(0)
            sequence.append((time, current_process.pid))
            
            execution_time = min(time_quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            time += execution_time
            
            for p in processes:
                if time_quantum > 1 and p.arrival_time in range(time - execution_time + 1, time + 1) and p not in queue and p.remaining_time > 0:
                    queue.append(p)
                    queue.sort(key=lambda x: (-x.priority, x.arrival_time))
            
            if current_process.remaining_time > 0:
                queue.append(current_process)
                queue.sort(key=lambda x: (-x.priority, x.arrival_time))
            else:
                current_process.completion_time = time
                completed += 1
        else:
            time += 1
    
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
    
    return processes, sequence

process_data = [
    (1, 0, 5, 10),
    (2, 1, 4, 20),
    (3, 3, 2, 30),
    (4, 4, 1, 40)
]

processes = [Process(pid, at, bt, pr) for pid, at, bt, pr in process_data]

scheduled_processes, sequence = priority_scheduling_preemptive_time_quantum(processes, time_quantum=2)

sequence_output = "Sequence: " + " -> ".join([f"P{pid}" for t, pid in sequence])
print(sequence_output)

print("\nPID | AT | BT | Priority | CT  | TAT | WT")
for p in scheduled_processes:
    print(f"{p.pid:3} | {p.arrival_time:2} | {p.burst_time:2} | {p.priority:8} | {p.completion_time:2} | {p.turnaround_time:3} | {p.waiting_time:2}")

