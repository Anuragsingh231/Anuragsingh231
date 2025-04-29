def reverse_lines(text):
    lines = text.split('\n')
    for line in lines:
        print(line[::-1])

sample_text = """Hello world
Python is fun
This is a test"""

reverse_lines(sample_text)
