import psutil

def get_mem():
    mem = psutil.virtual_memory()

    total_mem_gb = mem.total // 1024 ** 3
    print('Total ..................', total_mem_gb, 'Gb \n')

    available_mem_gb = mem.available // 1024 ** 3
    print('Available ..............', available_mem_gb, 'Gb \n')

    percent_mem = mem.percent
    print('Percent ................', percent_mem, '%' '\n')

    return total_mem_gb, available_mem_gb, percent_mem

print('/\-------MEMORY USAGE-------/\ \n')

def main():
    total_mem, available_mem, percent_mem = get_mem()
    # You can use the retrieved memory information here

if __name__ == '__main__':
    main()