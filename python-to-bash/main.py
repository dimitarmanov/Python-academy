import argparse

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('-v', '--var')

if __name__ == '__main__':
    args = parser.parse_args()
    if not args.var:
        print("NO VALUE")
    else:
        print("HELLO from PYTHON", args.var)

# python3 main.py -v Az

