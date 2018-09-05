# 15 regexp
import re # regexp is module? OMG!

regexp = 'a'
string = 'vasya@mail.ru'
regexp2 = r'\.ru' # всегда регулярки пихай в raw string, иначе придётся много экранировать

match = re.match(regexp, string) # string begins witch regexp ?
match = re.search(regexp, string) # search string, returns first match
match = re.findall(regexp, string) # search string globally, returns list
match = re.findall(regexp, string, re.I) # ignore case
print(match.group(0)) # finded symbols

split = re.split(r'-', '10-20-30-40') # разделить по знаку
split = re.split(r'-', '10-20-30-40', maxsplit=2) # сколько раз разделять
sub = re.subn(r'vasya', 'petya', string) #substitute (sed or s///) returns tuple (cortege)

mails = ['a@mail.ru', 'b@gmail.com', 'c@ya.ru']
regexp = r'@mail'
pattern = re.compile(regexp, re.I) # привести строку к какому то виду, прекомпилировать
for i in mails:
    print(pattern.search(i))

# demo/regexp.py

# s = 'Python Programming 101 for the Absolute Beginners'
#s = 'abc123xyz' # aaa111zzz
# s = 'ABC 12-4567 12-05-2007, XYZ 45-7896 11-11-2011, HGF 85-4125 12-01-2009'
# s = input('Введите свой день рождения: ')
# result = re.findall(r'^(\d\d?)-(\d{1,2})-(\d{4})$', s, re.I)

##l = ['(910)123-45-45', '1234578456', '(971)4567852']
##p = re.compile(r'\(?(\d{3})\)?(\d{3}-?\d{2}-?\d{2})')
##for phone in l:
##    ok = p.match(phone)
##    print(ok.group(0), ok.group(1), ok.group(2))

##s = 'JohnLennon\nPaulMcCartney\nGeorgeHarrison\nRingoStrar'
##p = r'^([A-Z][a-z]+)([A-Z][a-zA-Z]+)'
##names = re.findall(p, s, re.M)

pattern = re.compile('(\d\d?)-(\d\d?)-(\d{4})')
# 05-31-2018
res = pattern.subn(r'\2-\1-\3', '31-05-2018')


#print(result)
##\w = [a-zA-Z0-9]
##\d = [0-9]
##{3}
##{2,4}
##{2,}
##* == {0,}
##+ == {1,}
##? == {0,1}


##regexp = r'@mail|@gmail'
##mails = ['a@mail.ru', 'b@gmail.com', 'c@ya.ru', 'd@mail.ru']
##pattern = re.compile(regexp, re.I)
##for i in mails:
##    print(pattern.search(i))
##match = re.match(regexp, s, re.I)
##match = re.search(regexp, s, re.I)
##match = re.findall(regexp, s, re.I)
##split = re.split(r'-', '10-20-30-40', maxsplit=2)
##sub = re.subn(r'a', 'b', s)

