#!/usr/bin/env python3

# lib/my_string.py
class MyString:
    def __init__(self, value=''):
        self.value = value
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    value = property(get_value, set_value)
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace multiple punctuation marks with a single period
        text = self.value.replace('!!', '.').replace('!?', '.').replace('?!', '.').replace('...', '.')
        # Split on any punctuation mark (., ?, !)
        sentences = [s.strip() for s in text.replace('?', '.').replace('!', '.').split('.')]
        # Filter out empty or whitespace-only strings
        sentences = [s for s in sentences if s]
        return len(sentences)