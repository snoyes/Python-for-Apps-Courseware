import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        bot = BodyOfText('')
        self.assertEqual(0, bot.num_paragraphs())
    def test_single_paragraph(self):
        bot = BodyOfText('Hello, world.')
        self.assertEqual(1, bot.num_paragraphs())
    def test_several_paragraphs(self):
        bot = BodyOfText('''This is a longer story.

Once upon a time, there was a princess in a castle.

She grew up to be a famous dancer.''')
        self.assertEqual(3, bot.num_paragraphs())

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
