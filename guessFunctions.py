import itertools

import sequence  # cyclic inclusion works fine :>

# utility funtion which returns sequential pairs of a list
# pairs([1, 11, 111, 1111])  --> [(1, 11), (11, 111), (111, 1111)]
# pairs([1]) --> []
# pairs([])  --> []
def pairs(lst):
    return zip(lst[:-1], lst[1:])


# A sequence stepping by 1.
# for when we only have one thing before the ellipsis
def guess_step1(pre, post):
    if len(pre) != 1:
        return

    bot = pre[0]
    if len(post) == 0:
        return itertools.count(bot)
    elif len(post) == 1:
        top = post[0]
        if bot <= top:
            return range(bot, top + 1)
        else:
            return range(bot, top - 1, -1)  # note: bot > top in this case
    else:
        assert False, 'Currently only one end-point is supported'



# A sequence of equal steps
def guess_linear(pre, post):
    if not (len(pre) >= 2 or len(post) >= 2):
        return
    step = 0
    firstStep = True
    consistentStep = True

    myPairs = list(itertools.chain(pairs(pre), pairs(post)))
    assert len(myPairs)
    for first, second in myPairs:
        pairStep = second - first
        if firstStep:
            step = pairStep
            firstStep = False
        elif pairStep != step:
            consistentStep = False
            break

    if not consistentStep:
        return

    start = pre[0]  # the beginning of the sequence
    if step == 0:
        if len(post):
            if post[0] != start:
                return
            return [ start ] # since we terminate on ourselves, only return one element
        else:
            return itertools.repeat(start)
    else:
        # assert line through start goes through end
        if len(post):
            end = post[-1]
            if abs(end - start) % step != 0:  # will we end up and the last one?
                return False
            # numItems = abs(end - start) // step
            # return itertools.islice(itertools.count(start, step), numItems+1)
            return itertools.chain(range(start, end, step), [end])
        else:
            return itertools.count(start, step)


# A sequence of equal integer multiplications
def guess_exponential(pre, post):
    if not len(pre) >= 3:
        return

    step = 0
    firstStep = True
    consistentStep = True

    myPairs = list(itertools.chain(pairs(pre), pairs(post)))
    assert len(myPairs) >= 2
    for first, second in myPairs:
        if first == 0: return # let's not divide by zero
        pairStep = second / first
        if firstStep:
            step = pairStep
            firstStep = False
        elif pairStep != step:
            consistentStep = False
            break

    if not consistentStep:
        return

    if step != int(step):
        return
    step = int(step)

    start = pre[0]  # the beginning of the sequence
    if step == 0:
        if len(post):
            if post[0] != start:
                return
            return [ start ] # since we terminate on ourselves, only return one element
        else:
            return itertools.repeat(start)
    else:
        # TODO: assert curve goes through end
        end = 0
        haveEnd = bool(len(post))
        if haveEnd:
            end = abs(post[-1])

        def exponentialGenerator():
            current = start
            while abs(current) <= abs(end) or not haveEnd:
                yield current
                current *= step

        return exponentialGenerator()


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293] # ...
primes_set = set(primes)
def guess_primes(pre, post):
    # TODO: support arbitrarily high primes
    #       currently we only support a finite list of primes to keep it simple

    # def isPrime(n):
    #     # note: this is really naiive prime checking for the sake of briefness.
    #     if n in primes_set: return True
    #     if n < 2: return False
    #     for d in range(2, n):
    #         if n%d == 0:
    #             return False
    #     return True

    # ensure all givent numbers are prime
    if not all( number in primes_set for number in (pre + post) ):
        return

    # guess the sequence of the indecies
    # TODO: binary search for efficiency
    indecies = (
        [ primes.index(prime) for prime in pre  ] +
        [ ...                                   ] +
        [ primes.index(prime) for prime in post ]
    )
    try:
        indexSequence = sequence.sequence(*indecies)  # Yay recursion!
    except:
        return  # our index sequence matches no pattern

    # def exponentialGenerator():
    #     current = start
    #     while abs(current) <= abs(end) or not haveEnd:
    #         yield current
    #         current *= step
    def sequenceOfPrimesGenerator():
        for index in indexSequence:
            yield primes[index]

    return sequenceOfPrimesGenerator()

guessFunctions = [
    guess_step1,
    guess_linear,
    guess_exponential,
    guess_primes,
]


if __name__ == '__main__':
    # you probably wanted to run sequence.py rather than this
    from sequence import main
    main()
