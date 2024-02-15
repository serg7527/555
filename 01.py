import psutil

def get_user():
    p = psutil.users()
    terminal = '!!'.join('{}' for _ in p).format(*p)
    print(terminal)

cpu = psutil.cpu_freq(percpu=False)

print(cpu, '\n')

# def get_disk():
#     psutil.disk_usage('/')
#     sdiskusage = disk_info
#     return("total", "used', "free", "percent")
#         ...

# def show_mem(data):
#     return{}

# def show_disk(data):
#     return{}

# def show(user, cpu, mem, disk):
#     show_user(user)
#     show_cpu(cpu)
#     show_mem(mem)
#     show_disk(disk)

#     return{}

# def main():
#     cpu_info = get_cpu()
#     mem_info = get_mem()
#     disk_info = get_disk()
#     show(cpu = get_cpu, mem=get_mem, disk=get_disk)
  

# if __name__ == '__main__':
# main()  
