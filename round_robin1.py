from collections import deque

def round_robin(processes, time_quantum):
    n = len(processes)
    queue = deque()
    time = 0
    completed = 0
    result = []
    
    remaining_bt = {p['pid']: p['bt'] for p in processes}
    at_map = {p['pid']: p['at'] for p in processes}
    processes.sort(key=lambda x: x['at'])  
    arrived = set()
    execution_order = []

    while completed < n:
        for p in processes:
            if p['at'] <= time and p['pid'] not in arrived and p['pid'] not in queue:
                queue.append(p['pid'])
                arrived.add(p['pid'])

        if not queue:
            time += 1
            continue

        current = queue.popleft()
        execution_order.append((current, time))

        exec_time = min(time_quantum, remaining_bt[current])
        time += exec_time
        remaining_bt[current] -= exec_time

        for p in processes:
            if p['at'] <= time and p['pid'] not in arrived and p['pid'] not in queue:
                queue.append(p['pid'])
                arrived.add(p['pid'])

        if remaining_bt[current] > 0:
            queue.append(current)
        else:
            completed += 1
            ct = time
            bt = next(p['bt'] for p in processes if p['pid'] == current)
            at = at_map[current]
            tat = ct - at
            wt = tat - bt
            result.append({
                'pid': current,
                'CT': ct,
                'TAT': tat,
                'WT': wt
            })

    return execution_order, result

process_list = [
    {'pid': 'P1', 'at': 0, 'bt': 7},
    {'pid': 'P2', 'at': 1, 'bt': 4},
    {'pid': 'P3', 'at': 2, 'bt': 15},
    {'pid': 'P4', 'at': 3, 'bt': 11},
    {'pid': 'P5', 'at': 4, 'bt': 20},
    {'pid': 'P6', 'at': 4, 'bt': 9}
]

quantum = 5
exec_order, results = round_robin(process_list, quantum)

print("Execution Queue (Process @ Time):")
for p, t in exec_order:
    print(f"{p} @ {t}")

print("\nFinal Table:")
print(f"{'PID':<5} {'CT':<5} {'TAT':<5} {'WT':<5}")
for r in results:
    print(f"{r['pid']:<5} {r['CT']:<5} {r['TAT']:<5} {r['WT']:<5}")
