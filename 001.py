import psutil

def get_cpu():
    return psutil.cpu_times_percent(interval=None)

def get_mem():
    return psutil.virtual_memory()

def get_disk():
    return psutil.disk_usage('/')

def show_cpu(data):
    print("CPU Information:")
    cpu_percentages = data
    for i, cpu in enumerate(cpu_percentages):
        print(f"CPU Core {i + 1} Usage: {cpu}%")


def show_cpu(data):
    print("CPU Information:")
    # Display the CPU information from the 'data' variable
    pass

def show_mem(data):
    print("Memory Information:")
    # Display the memory information from the 'data' variable
    pass

def show_disk(data):
    print("Disk Information:")
    # Display the disk information from the 'data' variable
    pass

def show(cpu, mem, disk):
    show_cpu(cpu)
    show_mem(mem)
    show_disk(disk)

def main():
    cpu_info = get_cpu()
    mem_info = get_mem()
    disk_info = get_disk()
    show(cpu_info, mem_info, disk_info)

if __name__ == '__main__':
    main()