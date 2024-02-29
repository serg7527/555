import psutil



def get_mem():

    mem = psutil.virtual_memory()

    mem_str = mem[0] //1024 ** 3
    print('Total ..................', mem_str, 'Gb \n')

    mem_oper = mem[1] //1024 ** 3
    print('Available ..............', mem_oper, 'Gb \n')

    mem_ope = mem[5] //1024 ** 3
    print('Percent .................', mem_ope, 'Gb \n')

    return get_mem

print('/\.......MEMORY USAGE......../\ \n')



def main():
    mem_info = get_mem()

if __name__ == '__main__':
    main()