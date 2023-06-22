text = "ABABDABACDABABCABAB"
pattern = "ABAB"
def boyer_moore(text, pattern):
    # Create the bad character table
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    # Search for the pattern
    i = 0
    while i < len(text)-len(pattern)+1:
        j = len(pattern)-1
        while j >= 0 and text[i+j] == pattern[j]:
            j -= 1
        if j == -1:
            return i
        else:
            if text[i+j] in bad_char:
                i += max(1, j-bad_char[text[i+j]])
            else:
                i += j+1
    return -1

print(boyer_moore(text, pattern))