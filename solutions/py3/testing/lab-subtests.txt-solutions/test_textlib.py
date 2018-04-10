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

    def test_wordcounts(self):
        testitems = [
            {'text' : 'This is a sentence.',
             'counts' : {'this': 1, 'is': 1, 'a': 1, 'sentence': 1},
            },
            {'text': 'Truth is beauty; beauty, truth.',
             'counts': {'truth': 2, 'beauty': 2, 'is': 1},
             },
            {'text': 'I could finally SEE. But what I could see, remained a mystery.',
             'counts': {'i': 2, 'could': 2, 'finally': 1, 'see': 2,
                        'but': 1, 'what': 1, 'remained': 1, 'a': 1, 'mystery': 1},
             },
            ]
        for testitem in testitems:
            with self.subTest(text=testitem['text'], counts=testitem['counts']):
                body = BodyOfText(testitem['text'])
                self.assertEqual(testitem['counts'], body.wordcounts())
        # NOTE: You could also use keyword argument unpacking, e.g.:
        #   with self.subTest(**testitem):
        # Sign up for "Python - The Next Level" to learn about that.

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
