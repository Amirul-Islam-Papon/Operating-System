def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  
    
    n = len(processes)
    tat = [0] * n
    wt = [0] * n
    ct = [0] * n

    ct[0] = processes[0][1] + processes[0][2]  
    for i in range(1, n):
        ct[i] = max(ct[i-1], processes[i][1]) + processes[i][2]
    
    for i in range(n):
        tat[i] = ct[i] - processes[i][1]
        wt[i] = tat[i] - processes[i][2]
    
    print("Process\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{tat[i]}\t{wt[i]}")
    

process_list = [
    ('P1', 2, 5),
    ('P2', 0, 3),
    ('P3', 4, 4),
]

fcfs_scheduling(process_list)