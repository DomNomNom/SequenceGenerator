import itertools

import guessFunctions


"""
Tries to generate a sequence of things given examples and an ellipsis.

Example use:
    sequence(1,...,10)      --> 1,2,3,4,5,6,7,8,9,10
    sequence(2,4,6,...)     --> 2,4,6,8,10,12,14...   (linear sequence)
    sequence(2,4,8,...)     --> 2,4,8,16,32,64,128... (exponential sequence)
    sequence(2,4,8,...,64)  --> 2,4,8,16,32,64


Optionally, a guessFunction can be explicitely specified such that we consistently use that one instead of guessing
"""
def sequence(*args, guessFunction=None):
    assert args.count(Ellipsis) == 1, "you must give this function an ellipsis (...) otherwise it's no fun."
    assert all( type(arg) in [int, type(Ellipsis)] for arg in args ), "only integers are supported for now"

    # get number pre and post the ellipsis
    ellipsisIndex = args.index(Ellipsis)
    pre = args[:ellipsisIndex]
    post = args[ellipsisIndex+1:]

    assert len(pre) >= 1, "you must specify a starting point"

    if guessFunction is None:
        guesses = ( guess(pre, post) for guess in guessFunctions.guessFunctions )
    else:
        guesses = [ guessFunction(pre, post) ]
    guesses = list(filter(lambda x: x, guesses))

    assert len(guesses) > 0, "I couldn't guess the sequence you wanted"
    assert len(guesses) == 1, "The given sequence is ambiguous. I have multiple candidates which fit your description but would give different results: {}".format(guesses)

    return guesses[0]




def main():

    # prints a finite amount of the generated sequence
    def testSequence(*args):
        seq = sequence(*args)
        print (list(itertools.islice(seq, 20)))

    # lets test it
    # testSequence(20,...,12)
    # testSequence(3,6,9,...)
    # testSequence(2,4,8,...,64)
    testSequence(3,6,9,12, ..., 27,30)
    testSequence(3,0,-3,...,-9)

if __name__ == '__main__':
    main()
