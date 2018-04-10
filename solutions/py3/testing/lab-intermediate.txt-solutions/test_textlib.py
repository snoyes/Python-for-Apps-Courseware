import unittest
from textlib import BodyOfText, Paragraph

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText('')
    def test_single_paragraph(self):
        bot = BodyOfText('Hello, world.')
        self.assertEqual(1, bot.num_paragraphs())
    def test_several_paragraphs(self):
        bot = BodyOfText('''This is a longer story.

Once upon a time, there was a princess in a castle.

She grew up to be a famous dancer.''')
        self.assertEqual(3, bot.num_paragraphs())

class TestParagraph(unittest.TestCase):
    def test_empty_paragraph(self):
        para = Paragraph('')
        self.assertEqual(0, para.num_sentences())
    def test_single_sentence(self):
        para = Paragraph('This is a paragraph with one sentence.')
        self.assertEqual(1, para.num_sentences())
    def test_three_sentences(self):
        para = Paragraph('''This is a paragraph. It has several sentences.
Three, in fact.''')
        self.assertEqual(3, para.num_sentences())
    

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
