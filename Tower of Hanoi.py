def Tower(n, source, aux, destination):
    if n % 2 == 0:
        for i in range(1, pow(2, n)):
            if i % 3 == 1:
                if len(source) == 0:
                    source.insert(0, aux.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(aux) == 0:
                    aux.insert(0, source.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if source[0] > aux[0]:
                        source.insert(0, aux.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        aux.insert(0, source.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
            elif i % 3 == 2:
                if len(source) == 0:
                    source.insert(0, destination.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(destination) == 0:
                    destination.insert(0, source.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if source[0] > destination[0]:
                        source.insert(0, destination.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        destination.insert(0, source.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
            else:
                if len(aux) == 0:
                    aux.insert(0, destination.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(destination) == 0:
                    destination.insert(0, aux.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if aux[0] > destination[0]:
                        aux.insert(0, destination.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        destination.insert(0, aux.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
    else:
        for i in range(1, pow(2, n)):
            if i % 3 == 1:
                if len(source) == 0:
                    source.insert(0, destination.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(destination) == 0:
                    destination.insert(0, source.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if source[0] > destination[0]:
                        source.insert(0, destination.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        destination.insert(0, source.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
            elif i % 3 == 2:
                if len(source) == 0:
                    source.insert(0, aux.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(aux) == 0:
                    aux.insert(0, source.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if source[0] > aux[0]:
                        source.insert(0, aux.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        aux.insert(0, source.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
            else:
                if len(aux) == 0:
                    aux.insert(0, destination.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                elif len(destination) == 0:
                    destination.insert(0, aux.pop(0))
                    print(f'{source} \t\t{aux} \t\t{destination}')
                else:
                    if aux[0] > destination[0]:
                        aux.insert(0, destination.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')
                    else:
                        destination.insert(0, aux.pop(0))
                        print(f'{source} \t\t{aux} \t\t{destination}')

source = [1, 2, 3, 4, 5]
aux = []
destination = []
print(f'Source\t\tAux\t\tDestination')
print(f'{source} \t\t{aux} \t\t{destination}')
Tower(5, source, aux, destination)
