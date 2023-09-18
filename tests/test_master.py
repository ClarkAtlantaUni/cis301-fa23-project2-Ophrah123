import pickle

from cis301.project2.__main__ import main


def store(obj, fileName):
    file= None
    try:
        file = open(fileName, "wb")
        pickle.dump(obj, file)
    except:
        raise Exception("IO Exception")
    finally:
        if file != None:
            file.close();
def load(fileName):
    obj=None
    try:
        file = open(fileName, "rb")
        obj = pickle.load(file)
    except:
        raise Exception("IO Exception")
    finally:
        return obj

def test_main(capsys):
    print(main())
    captured = capsys.readouterr()
    config = load("tdata.dat", "rb")
    assert config['usage'] == captured.out


def test_phonebill():
    phonebill = PhoneBill("customer name")
    print(phonebill)

def test_phonecall():
    phonecall = PhoneCall("404123456", "")