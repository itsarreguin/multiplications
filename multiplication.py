def run():
    for i in range(1, 11):
        print(' ')
        print(f'Tabla del {i}')
        for j in range(1, 11):
            print(f'{i} x {j} = {i*j}')


if __name__ == '__main__':
    run()
