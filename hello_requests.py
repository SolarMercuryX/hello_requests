import time

def main():
    print('Hello World !')

if __name__ == '__main__':
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f'[Finished in {(end_time - start_time):.1f}s]')
