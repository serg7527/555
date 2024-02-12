from __future__ import print_function

import sys

import psutil


def main():
    if not hasattr(psutil, "sensors_fans"):
        return sys.exit("platform not supported")
    fans = psutil.sensors_fans()
    if not fans:
        print("no fans detected")
        return
    for name, entries in fans.items():
        print(name)
        for entry in entries:
            print("    %-20s %s RPM" % (entry.label or name, entry.current))
        print()


if __name__ == '__main__':
    main()