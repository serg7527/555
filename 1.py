from __future__ import print_function
import sys
import psutil
from psutil._common import bytes2human
import os



def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def main():
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
    else:
        temps = {}
    fans = psutil.sensors_fans() if hasattr(psutil, "sensors_fans") else {}
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
    else:
        battery = None

    if not any((temps, fans, battery)):
        print("can't read any temperature, fans or battery info")
        return

    names = set(list(temps.keys()) + list(fans.keys()))
    for name in names:
        print(name)
        # Temperatures.
        if name in temps:
            print("\nTemperatures:\n-------------------------------------------------------------------")
            for entry in temps[name]:
                s = " %-20s %s °C (high = %s °C, critical = %s °C)" % (
                    entry.label or name,
                    entry.current,
                    entry.high,
                    entry.critical,
                )
                print(s)
        # Fans.
        if name in fans:
            print("    Fans:")
            for entry in fans[name]:
                print(
                    "        %-20s %s RPM"
                    % (entry.label or name, entry.current)
                )

    # Battery.
    if battery:
        print("\nBattery:\n-------------------------------------------------------------------")
        print(" charge:              %s%%" % round(battery.percent, 2))
        if battery.power_plugged:
            print(
                " status:     %s"
                % ("         charging" if battery.percent < 100 else "         fully charged")
            )
            print(" plugged in:          yes")
        else:
            print(" left:                %s"% secs2hours(battery.secsleft))
            print(" status:           %s"% "   discharging")
            print(" plugged in:          no")


if __name__ == '__main__':
    main()




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


if __name__ == '__main__':
    main()



def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("\nDevice", "Total", "Used", "Free", "Use ", "Type", "Mount\n"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or not part.fstype:
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        line = templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint,
        )
        print(line)





def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("\nDevice", "Total", "Used", "Free", "Use ", "Type", "Mount\n"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or not part.fstype:
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        line = templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint,
        )
        print(line)


if __name__ == '__main__':
    sys.exit(main())




psutil.cpu_freq()
psutil.cpu_freq(percpu=True)