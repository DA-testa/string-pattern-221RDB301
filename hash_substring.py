# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())
        source = input().rstrip()
        if source == 'F':
            filename = input().rstrip()
            with open(filename, 'r') as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        else:
            pattern = input().rstrip()
            text = input().rstrip()
        return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    p = 10**9 + 7
    x = 263
    m = len(pattern)
    n = len(text)
    pattern_hash = sum([ord(pattern[i]) * pow(x, i, p) for i in range(m)]) % p
    rolling_hash = sum([ord(text[i]) * pow(x, i, p) for i in range(m)]) % p
    x_m = pow(x, m, p)
    occurrences = []
    
    for i in range(n - m + 1):
        if pattern_hash == rolling_hash and pattern == text[i:i+m]:
            occurrences.append(i)
        
        if i < n - m:
            rolling_hash = (rolling_hash - ord(text[i]) + ord(text[i+m]) * x_m) % p
    
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

