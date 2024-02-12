from __future__ import print_function

import sys

from psutil._common import bytes2human

import psutil

# BATTERY

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def main():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    print("Charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print(
            "Status:     %s"
            % ("charging" if batt.percent < 100 else "fully charged")
        )
        print("Plugged in: yes")
    else:
        print("left:       %s" % secs2hours(batt.secsleft))
        print("Status:     %s" % "discharging")
        print("Plugged in: no")


if __name__ == '__main__':
    main()


# MEMORY

def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))




def main():
    print('\nMEMORY\n--------------------')
    pprint_ntuple(psutil.virtual_memory())
    print('\nSWAP\n--------------------')
    pprint_ntuple(psutil.swap_memory())




# TEMPERATURES

def main():
    if not hasattr(psutil, "sensors_temperatures"):
        sys.exit("platform not supported")
    temps = psutil.sensors_temperatures()
    if not temps:
        sys.exit("can't read any temperature")
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            line = "    %-15s %5s  °C  (high = %s  °C,  critical = %s  °C)" % (
                entry.label or name,
                entry.current,
                entry.high,
                entry.critical,
            )
            print(line)
        print('\n')


if __name__ == '__main__':
    main()