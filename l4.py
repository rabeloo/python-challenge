from urllib.request import urlopen
import re

baseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
number = '12345'

while True:
    print(baseUrl+number)
    content = urlopen(baseUrl + number).read().decode()
    pattern = re.compile("and the next nothing is (\d+)")
    match = pattern.search(content)
    if match == None:
        if content == "Yes. Divide by two and keep going.":
            number = str(int(number)/2)
        else:
            print(content)
            break;
    else:
        number = match.group(1)