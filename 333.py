import psutil

def get_cpu():
    return psutil.cpu_times_percent(interval=None)

def get_mem():
    return psutil.virtual_memory()

def get_disk():
    return psutil.disk_usage('/')

if __name__ == '__main__':

main()