from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # An anagram is a word or phrase formed by rearranging the letters of a 
        # different word or phrase, using all the original letters exactly once.


        # first of all both  the words should be of same lenght
        # arrenge both the words in alphabetical order
        #  if same then anagram --- time complexcity ---O(n logn) --slow

        # or take frequency counts for each character --- by making dictionary 
        # so if we say that we have two dictionaries a and b for both words 
        # how will we compair them --- so in a it will check all key and values and then check inb
        # if there is anything in b that was not in a 
        # and somehow the itr in a is O(n) whereas for b it is O(1)

        
        # built in fun used 
        if len(s) != len(t):
            return False
        # return sorted(s) == sorted(t)
        # but the time com is O(n log n)

        return Counter(s) == Counter(t)
        # time com is O(n)
