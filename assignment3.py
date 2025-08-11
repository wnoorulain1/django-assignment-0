# Program to check if two strings are anagrams

def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Compare sorted versions of both strings
    return sorted(s1) == sorted(s2)


# Example input
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Check and print result
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")