class BodyOfText:
    def __init__(self, text):
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')
    def paragraphs(self):
        return []

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
