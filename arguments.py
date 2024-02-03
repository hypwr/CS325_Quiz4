import argparse

def argumentClass():
    argparser=argparse.ArgumentParser()
    argparser.add_argument(help='Enter a string',dest='string1',type=str)
    argparser.add_argument(help='Enter a integer/whole number',dest='int1',type=int)
    argparser.add_argument(help='Enter a decimal number',dest='float1',type=float)
    
    args=argparser.parse_args()

    coolWord=args.string1
    coolInt=args.int1
    coolFloat=args.float1

    print("You're cool word is \""+coolWord+"\"")
    print("You're cool integer is \""+str(coolInt)+"\"")
    print("You're cool floating point number is \""+str(coolFloat)+"\"")

def main() -> None:
    argumentClass()

main()