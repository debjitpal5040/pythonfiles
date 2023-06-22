# KMP string matching algorithm
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
def kmp(text, pattern):
    # Create the prefix table
    prefix = [0]*len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            prefix[j] = i+1
            i += 1
            j += 1
        else:
            if i != 0:
                i = prefix[i-1]
            else:
                prefix[j] = 0
                j += 1
    # Search for the pattern
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix[j-1]
            else:
                i += 1
    if j == len(pattern):
        return i-j
    return -1

print(kmp(text, pattern))