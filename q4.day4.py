class Solution:
   def isPalindrome(self, string: str):
       
       sequence=""
       for i in string:
           if i.isalpha():
               sequence+=i
           elif i.isdigit():
               sequence+=i
       sequence=sequence.lower()
       for i in range(len(sequence)//2):
           if sequence[i] != sequence[len(sequence)-1-i]:
               return False
       return True
  
