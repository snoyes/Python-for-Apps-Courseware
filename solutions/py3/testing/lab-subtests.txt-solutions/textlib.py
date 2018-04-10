class BodyOfText:
    def __init__(self, text):
        if text == '':
            raise ValueError
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')
    def paragraphs(self):
        return []
    def wordcounts(self):
        counts = {}
        for chunk in self.text.strip().split():
            word = chunk.lower().rstrip('.,;:')
            try:
                counts[word] += 1
            except KeyError:
                counts[word] = 1
        return counts

class Paragraph:
    def __init__(self, text):
        self.text = text
    def num_sentences(self):
        if self.text == '':
            return 0
        return 1 + self.text.replace('\n', ' ').count('. ')
    

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
