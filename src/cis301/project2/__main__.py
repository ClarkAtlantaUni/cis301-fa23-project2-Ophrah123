import re
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


def usage():
    help = 'Usuage: project2 [options] <args>args are (in this order):'\
    +'\tcustomer\t\t\t'+'person whose phone bill we are modeling\n'\
    +'\tcaller number\t\t' +'person whose phone number we are modeling\n'

    return help


def isvalid_phone_number(phone_number):
    phone_pattern = r"[1-9][0-9]{2}[0-9]{3}-[0-9]{4}$"
    if re.match(phone_pattern, phone_number):
        return True
    else:
        return False
    #Compile phone pattern


def parse_cli_argv(argv):
    indx = 0
    print_flag = False

    if "-README" in argv:
        print(usage())
        exit()
    if "-print" in argv and len(argv) == 8:
        if argv[0] == "-print":
            indx += 1
            print_flag = True
        else:
            print(usage())
            return

    elif len(argv) == 7:
        print(usage())
        return

    #check for -print

    #if -print then print a summary
    #TODO: Check the list of args for each phonebill/call

    #TODO: Check for owner
    owner = argv[indx]

    #TODO: Check caller and validate phone number
    caller = argv[indx + 1]
    #phone number format: 000-000-0000

    if not isvalid_phone_number(caller):
        print(usage())
        return


    #TODO: Check callee and validate phone numner
    calle = argv[indx + 2]

    #TODO: Check start date and time + validate date/time format
    #TODO: Check end date and time + validate date/time format
    #TODO: instantiate a phonebill
    #TODO: instantiate a phonecall
    #TODO: Add phonecall to phonebill
    #TODO: If -print then print a summary



if __name__ == "__main__":
    main()
