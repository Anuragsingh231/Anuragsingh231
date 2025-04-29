def count_characters(s):
    no_spaces = ''.join(s.split())
    return len(no_spaces)

string = "Hello, World!"
print("Number of characters (excluding spaces):", count_characters(string))
