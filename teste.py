from bs4 import BeatifulSoup

with open('cfederal.html', 'r') as f:
    soup_string = BeatifulSoup(f.read(), 'html.parser')
print(soup_string)