import re
# string = "Good morning , it is good,everything is good"
# match = re.match("good",string,re.I)      # I- case insensitive  #<re.Match object; span=(0, 4), match='Good'>
# #match1 = re.search("good",string,re.I)      #<re.Match object; span=(0, 4), match='Good'>
# #match2 = re.findall("good",string,re.I)      #['Good']
# print(match)

# # if match:
# #     print("Matching",match.group(0))

# match3= re.findall("(?i)morning",string)        #Also case insensitive
# print(match3)

# match4= re.findall("good.morning",string,re.I | re.DOTALL)  #['Good morning']
# print(match4)

# match5= re.search("good.morning",string,re.I | re.DOTALL)   #DOTALL will works with findall and search
# myspan = match5.span()
# print(myspan)   #(0, 12)

# l=[]
# for i in re.finditer(re.escape("good"),string,re.I):    
#     print(i)    #<re.Match object; span=(0, 4), match='Good'>,<re.Match object; span=(21, 25), match='good'>,<re.Match object; span=(40, 44), match='good'>
#     l.append(i.span())
# print(l)        #[(0, 4), (21, 25), (40, 44)]


# match6 = re.sub("(?i)good","excellent",string)  #excellent morning , it is excellent,everything is good
# print(match6)

string1 = '''hi 
hello
how are you
welcome'''
# match7 = re.split("\n",string1)
# print(match7)
pattern = r'[a].*[y]'
match = re.findall(pattern,string1)
print(match)