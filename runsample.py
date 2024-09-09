import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=0)
    parser.add_argument("--y", type=int, default=0)
    parser.add_argument("--z", type=int, default=0)
    args = parser.parse_args()
    print(args.x,args.y,args.z)

main()
