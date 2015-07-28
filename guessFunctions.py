import itertools

# utility funtion which returns sequential pairs of a list
# pairs([1, 11, 111, 1111])  --> [(1, 11), (11, 111), (111, 1111)]
# pairs([1]) --> []
# pairs([])  --> []
def pairs(lst):
    return zip(lst[:-1], lst[1:])



# special case when we only have one thing before the ellipsis
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
            assert False, 'not implemented'
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
        pairStep = second // first
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



guessFunctions = [
    guess_step1,
    guess_linear,
    guess_exponential,
]



if __name__ == '__main__':
    from sequence import main
    main()