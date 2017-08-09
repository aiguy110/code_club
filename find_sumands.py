import random

# Generate some random, sorted (ascending), numbers
N = 10
values = list(range(int(N*1.5)))
while len(values) > N:
    i = random.choice(range(len(values)))
    del values[i]

# Target value
target = N

def find_summands_for(target, candidates):
    """
    Returns the indices of the first two numbers found in cadidates which add to
    the target, or returns None if no such numbers are found. (candidates are
    expected to be presorted into ascending order)
    """
    a, b = 0, len(candidates)-1
    while True:
        if a == b:
            return None

        sum = candidates[a] + candidates[b]
        print('sum=={}'.format(sum))
        if sum < target:
            a += 1
            print('a=={}'.format(a))
        elif sum > target:
            b -= 1
            print('b=={}'.format(b))
        else:
            return a,b

found_summands = find_summands_for(target, values) 
print( 'Candidate Summands:\n{}\nTarget:\n{}\nFound Summands:\n{}'.format(values, target, str(found_summands)) )
