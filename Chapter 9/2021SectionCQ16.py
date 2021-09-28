# Question 16(a
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
 if sorted(w1) == sorted(w2):
   print(w1,"Is an anagram of",w2)
   return True 
 else:
   print(w1,"Is not an anagram of",w2)
   return False

word1 =str. lower (input("Enter the first word: "))
word2 =str. lower (input("Enter the second word:"))

phrase1 =str. lower(input("Enter a phrase:"))



# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1) == sorted(word2)):
   print(word1,"Is an anagram of",word2)
elif(sorted(phrase1) == sorted(word1)):
  print(phrase1,"is an anagram of",word1)
else:
  print(word1,"Is not an anagram of",word2)
is_anagram(word1,word2)
