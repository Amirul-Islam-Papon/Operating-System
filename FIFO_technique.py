def fifo_page_replacement_simulation(pages, frame_size):
    memory = []
    hits = 0
    misses = 0

    print(f"{'Step':<5} {'Page':<6} {'Memory':<25} {'Result'}")

    for i, page in enumerate(pages, start=1):
        if page in memory:
            hits += 1
            result = "Hit"
        else:
            misses += 1
            result = "Miss"
            if len(memory) < frame_size:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        
        mem_display = "[" + ", ".join(str(p) for p in memory) + "]"
        print(f"{i:<5} {page:<6} {mem_display:<25} {result}")

    print(f"Total Page Hits: {hits}")
    print(f"Total Page Misses: {misses}")


page_reference = [0, 1, 5, 3, 5, 0, 2, 4, 7, 9, 0, 0, 3]
frame_size = 4

fifo_page_replacement_simulation(page_reference, frame_size)
