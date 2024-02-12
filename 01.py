import psutil

def get_cpu():
    
    return{}

def get_mem():
    
    return{}

def get_disk():
    
    return{}

def show_cpu(data):
    return{}

def show_mem(data):
    return{}

def show_disk(data):
    return{}

def show(cpu, mem, disk):
    show_cpu(cpu)
    show_mem(mem)
    show_disk(disk)
    return{}

def main():
    cpu_info = get_cpu()
    mem_info = get_mem()
    disk_info = get_disk()
    show(cpu = get_cpu, mem=get_mem, disk=get_disk)
  

if __name__ == '__main__':
    main()
