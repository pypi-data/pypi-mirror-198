import os
import subprocess
import sys
from unittest import mock

from unittest.mock import Mock

from src.PTWordFinder import calculate_words
from src.PTWordFinder import nonblank_lines
from click.testing import CliRunner

# Functional test

def test_help():
    exit_status = os.system('python3 src/PTWordFinder.py --help')
    assert exit_status == 0
    
def test_valid_files():
    exit_status = os.system('python3 src/PTWordFinder.py tests/words-list.txt tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt')
    assert exit_status == 0

def test_too_low_arguments():
    exit_status = subprocess.run(['python3','src/PTWordFinder.py', 'tests/words-list.txt'], capture_output=True, text=True)
    assert True == exit_status.stderr.__contains__('Error: Missing argument')

def test_not_existed_file():
    exit_status = subprocess.run(['python3','src/PTWordFinder.py', 'words-list.txt', 'nonexisted_file.txt'], capture_output=True, text=True)
    assert True == exit_status.stderr.__contains__(' No such file or directory')

def test_number_of_lines():
    result = subprocess.run(['python3','src/PTWordFinder.py', 'tests/words-list.txt', 'tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    assert True == result.stdout.__contains__('Number of lines : 9513')

def test_number_of_words():
    result = subprocess.run(['python3','src/PTWordFinder.py', 'tests/words-list.txt', 'tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    assert True == result.stdout.__contains__('Found: 166 words')

def test_time_in_second():
    result = subprocess.run(['python3','src/PTWordFinder.py', 'tests/words-list.txt', 'tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    # time musat be under 1 second
    assert True == result.stdout.__contains__('Time elapsed: 0.')
    
    # Unit tests

def test_calculate_words():
    runner = CliRunner()
    result = runner.invoke(calculate_words, ['tests/words-list.txt','tests/test-file.txt'])
    assert result.exit_code == 0      
    assert result.output == ("Number of lines : 4\n"
                                "Found: 6 words\n"
                                "Time elapsed: 0.0 second\n")
    
def test_nonblank_lines_for_multilines():

    # given

    # multiline string
    # multiple spaces ale skipped
    # empty line not counting
    # specjal charakter not conting
    first_line = 'bb bbb, bbb       '
    second_line = "    ...   "
    third_line = "  dd d d  (ddd)   d      \n"

    text='\n'.join((first_line,second_line,third_line))

    filename ='test-file'
 
    text_data = mock.mock_open(read_data=text)
     
    with mock.patch('%s.open' % __name__,text_data, create=True):
        f = open(filename)
        
    #when
        print(f)
        result = nonblank_lines(f)
        result=list(result)
    
    #then        
    expected_text =[['bb', 'bbb', 'bbb'],[''],['dd', 'd', 'd','ddd','d']]    
    assert result ==  expected_text
 

def test_nonblank_lines_for_one_line():
    #given

    # one line string
    filename ='test-file'
    text= '     bb bbb, bbb,       '


    #when     
    text_data = mock.mock_open(read_data=text)
    
    with mock.patch('%s.open' % __name__,text_data, create=True):
        f = open(filename)
        
        result = nonblank_lines(f)
        result=list(result)

    #then
        expected_text = [['bb', 'bbb', 'bbb']]
    
        assert result ==  expected_text

if __name__ == "__main__":
    sys.exit(calculate_words(sys.argv))     
