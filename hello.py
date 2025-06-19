# Find all vowels in the string "chaitanya"
# Expected: a, i, a, a
a="chaitanya"
for i in a:
    if i in "aeiou":
        print(i)
a
i
a
a

# Find how many tibmes the letter 'a' appears in "banana"
# Expected: 3
b="banana"
count=0
for i in b:
    if i in "a":
        count+=1
        print(count)
        

# Print all the characters in "education" that are not vowels
# Expected: d, c, t, n
k="education"
for i in k:
    if i not in "aeiou":
        print(i)

# Count how many times each character appears in "mississippi"


# Find and print all the capital letters in "WelcomeToPython"
# k="WelcomeToPython"
for i in k:
    if i.isupper():
        print(i)

# Print all characters at even indexes from "developer"
# Expected: d, v, l, p, r
a="developer"
b=0
for b in range(0,len(a)):
    if b%2==0:
        print(a[b])

# Check if the character 'z' is present in "amazing"
# Expected: Yes
a="amazing"
if "z"in a:
    print("yes")

# Print all characters of "programming" that appear more than once
# Expected: r, g, m
s="programming"
p=set(s)
for i in p:
    if s.count(i)>1:
        print(i)

# Replace all 'a' with '*' in "banana"
# Expected: b*n*n*
a="banana"
b=a.replace("a","*")
print(b)

b*n*n*

# Remove all vowels from "chaitanya" and print the result
# Expected: chtny
a="chaitanya"
for i in a:
    if i not in "aeiou":
        print(i)
c
h
t
n
y