
from nose.tools import *
import sys
sys.path.append('D:\Rohit\Projects\Grep')
from grep import utils
import re


def test_convert_patterns():
	# test that i can convert a list of patterns into expressions
    results = utils.convert_patterns(['else','elif'])
    # assert that they are equal to my expectations
    expected = [re.compile('else'), re.compile('elif')]
    assert_equal(results, expected)


def test_troll_directories():
	# given a directory, return all of its contents
    results = utils.troll_directories(".")
    # assert that we have same contents
    assert_true('./tests/grep_tests.py' in results)


def test_apply_grep():
	
	# get a list of directories
    file = utils.troll_directories['.']
    patterns = utils.convert_patterns(['else'])

    # apply a simple pattern on them
    utils.apply_patterns(files, patterns)
    #assert that we get the right results
    
