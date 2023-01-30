#!/usr/bin/python

import random, sys, argparse

class shuf:
    def __init__(self, input):
        self.lines = input
        self.linecount = len(self.lines)

    def randomline(self):
        return random.choice(self.lines)
                         
    def randomsample(self, count=None):
        if count and count < self.linecount: return "".join(random.sample(self.lines, count))
        else: return "".join(random.sample(self.lines, self.linecount))

def exit_error(msg, code=0):

    print (str(msg), file=sys.stderr)
    exit(0)

def main():
    program_name = "shuf"
    usage_msg = """%(prog)s [OPTION]... [FILE]
  or:  shuf -e [OPTION]... [ARG]...
  or:  shuf -i LO-HI [OPTION]...
Write a random permutation of input lines to standard output."""
    program_description = "With no FILE, or when FILE is -, read standard input."

    parser = argparse.ArgumentParser(
            prog = program_name,
            usage = usage_msg,
            description = program_description
            )

    parser.add_argument('file', type=argparse.FileType("r"), nargs='?')
    parser.add_argument('-r', '--repeat', action='store_true', dest="repeat", help="output lines can be repeated") 
    parser.add_argument('-n', '--head-count', metavar="COUNT", type=int, action="store", help="output at most COUNT lines")
    parser.add_argument('-i', '--input-range', metavar="LO-HI", help="treat each number LO through HI as an input line")
    parser.add_argument('-e', '--echo', type=str, nargs='+', help="treat each ARG as an input line")      # option that takes a value
    args = parser.parse_args()
    linecount = args.head_count
    processedInput = []

    try:
        args, unk = parser.parse_known_args()
    except Exception as e:
        exit_error(e)

    if args.file: 
        if args.input_range or args.echo: parser.error("Extra operand.")
        try: 
            processedInput = args.file.readlines()
        except: 
            parser.error("I/O error")
    elif args.input_range:
        lo, hi = map(int, args.input_range.split("-"))
        numberRange = list(range(lo, hi+1))
        numberRange = (str(e) for e in numberRange)
        processedInput = [num + '\n' for num in numberRange]
    elif args.echo:
        accumulate = args.echo
        processedInput = [string + '\n' for string in accumulate]
    else:
        try: 
            args.file = sys.stdin
            processedInput = args.file.readlines()
        except: 
            parser.error("I/O error")


    generator = shuf(processedInput)
    if args.repeat is True:
       if linecount: 
           for x in range(linecount):
               sys.stdout.write(generator.randomline())
       else: 
           while not linecount: 
               try:
                   sys.stdout.write(generator.randomline())
               except:
                   exit(1)
    else:
       sys.stdout.write(generator.randomsample(linecount))
    
if __name__ == "__main__":
    main()
