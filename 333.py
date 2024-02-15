def show_cpu(data):
    print("CPU Information:")
    cpu_percentage = psutil.cpu_percent(interval=None)
    print(f"Overall CPU Usage: {cpu_percentage}%")
    cpu_percentages = data
    for i, cpu in enumerate(cpu_percentages):
        print(f"CPU Core {i + 1} Usage: {cpu}%")

def show_mem(data):
    print("Memory Information:")
    print(f"Total Memory: {data.total} bytes")
    print(f"Available Memory: {data.available} bytes")
    print(f"Used Memory: {data.used} bytes")
    print(f"Memory Percentage: {data.percent}%")

def show_disk(data):
    print("Disk Information:")
    print(f"Total Disk Space: {data.total} bytes")
    print(f"Used Disk Space: {data.used} bytes")
    print(f"Free Disk Space: {data.free} bytes")
    print(f"Disk Usage Percentage: {data.percent}%")