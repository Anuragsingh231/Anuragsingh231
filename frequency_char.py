def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = "hello world"
result = char_frequency(string)
print("Character frequencies:", result)
