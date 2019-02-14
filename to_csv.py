import sys
import re

def to_csv(f_in, f_out):
    lines = list(f_in)[1:]
    regex = re.compile(r'[ \t]+')
    for i in range(len(lines)):
        line = lines[i]
        line = re.sub(regex, ',', line)
        line = '{},'.format(i) + line
        f_out.write(line)
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 to_csv.py <filename>.txt')
        print('Please make sure txt file is of proper format:')
        print('header1 header2 ... headerN')
        print('value1 value2 ... valueN')
        print('...')
        exit(1)

    file = open(sys.argv[1], 'r')
    csv = open('./mhc.csv', 'w')
    to_csv(file, csv)
