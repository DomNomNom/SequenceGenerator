import itertools

from guessFunctions import guessFunctions


"""
Tries to generate a sequence of things given examples and an ellipsis.

Example use:
    sequence(1,...,10)
    sequence(2,4,6,...) --> 2,4,6,8,10,12,14... (linear sequence)
    sequence(2,4,8,...) --> 2,4,8,16,32,64,128... (exponential sequence)
    sequence(2,4,8,...,64)
    # maybe later: sequence('a',...'z')  # The lowercase alphabet from 'a'
"""
def sequence(*args):
    assert args.count(Ellipsis) == 1, "you must give this function an ellipsis (...) otherwise it's no fun."
    assert all([ type(arg) in [int, type(Ellipsis)] for arg in args ]), "only integers are supported for now"
    ellipsisIndex = args.index(Ellipsis)

    # pre and post ellipsis
    pre = args[:ellipsisIndex]
    post = args[ellipsisIndex+1:]

    assert len(pre) >= 1, "you must specify a starting point"

    guesses = [ guess(pre, post) for guess in guessFunctions ]
    guesses = list(filter(lambda x: x, guesses))
    assert len(guesses) > 0, "I couldn't guess the sequence you wanted"
    assert len(guesses) == 1, "The given sequence is ambiguous. I have multiple candidates which fit your description but would give different results: {}".format(guesses)
    return guesses[0]




def main():
    # prints a finite amount of the generated sequence
    def testSequence(*args):
        seq = sequence(*args)
        print (list(itertools.islice(seq, 20)))

    testSequence(20,...,12)
    testSequence(3,6,9,...)
    testSequence(2,4,8,...,64)

if __name__ == '__main__':
    main()