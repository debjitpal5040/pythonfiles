text = "ABABDABACDABABCABAB"
pattern = "ABAB"
def rabin_carp(text, pattern):
    # Calculate the hash of the pattern
    p = 0
    for i in range(len(pattern)):
        p += ord(pattern[i]) * 26**(len(pattern)-i-1)
    # Calculate the hash of the first window
    t = 0
    for i in range(len(pattern)):
        t += ord(text[i]) * 26**(len(pattern)-i-1)
    # Compare the hashes
    for i in range(len(text)-len(pattern)+1):
        if t == p:
            return i
        else:
            if i < len(text)-len(pattern):
                t = (t - ord(text[i])*26**(len(pattern)-1))*26 + ord(text[i+len(pattern)])
    return -1

print(rabin_carp(text, pattern))