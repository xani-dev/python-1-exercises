import re

def vowel_counter(sentence): 
    vowels = re.findall('[aeiouAEIOU]', sentence)
    print(f'Number of vowels in {sentence}: ', len(vowels))


