import psutil


def get_cpu():
    print('/\---------CPU USAGE----------/\ \n')
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    for el in range(len(cpu)):
        print(f'CPU core - {el} :...........> {cpu[el]} % \n')


def get_mem():
    print('/\-------MEMORY USAGE-------/\ \n')
    mem = psutil.virtual_memory()
    mem_str = mem[0] /1024 ** 3
    mem_oper = mem[1] /1024 ** 3
    mem_ope = mem[5] /1024 ** 3
    print('Total =', mem_str, 'Gb \n')
    print('Available =', mem_oper, 'Gb \n')
    print('Percent =', mem_ope, 'Gb \n')


def get_disk():
    disk = psutil.disk_usage('/')
    disk_total = disk[0] /1024 ** 3
    disk_used = disk[1] /1024 ** 3
    disk_free = disk[2] /1024 ** 3
    disk_percent = disk[3] /1024

    print('/\-------DISK USAGE--------/\ \n')
    print('Total = ', disk_total, 'Gb \n')
    print('Used =', disk_used, 'Gb \n')
    print('Free =', disk_free, 'Gb \n')
    print('Percent =', disk_percent,'Gb')


def main():
    cpu_info = get_cpu()
    mem_info = get_mem()
    disk_info = get_disk()
    #show(cpu_info, mem_info, disk_info)

if __name__ == '__main__':
    main()