from parser import pos_tagger, grammar_check, bracketed_sentence, incorrect_sentence_parser, build_tree
from file_manager import get_tests, get_lex, get_rules, print_tests


def main():
    rules = get_rules()
    lex_arr = get_lex()
    tests = get_tests()

    while True:
        x = input('\n\nInput a test number, type \'help\' to see all test cases or \'exit\' to exit the program\n')
        if x in 'help':
            print('-----------------------------------------------------------')
            print_tests()

        elif x in 'exit':
            return

        elif x.isdigit():
             print('\n\nRESULTS\n-----------------------------------------------------------')
             x = int(x)
             pos = pos_tagger(x,tests,lex_arr)

             if grammar_check(pos, rules) == True:
                 print('Verdict: Sentence is grammatically correct\n')
                 bracketed_sentence(pos)
                 build_tree(pos)
             else:
                 test = tests[x].split()
                 print('Verdict: Sentence is not grammatically correct\n')
                 incorrect_sentence_parser(test)
        else:
            print('\n-----------------------------------------------------------')
            print('\nPLEASE INPUT A CORRECT COMMAND!\n')
        print('-----------------------------------------------------------')







if __name__== "__main__":
  main()
