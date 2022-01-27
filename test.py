#test
import os 
from subprocess import getstatusoutput, getoutput

prg = './hello.py'


def test_exists():

    assert os.path.isfile(prg)