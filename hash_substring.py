def read_input():
    source = input().strip()
    if source == "I":
        pattern = input().strip()
        text = input().strip()
    elif source == "F":
        file_name = input().strip()
        with open(file_name, mode="r") as input_file:
            pattern = input_file.readline().strip()
            text = input_file.readline().strip()
    return pattern, text

def print_occurrences(output):
    print(" ".join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 10**9+7
    multiplier = 256
    len_pattern = len(pattern)
    len_text = len(text)
    pattern_hash = sum(ord(pattern[i])*multiplier**(len_pattern-i-1) for i in range(len_pattern)) % prime
    rolling_hash = sum(ord(text[i])*multiplier**(len_pattern-i-1) for i in range(len_pattern)) % prime
    multiplier_to_len = pow(multiplier, len_pattern-1, prime)
    occurrences = []
    for i in range(len_text-len_pattern+1):
        if rolling_hash == pattern_hash and text[i:i+len_pattern] == pattern:
            occurrences.append(i)
        if i < len_text-len_pattern:
            rolling_hash = (rolling_hash - ord(text[i])*multiplier_to_len) % prime
            rolling_hash = (rolling_hash*multiplier + ord(text[i+len_pattern])) % prime
            rolling_hash = (rolling_hash + prime) % prime
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
