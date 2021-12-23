import argparse
import time

def main():
    print('Hello World !')

    ap = argparse.ArgumentParser()
    ap.add_argument('-c', action='store_true')
    ap.add_argument('-f')
    ap.add_argument('-l', action='store_true')

    args = ap.parse_args()

    with open(args.f, 'r') as f:
        if args.c:
            print(len(f.read()))
            f.seek(0)
        if args.l:
            print(len(f.readlines()) + 1)

if __name__ == '__main__':
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f'[Finished in {(end_time - start_time):.1f}s]')
