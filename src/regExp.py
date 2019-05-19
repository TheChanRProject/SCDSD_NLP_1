# r'[\w\.-]+@[\w\.-]+' Email
# r"(\d{3}\d{3}\d{4})" Phone number based on digits
# r".*?(\(?\d{3})? ?[\.-]? ?\d{3} ?[\.-]? ?\d{4}).*?" Phone number with possible delimiters
# r"(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
# Facebook URL matching ^
# https://regexr.com/
# best reg exp for phone num: r"(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})"

import os
import re
textFiles = os.listdir("data")

file = open("data/findNumbers.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
    print(re.findall(r"(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})", line))
    
