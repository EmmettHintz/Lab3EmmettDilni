import nltk
from nltk import CFG
from nltk import grammar
from nltk.parse.generate import generate
from nltk import ChartParser, word_tokenize
import os
import json
nltk.download('punkt')
nltk.download('punkt_tab')


def get_grammar(grammar_fname:str)->grammar.CFG:
    """
    something something
    """
    with open(grammar_fname) as f:
        grammar_str = f.read()

    return(CFG.fromstring(grammar_str))


def parse_sentence(sentence:str, grammar:grammar.CFG) -> list:
    """
    something something
    """
    chart_parser = ChartParser(grammar)
    tokens = word_tokenize(sentence)
    parses = chart_parser.parse(tokens)
    return list(parses) 


def is_grammatical(sentence:str, grammar:grammar.CFG) -> bool:
    """

    """
    try:
        parses = parse_sentence(sentence, grammar)
        return len(parses) > 0
    except:
        return False #unable to parse

def test(sentences: dict, grammar: grammar.CFG) -> dict: 
    """
    sentences: dictionary where keys are the sentences mapping to boolean values indicating whether the sentence is grammatical

    output: for each sentence 1 if correct, 0 if incorrect

    """
    res = {} 
    for key,val in sentences.items():
        if is_grammatical(key,grammar)==val:
            res[key] = 1
        else:
            print(key)
            print(f'Expected: {val} \t \t Got: {is_grammatical(key, grammar)}\n')
            res[key] = 0
    
    return res



def test_grammar2(grammar_fname):
    print('\nTesting grammar 2')
    if os.path.exists(grammar_fname):
        grammar = get_grammar(grammar_fname)

        sents = {}
        for IV in ['existed', 'vanished', 'died']:
            ungramm = f'the panda {IV} the friend'
            gramm = f'the panda {IV}'
            sents[ungramm] = False
            sents[gramm] = True

        for DTV in ['gave', 'lent', 'sent']:
            ungramm = f'the panda {DTV} the friend'
            gramm1 = f'the panda {DTV} the friend the sandwich'
            gramm2 = f'the panda {DTV} the friend to the sandwich'

            sents[ungramm] = False
            sents[gramm1] = True
            sents[gramm2] = True

        res = test(sents, grammar)

        return sum(res.values())/len(res)
    else:
        print('No file submitted')
        return -1

def test_grammar3(grammar_fname):
    print('\nTesting grammar 3')
    if os.path.exists(grammar_fname):
        grammar = get_grammar(grammar_fname)

        sents = {}
        for IV in ['existed', 'vanished', 'died']:
            ungramm = f'the panda joyfully {IV} the friend'
            ungramm2 = f'the panda joyfully joyfully {IV} the friend'
            gramm = f'the panda very very very very joyfully {IV}'
            gramm2 = f'the panda {IV} peacefully'
            gramm3 = f'the very very very excited ponderous panda {IV} peacefully'
            sents[ungramm] = False
            sents[ungramm2] = False
            sents[gramm] = True
            sents[gramm2] = True
            sents[gramm3] = True

        for DTV in ['gave', 'lent', 'sent']:
            ungramm = f'the panda joyfully {DTV} the  excited friend'
            ungramm2 = f'the panda joyfully joyfully {DTV} the  excited friend'
            gramm1 = f'the very very excited ponderous panda peacefully {DTV} the delicious friend the sandwich'
            gramm2 = f'the very very excited ponderous panda peacefully {DTV} the delicious friend to the sandwich'
            gramm3 = f'the panda peacefully {DTV} the friend the sandwich'

            sents[ungramm] = False
            sents[gramm1] = True
            sents[gramm2] = True
            sents[gramm3] = True

        res = test(sents, grammar)

        return sum(res.values())/len(res)
    else:
        print('No file submitted')
        return -1

def test_grammar4(grammar_fname):
    print('\nTesting grammar 4')
    if os.path.exists(grammar_fname):
        grammar = get_grammar(grammar_fname)
        sents_list = [
            'the friend that vanished very peacefully saw my friend in her pajamas',
            'the pajamas that ate the delicious sandwich vanished joyfully',
            'my friend that took the very delicious pajamas gave the panda her excited sandwich that vanished',
            'the panda that took the very delicious pajamas gave my friend that ate the sandwich her pajamas that vanished',
            'the ponderous panda that gave the delicious sandwich that existed peacefully to my friend that took the pajamas vanished'
        ]

        sents = {item: True for item in sents_list}

        res = test(sents, grammar)

        return sum(res.values())/len(res)
    else:
        print('No file submitted')
        return -1

def test_grammar5(grammar_fname):
    print('\nTesting grammar 5')
    if os.path.exists(grammar_fname):
        grammar = get_grammar(grammar_fname)
        sents_list = [
            'that the panda existed very peacefully pleased my friend',
            'that the sandwich in my panda gave the very very ponderous friend in the delicious delicious pajamas my sandwich perplexed the friend',
            'that the pajamas in the sandwich peacefully vanished in my very very excited friend surprised the pajamas in my delicious sandwich',
            'that the friend that ate my excited delicious sandwich vanished perplexed the ponderous pajamas',
        ]


        sents = {item: True for item in sents_list}
        ungramm_sents = ['that the panda existed peacefully pleased my friend existed',
        'that the panda existed peacefully perplexed my friend existed',
        'that the panda existed peacefully surprised']

        for sent in ungramm_sents:
            sents[sent] = False

        res = test(sents, grammar)

        return sum(res.values())/len(res)
    else:
        print('No file submitted')
        return -1


def main():
    tests = {
        # 'grammar2.txt': test_grammar2,
        'grammar3.txt': test_grammar3,
        # 'grammar5.txt': test_grammar5
    }

    results = []

    for fname,func in tests.items():
        # if os.path.exists(fname):
        score = func(fname)
        res = {
            "score": score,
            "name": fname,
            "visibility": "visible"
        }

        results.append(res)
        # else:
        #     print(f'{fname} not submitted')

    output = {
        "score": 0,
        "tests": results
    }

    print()
    print('Printing accuracy on each grammar')
    for item in output["tests"]:
        name = item["name"].split("/")[-1]
        print(f'{name}: \t {item["score"]}')

    # with open('/autograder/results/results.json', 'w') as f:
    #     json.dump(output, f)


if __name__ == '__main__':
    main()