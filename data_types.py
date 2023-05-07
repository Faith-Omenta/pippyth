# Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string
def swap_characters(word_name1,word_name2):
    word_name1=word_name2[0:2]+word_name1[0:2]
    word_name2=word_name1[0:2]+word_name2[0:2]
    return word_name1+ " " +word_name2
print(swap_characters("Faith","Omenta"))

#Write a Python function that takes a list of words and returns the longest word
# and the length of the longest one
def lengt_of_longest(text):
    count = 0

    for i in text:
        if len(i)>=count:
            count=len(i)
            return count
print(lengt_of_longest(["volkswagen","volvo","porsche"]))
#Write a Python program that accepts a comma-separated sequence of words as input 
# and prints the distinct words in sorted form (alphanumerically).
def distinct_words(text):
    text = text.split(",")
    
    text = [text.strip() for text in text]
   
    distinct_word = sorted(set(text))

    return distinct_word
print(distinct_words("Lindsay,Glenah,Melvin,Philis,Darlene"))


#Write a Python function that takes two lists and returns True if they have at 
# least one common member.
def common_member(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                answer = True
                return answer
print(common_member([10,34,65,42], [34,21,40,23]))

# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], 
# ["#000000", "#FF0000", "#800000", "#FFFF00"]

l1=["Black", "Red", "Maroon", "Yellow"], 
l2=["#000000", "#FF0000", "#800000", "#FFFF00"]
def convert_list(keys, values):
    list = [{keys[i]: values[i]} for i in range(len(keys))]
    return list
print(convert_list(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))

# Write a Python program to check whether all dictionaries in a list are empty or 
# not

l = [{},{},{}] 
all_empty = True
for i in l:
    if i:
        all_empty = False


# Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
numbers = [3,5,45,97,32,22,10,19,39,43]
remove_odd = [n for n in numbers if n%2 == 0 ]
print(remove_odd)

#Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5
list_a = [1,2,3,4]
list_b = [2,3,4,5]
common_numbers_in_list = [x for x in list_a if x in list_b]
print (common_numbers_in_list)

#Use a nested list comprehension to find all of the numbers from 1-1000 that 
# are divisible by any single digit besides 1 (2-9)
all_numbers=list(range(1,1000))
all__numbers=list(range(2,9))
s = [number for number in range(1,1000) if True in [True for x in range(2,9) if number % x == 0]]
print(s)
# Write a Python function to remove all vowels in a string
def remove_vowels(name):
    vowels = ["a","e","i","o","u"]
    empty = ""
    for i in range(len(name)):
        if name[i] not in vowels:
            empty += name[i]
    return empty

print(remove_vowels("Lindsay"))
