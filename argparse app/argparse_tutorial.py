import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help = 'echo the string you use here')
    parser.add_argument("-t","--twice", help="make  it twice", action='store_true')
    args = parser.parse_args()
    print(args.echo)

    if args.twice: 
        print(args.echo)