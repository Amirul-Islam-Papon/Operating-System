def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    index = 0  
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % capacity
            page_faults += 1
        print(f"Page: {page} -> Memory: {memory}")

    print(f"\nTotal Page Faults: {page_faults}")
    return page_faults

pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
fifo_page_replacement(pages, capacity)
