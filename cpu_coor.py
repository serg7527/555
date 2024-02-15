from __future__ import print_function
import collections
import os
import sys
import time
import psutil
from psutil._compat import get_terminal_size


if not hasattr(psutil.Process, "cpu_num"):
    sys.exit("platform not supported")


def clean_screen():
    if psutil.POSIX:
        os.system('clear')
    else:
        os.system('cls')


def main():
    num_cpus = psutil.cpu_count()
    if num_cpus > 8:
        num_cpus = 8  # try to fit into screen
        cpus_hidden = True
    else:
        cpus_hidden = False

    while True:
        # header
        clean_screen()
        cpus_percent = psutil.cpu_percent(percpu=True)
        for i in range(num_cpus):
            print("CPU %-6i" % i, end="")
        if cpus_hidden:
            print(" (+ hidden)", end="")

        print()
        for _ in range(num_cpus):
            print("%-10s" % cpus_percent.pop(0), end="")
        print()

        # processes
        procs = collections.defaultdict(list)
        for p in psutil.process_iter(['name', 'cpu_num']):
            procs[p.info['cpu_num']].append(p.info['name'][:5])

        curr_line = 3
        while True:
            for num in range(num_cpus):
                try:
                    pname = procs[num].pop()
                except IndexError:
                    pname = ""
                print("%-10s" % pname[:10], end="")
            print()
            curr_line += 1
            if curr_line >= get_terminal_size()[1]:
                break

        time.sleep(1)


if __name__ == '__main__':
    main()