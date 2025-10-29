text = "Python"
list=['a','e','i','o','u']
for ch in list:
    if ch.lower() in "aeiou":
        print("Vowel found:", ch)
    break