import re

def vowel_counter(sentence): 
    vowels = re.findall('[aeiouAEIOU]', sentence)
    print('Number of vowels:', len(vowels))


