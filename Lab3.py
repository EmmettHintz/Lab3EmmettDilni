import nltk
from nltk import CFG
from nltk import grammar
from nltk.parse.generate import generate
from nltk import ChartParser, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')


def get_grammar(grammar_fname:str)->grammar.CFG:
    with open(grammar_fname) as f:
        grammar_str = f.read()
    return CFG.fromstring(grammar_str)


def parse_sentence(sentence:str, grammar:grammar.CFG):
    chart_parser = ChartParser(grammar)
    tokens = word_tokenize(sentence)
    parses = chart_parser.parse(tokens)
    # print(f"Tokens: {tokens}")  # Checking tokenization
    return list(parses) 

def generate_sentences(grammar: grammar.CFG, num_sents: int, max_depth=13) -> list:
    """
    Without max_depth a recursive grammar can cause run time error by hitting recursive stack depth limits.  
    """
    sents = generate(grammar, n=num_sents, depth=max_depth)

    return [' '.join(s) for s in sents]

def is_grammatical(sentence:str, grammar:grammar.CFG) -> bool:
    """
    Returns True if sentence is grammatical given the grammar, False otherwise
    """
    if parse_sentence(sentence, grammar):
        return True
    return False


def test_grammar2(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    grammar = get_grammar(grammar_fname)
    for sent in generate_sentences(grammar, num_sents=10):
        print(sent)
        assert is_grammatical(sent, grammar)
    # Tests for part 2 ungrammmatical sentences
    print(is_grammatical('the panda existed the friend', grammar))
    print(is_grammatical('the panda died the sandwich', grammar))
    print(is_grammatical('the panda vanished the pajamas', grammar))
    print(is_grammatical('the panda gave the friend', grammar))
    print(is_grammatical('the panda lent the sandwich', grammar))
    print(is_grammatical('the panda sent the pajamas', grammar))


def test_grammar3(gramqmar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    grammar = get_grammar(gramqmar_fname)
    # for sent in generate_sentences(grammar, num_sents=10):
    #     print(sent)
    #     assert is_grammatical(sent, grammar)
    
    # Tests for part 3 ungrammmatical sentences
    # These should be grammatical
    # the panda vanished peacefully
    # the ponderous pajamas peacefully died
    # My very very ponderous friend existed very very very peacefully.
    # the friend ate the excited delicious sandwich joyfully
    # the delicious panda joyfully saw the excited sandwich
    # the panda took the delicious delicious delicious pajamas in the sandwich in my very ponderous friend
    # the pajamas joyfully gave my friend the ponderous delicious sandwich in the panda
    print('---')
    print('Grammatical sentences')
    print(is_grammatical('the panda vanished peacefully', grammar))
    assert(is_grammatical('the panda vanished peacefully', grammar))
    print(is_grammatical('the ponderous pajamas peacefully died', grammar))
    assert(is_grammatical('the ponderous pajamas peacefully died', grammar))
    print(is_grammatical('the delicious panda joyfully saw the excited sandwich', grammar))
    assert(is_grammatical('the delicious panda joyfully saw the excited sandwich', grammar))
    print(is_grammatical('the friend ate the excited delicious sandwich joyfully', grammar))
    assert(is_grammatical('the friend ate the excited delicious sandwich joyfully', grammar))
    print(is_grammatical('my very very ponderous friend existed very very very peacefully', grammar))
    assert(is_grammatical('my very very ponderous friend existed very very very peacefully', grammar))
    print(is_grammatical('the panda took the delicious delicious delicious pajamas in the sandwich in my very ponderous friend', grammar))
    assert(is_grammatical('the panda took the delicious delicious delicious pajamas in the sandwich in my very ponderous friend', grammar))
    print(is_grammatical('the pajamas joyfully gave my friend the ponderous delicious sandwich in the panda', grammar))
    assert(is_grammatical('the pajamas joyfully gave my friend the ponderous delicious sandwich in the panda', grammar))
    
    print('---')
    print('Ungrammatical sentences')
    print(is_grammatical('the panda ponderous vanished peacefully', grammar))
    assert(is_grammatical('the panda ponderous vanished peacefully', grammar) == False)
    print(is_grammatical('the ponderous panda excited vanished peacefully', grammar))
    assert(is_grammatical('the ponderous panda excited vanished peacefully', grammar) == False)
    print(is_grammatical('the panda gave the delicious very delicious pajamas to my friend peacefully', grammar))
    assert(is_grammatical('the panda gave the delicious very delicious pajamas to my friend peacefully', grammar) == False)
    print(is_grammatical('the panda joyfully peacefully gave the delicious pajamas to my friend', grammar))
    assert(is_grammatical('the panda joyfully peacefully gave the delicious pajamas to my friend', grammar) == False)
    
    print('Autograder Test Cases')
    print('---')
    # the panda very very very very joyfully existed
    # Expected: True Got: False
    assert(is_grammatical('the panda very very very very joyfully existed', grammar) == True) 
    print(is_grammatical('the panda very very joyfully existed', grammar))

    # the panda very very very very joyfully vanished
    # Expected: True Got: False
    assert(is_grammatical('the panda very very very very joyfully vanished', grammar) == True)
    print(is_grammatical('the panda very very very very joyfully vanished', grammar))
    

    # the panda very very very very joyfully died
    # Expected: True Got: False
    print(is_grammatical('the panda very very very very joyfully died', grammar))
    assert(is_grammatical('the panda very very very very joyfully died', grammar) == True)
    
    

    # the panda joyfully gave the excited friend
    # Expected: False Got: True
    print(is_grammatical('the panda joyfully gave the excited friend', grammar))
    assert(is_grammatical('the panda joyfully gave the excited friend', grammar) == False)

    # the very very excited ponderous panda peacefully gave the delicious friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully gave the delicious friend the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully gave the delicious friend the sandwich', grammar) == True)
    
    # the very very excited ponderous panda peacefully gave the delicious friend to the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully gave the delicious friend to the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully gave the delicious friend to the sandwich', grammar) == True)
    
    # the panda peacefully gave the friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the panda peacefully gave the friend the sandwich', grammar))
    assert(is_grammatical('the panda peacefully gave the friend the sandwich', grammar) == True)
    

    # the panda joyfully lent the excited friend
    # Expected: False Got: True
    print(is_grammatical('the panda joyfully lent the excited friend', grammar))
    assert(is_grammatical('the panda joyfully lent the excited friend', grammar) == False)

    # the very very excited ponderous panda peacefully lent the delicious friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully lent the delicious friend the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully lent the delicious friend the sandwich', grammar) == True)

    # the very very excited ponderous panda peacefully lent the delicious friend to the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully lent the delicious friend to the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully lent the delicious friend to the sandwich', grammar) == True)

    # the panda peacefully lent the friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the panda peacefully lent the friend the sandwich', grammar))
    assert(is_grammatical('the panda peacefully lent the friend the sandwich', grammar) == True)

    # the panda joyfully sent the excited friend
    # Expected: False Got: True
    print(is_grammatical('the panda joyfully sent the excited friend', grammar))
    assert(is_grammatical('the panda joyfully sent the excited friend', grammar) == False)

    # the very very excited ponderous panda peacefully sent the delicious friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully sent the delicious friend the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully sent the delicious friend the sandwich', grammar) == True)

    # the very very excited ponderous panda peacefully sent the delicious friend to the sandwich
    # Expected: True Got: False
    print(is_grammatical('the very very excited ponderous panda peacefully sent the delicious friend to the sandwich', grammar))
    assert(is_grammatical('the very very excited ponderous panda peacefully sent the delicious friend to the sandwich', grammar) == True)

    # the panda peacefully sent the friend the sandwich
    # Expected: True Got: False
    print(is_grammatical('the panda peacefully sent the friend the sandwich', grammar))
    assert(is_grammatical('the panda peacefully sent the friend the sandwich', grammar) == True)


def test_grammar4(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    pass

def test_grammar5(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    # that the panda existed very peacefully pleased my friend
    # that the friend that ate my excited delicious sandwich vanished perplexed the ponderous pajamas.
    # that the sandwich in my panda gave the friend that ate the pajamas my sandwich perplexed the friend in her pajamas.
    print('---')
    print('Grammatical sentences')
    grammar = get_grammar(grammar_fname)
    print(is_grammatical('that the panda existed very peacefully pleased my friend', grammar))
    print(is_grammatical('that the friend that ate my excited delicious sandwich vanished perplexed the ponderous pajamas', grammar))
    print(is_grammatical('that the sandwich in my panda gave the friend that ate the pajamas my sandwich perplexed the friend in her pajamas', grammar))
    
def main():
    # grammar = get_grammar('grammar1.txt')
    # for sent in generate_sentences(grammar, num_sents=10):
    #     print(sent)

    # sent = 'the panda saw my friend in her pajamas'

    # for parse in parse_sentence(sent, grammar):
    #     parse.pretty_print() 

    # sent2 = 'the pajamas ate my friend in the panda'

    # for parse in parse_sentence(sent2, grammar):
    #     parse.pretty_print()

    # # TEST GRAMMAR2
    # test_grammar2('Lab3/grammar2.txt')
        
    # TEST GRAMMAR3
    test_grammar3('grammar3.txt')
    
    # Test GRAMMAR5
    # test_grammar5('grammar5.txt')
    
main()
