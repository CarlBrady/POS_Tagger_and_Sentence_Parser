
def get_tests():
    t=''
    tests_file = open("tests.txt","r") #Open and read file that contains tests sentnces
    tests = tests_file.readlines() #store each line as an individual test sentence
    tests_file.close()
    i = 0
    return tests

def get_lex():

    lex_file = open("lex.txt","r") #Open and read file that contains lexicon
    lex_arr = lex_file.readlines()
    lex_file.close()
    return lex_arr

def get_rules():

    rule_file = open("rules.txt","r") #Open and read file that contains rules
    rule_arr = rule_file.readlines()
    rule_file.close()
    return rule_arr

def get_grammar():
    file = open("grammar.txt","r") #Open and read file that contains rules
    file_str = file.read()
    grammar = CFG.fromstring(file_str) #CFG = Read File
    file.close()
    return grammar


def print_tests():
    t=''
    tests_file = open("tests.txt","r") #Open and read file that contains tests sentnces
    tests = tests_file.readlines() #store each line as an individual test sentence
    tests_file.close()
    i = 0
    for t in tests:
        print(str(i) +': ' + t)
        i += 1
