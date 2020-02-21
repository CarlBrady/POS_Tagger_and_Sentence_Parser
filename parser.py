from treelib import Node, Tree

#pos_tagger(x,tests,lex_arr) x = test number, tests = list of test sentences, lex_arr = list of lexicon rules
#This function compares each word of the test sentence against the lexicon file and allocates the related tag
def pos_tagger(x,tests,lex_arr):
    sentence= ''
    j = 0
    i = 0
    test = tests[x].split()
    print('\nTest Sentence: ' + tests[x])
    for word in test:
        for lexi in lex_arr:
            lex = lex_arr[j].split()
            if test[i] == lex[1]:
                sentence += lex_arr[j]
            j+= 1
        j = 0
        i += 1
    return sentence


# grammar_check(pos,rules) is a boolean function that takes in the tagged pos sentence
# and a list of rules and compares the two and returns true if the sentence is correct
def grammar_check(pos, rules):
    checker = ''
    i = 1
    pos_split = pos.split()
    pos_NP = pos_split[0] + ' ' + pos_split[2] # gets the POS tag for the first two words and adds to string
    pos_VP = pos_split[4] # gets the POS tag for the third word and adds to string
    pos_NP2 = pos_split[6] + ' '+pos_split[8] + ' ' + pos_split[10] # gets the POS tag for the last three words and adds to string


    if pos_split[1] in 'a' and pos_split[3] == 'men': # checks for 'a men' in a sentence
        print('\'A men\' is grammatically incorrect.')
        return False
    elif pos_split[1] in 'a' and pos_split[3] == 'women': # checks for 'a women' in a sentence
        print('\'A women\' is grammatically incorrect')
        return False


    while i<3: # Checking the if the childern of NP that has a parent of S are correct
        rule = rules[i].split('->')
        x = rule[1].split() # rule[1] is only split here again to fix the formatting and remove extra spacing
        y = x[0]+' '+x[1] # here we assign formatted x to y
        if pos_NP == y:
            checker += rule[0] # rule[0] is the left hand side of the matching rule
        i += 1
    i=4
    while i<6: # Checking if the childern of VP the has a parent of VP are correct
        rule = rules[i].split('->')
        x = rule[1].split()
        y = x[0]
        if pos_VP == y:
            checker += rule[0]
        i += 1

    rule = rules[6].split('-> ') #checks if the childern of NP that has a parent of VP are correct
    x = rule[1].split()
    y = x[0]+' '+x[1]+' '+x[2]
    if pos_NP2 == y:
        checker += rule[0]
    i += 1

    str_split = checker.split()
    if str_split[2] == 'NP': # all POS tags have been analysed and if the sentence is correct 'checker' should be NP VPzNP or NPp VPp NP
        if str_split[0] == 'NP' and str_split[1] == 'VPz':
            return True
        elif str_split[0] == 'NPp' and str_split[1] == 'VPp':
            return True
    else:
        return False


# bracketed_sentence(sentence) takes in a test sentence that has been proven to be correct and creates a bracketed phrasal structure
def bracketed_sentence(sentence):
    i = 0
    br_sentence = '[S1[S[NP['
    split = sentence.split()
    while i<3:
        br_sentence += '[' + split[i] + ' ' + split[i+1] + ']'
        i+=2
    br_sentence += ']][VP[VP'
    while i<5:
        br_sentence += '[' + split[i] + ' ' + split[i+1] + ']'
        i+=2
    br_sentence += '][NP['
    while i<11:
        br_sentence += '[' + split[i] + ' ' + split[i+1] + ']'
        i+=2
    br_sentence += ']]]'
    print(br_sentence)

# build_tree also takes a correct sentnce as an arg and outputs a tree to the cmd line
def build_tree(sentence):
    print('\n\nParser Tree Plot\n')
    split = sentence.split()
    tree = Tree()
    tree.create_node("S1", "s1")
    tree.create_node("S", "s", parent="s1")
    tree.create_node("NP", "np", parent="s")
    tree.create_node("VP", "vp", parent="s")
    tree.create_node("VP", "vp2", parent = "vp")
    tree.create_node("_NP", "np2", parent = "vp")
    tree.create_node(split[0],"dt" , parent="np")
    tree.create_node(split[2], "nn", parent="np")
    tree.create_node(split[4], "vb", parent="vp2")
    tree.create_node(split[6], "dt2", parent="np2")
    tree.create_node(split[8], "jj", parent="np2")
    tree.create_node(split[10], "nn1", parent="np2")
    tree.create_node(split[1],"1" , parent="dt")
    tree.create_node(split[3], "2", parent="nn")
    tree.create_node(split[5], "3", parent="vb")
    tree.create_node(split[7], "4", parent="dt2")
    tree.create_node(split[9], "5", parent="jj")
    tree.create_node(split[11], "6", parent="nn1")
    tree.show()



# incorrect_sentence_parser(sentence) takes an incorrect sentence and creates a bracketed phrasal structure for as long as the sentence is valid
def incorrect_sentence_parser(sentence):
    br_str = '[S1[S[NP['
    if repr(sentence[0]) == "'the'":
        br_str += "DT the]"

    elif repr(sentence[0]) == "'a'":
        br_str += "DT a]"

    else:
        return

    if repr(sentence[1]) in "'men'":
        if repr(sentence[0]) in ("'a'"):
            return
        else:
            x = repr(sentence[1])
            br_str += "[NNP "+ x[1:-1] +"]"

    elif repr(sentence[1]) in "'man'":
        if repr(sentence[0]) in ("'a'"):
            return
        else:
                x = repr(sentence[1])
                br_str += "[NNP "+ x[1:-1]+"]"

    else:
        return

    if repr(sentence[2]) == "'bites'":
        if repr(sentence[1]) not in ("'man'" , "'woman'"):
            print('Sentence incorrect but correct as far as ' + repr(sentence[1]))
            br_str += "]]"
            print('\n' + br_str)
            return

    elif repr(sentence[2]) == "'bite'":
        if repr(sentence[1]) not in ("'men'" , "'women'"):
            print('Sentence incorrect but correct as far as ' + repr(sentence[1]))
            br_str += "]]]"
            print('\n' + br_str)
            return

    elif repr(sentence[2]) == "'like'":
        if repr(sentence[1]) not in ("'men'" , "'women'"):
            print('Sentence incorrect but correct as far as ' + repr(sentence[1]))
            br_str += "]]]"
            print('\n' + br_str)
            return

    elif repr(sentence[2]) == "'likes'":
        if repr(sentence[1]) not in ("'man'" , "'woman'"):
            print('Sentence incorrect but correct as far as ' + repr(sentence[1]))
            br_str += "]]]"
            print('\n' + br_str)
            return


    br_str += "]]"
    return
