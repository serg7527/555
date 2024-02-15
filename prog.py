import psutil
from psutil._common import bytes2human

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
    virt = psutil.virtual_memory()
    swap = psutil.swap_memory()
    templ = "%-7s %10s %10s %10s %10s %10s %10s"
    print(templ % ('', 'total', 'used', 'free', 'shared', 'buffers', 'cache'))
    sect = templ % (
        'Mem:',
        int(virt.total / 1024),
        int(virt.used / 1024),
        int(virt.free / 1024),
        int(getattr(virt, 'shared', 0) / 1024),
        int(getattr(virt, 'buffers', 0) / 1024),
        int(getattr(virt, 'cached', 0) / 1024),
    )
    print(sect)
    sect = templ % (
        'Swap:',
        int(swap.total / 1024),
        int(swap.used / 1024),
        int(swap.free / 1024),
        '',
        '',
        '',
    )
    print(sect)


if __name__ == '__main__':
    main()


cpu = psutil.cpu_freq(percpu=False)
print(cpu, '\n')

cpu_tim = psutil.cpu_times_percent(interval=3, percpu=False)
print(cpu_tim, '\n')

cpu_per = psutil.cpu_percent(interval=3, percpu=True)
print(cpu_per, '\n')