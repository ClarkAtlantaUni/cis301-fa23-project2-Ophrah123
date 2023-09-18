import sys

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print (args)
    print(f"Missing command line arguments")

def parse_cli_argv(argv):
    raise NotImplementedError('not implemented yet')
    
if __name__ == "__main__":
    main()