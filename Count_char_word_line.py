def count_text_stats(text):
    num_characters = len(text)
    num_words = len(text.split())
    num_lines = len(text.splitlines())

    return num_characters, num_words, num_lines

sample_text = """Hello world
Python is fun
This is a test"""

chars, words, lines = count_text_stats(sample_text)
print("Characters:", chars)
print("Words:", words)
print("Lines:", lines)
