def sjf_scheduling(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_done = [False] * n

    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n
    start = [0] * n

    while completed < n:
        idx = -1
        shortest = float('inf')
        for i in range(n):
            pid, arrival, burst = processes[i]
            if arrival <= current_time and not is_done[i]:
                if burst < shortest:
                    shortest = burst
                    idx = i

        if idx == -1:
            current_time += 1  
        else:
            pid, arrival, burst = processes[idx]
            start[idx] = current_time
            completion[idx] = current_time + burst
            turnaround[idx] = completion[idx] - arrival
            waiting[idx] = turnaround[idx] - burst
            current_time = completion[idx]
            is_done[idx] = True
            completed += 1

    print("PID\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for i in range(n):
        pid, arrival, burst = processes[i]
        print(f"{pid}\t{arrival}\t{burst}\t{start[i]}\t{completion[i]}\t\t{waiting[i]}\t{turnaround[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround)/n:.2f}")

process_list = [(1, 2, 4), (2, 10, 1), (3, 3, 2), (4, 2, 5), (5, 0, 5)]
sjf_scheduling(process_list)
