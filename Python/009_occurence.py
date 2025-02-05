#find tha occurence of a string in a list

my_list = ["apple", "banana", "apple", "banana", "apple", "banana", "apple", "banana"]
alphabet = input("Enter the alphabet to find: ")  # You want to input a single letter

joined = "".join(my_list)
count = joined.count(alphabet)

print(f"The alphabet {alphabet} occurs {count} times in the list.")