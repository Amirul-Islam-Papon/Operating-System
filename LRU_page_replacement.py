from collections import OrderedDict

def lru_page_replacement(pages, capacity):
    memory = OrderedDict()
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.popitem(last=False) 
        else:
            memory.move_to_end(page) 

        memory[page] = True  
        print(f"Page: {page} -> Memory: {list(memory.keys())}")

    print(f"\nTotal Page Faults: {page_faults}")
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4]
capacity = 3
lru_page_replacement(pages, capacity)
