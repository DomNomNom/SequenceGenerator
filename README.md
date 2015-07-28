# SequenceGenerator
Tries to generate a sequence of things given examples and an ellipsis.
Example use:

    sequence(1,...,10)      --> 1,2,3,4,5,6,7,8,9,10
    sequence(2,4,6,...)     --> 2,4,6,8,10,12,14...   (linear sequence)
    sequence(2,4,8,...)     --> 2,4,8,16,32,64,128... (exponential sequence)
    sequence(2,4,8,...,64)  --> 2,4,8,16,32,64

