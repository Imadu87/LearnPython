# text = "Python"
# print(text[0:6])
# print(text[0:5:2])
# negative slicing 
# print(text[-2:-1])

# basic structure 
# string[start : end : step]
# Important steps:
#     start: Inclusive 
#     end: exclusive 
#     steps: by default: 1

# Positive Indexing
# P   Y   T   H   O   N
# 0   1   2   3   4   5

# Negative Indexing
# P   Y   T   H   O   N
# -6  -5  -4  -3  -2  -1

# text = "PYTHON"
# print(text[-4:-1]) # THO 

# print(text[-6:])

# Steps
# print(text[::2])
# reverse steps
# print(text[::-2])

# Golden Rule of Slicing
# Agar step positive hai start < end hona chahiye
# Agar step negative hai start > end hona chahiye

# s = "ABCDEFGHIJ"
# print(s[2:7]) 
# print(s[-5:-1])
# print(s[::3])
# print(s[5:1:-1])
# print(s[::-2])

# mn = "Harry"
# print(mn[-4:-2])