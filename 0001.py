

# def get_cpu():
#     cpu_info = {}
#     cpu_info["physical_cores"] = psutil.cpu_count(logical=False)
#     cpu_info["logical_cores"] = psutil.cpu_count()
#     cpu_info["cpu_percent"] = psutil.cpu_percent()
#     cpu_info["cpu_freq"] = psutil.cpu_freq()
#     return cpu_info



# def show(cpu, mem, disk):
#     print("CPU Information:")
#     print("Physical Cores:", cpu["physical_cores"])
#     print("Logical Cores:", cpu["logical_cores"])
#     print("CPU Usage:", cpu["cpu_percent"], "%")
#     print("CPU Frequency:", cpu["cpu_freq"])

#     print("\nMemory Information:")
#     print("Total Memory:", mem["total"], "GB")
#     print("Available Memory:", mem["available"], "GB")
#     print("Used Memory:", mem["used"], "GB")

#     print("\nDisk Information:")
#     print("Total Disk Space:", disk["total"], "GB")
#     print("Available Disk Space:", disk["available"], "GB")
#     print("Used Disk Space:", disk["used"], "GB")





# def show_cpu(data):
#     print("CPU Information:")
#     cpu_percentages = data
#     for i, cpu in enumerate(cpu_percentages):
#         print(f"CPU Core {i + 1} Usage: {cpu}%")

import psutil

psutil.cpu_times()