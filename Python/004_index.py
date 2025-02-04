#isnumberic
s3="\u00B2"
s4="10\u00BD"

print("====================================")
print(s3.isdecimal())
print(s3.isdigit())
print(s3.isnumeric()) #isnumeric() takes no arguments (1 given)
print(s3.isidentifier()) #isidentifier() takes no arguments (1 given)
print(s3)

print("====================================")

print(s4.isdecimal())
print(s4.isdigit())
print(s4.isnumeric()) #isnumeric() takes no arguments (1 given)
print(s4)
print("====================================")

s="hello world"
print(s.islower())
print(s.isupper())

print("====================================")

a=["hai","hello","world"]
print("?".join(a))

print("====================================")

stp="hello world"
print(stp.strip("hwd"))

print("====================================")

SP="hello world"
print(SP.split(", "))
print(SP.title())
print(SP.swapcase())