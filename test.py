import unittest
import re

target = __import__("mini-grep")
search = target.search
compile_regex = target.compile_regex

class TestSearchFunction(unittest.TestCase):

    def test_long_file(self):
        self.assertEqual(
            search('./test_texts/bible', '\\svile\\s', True),
            [
            '17965 should seem vile unto thee.', 
            '23098 good unto you: but unto this man do not so vile a thing.', 
            '27241 6:22 And I will yet be more vile than thus, and will be base in mine', 
            '44399 18:3 Wherefore are we counted as beasts, and reputed vile in your', 
            '46458 15:4 In whose eyes a vile person is contemned; but he honoureth them', 
            '58899 32:5 The vile person shall be no more called liberal, nor the churl', 
            '58902 32:6 For the vile person will speak villany, and his heart will work', 
            '63807 them like vile figs, that cannot be eaten, they are so evil.', 
            '72543 11:21 And in his estate shall stand up a vile person, to whom they', 
            '90483 1:26 For this cause God gave them up unto vile affections: for even', 
            '94578 Christ: 3:21 Who shall change our vile body, that it may be fashioned', 
            '96960 goodly apparel, and there come in also a poor man in vile raiment; 2:3'
            ]
            )

    def test_non_english_file(self):
        self.assertEqual(search('./test_texts/tadeusz', '\\sbudową,\\s', True),
                         ['398 Okazały budową, poważny ogromem,'])

    def test_quiet(self):
        self.assertEqual(search('./test_texts/tadeusz', '\\sbudową,\\s', False),
                         ['Okazały budową, poważny ogromem,'])

    def no_occcurence_found(self):
        self.assertEqual(search('./test_texts/bible', '\\sgyatt\\s', False),
                         ['No occurencce of PATTERN found in file.'])

    def test_file_not_found(self):
        self.assertEqual(search('./test_texts/boble', '\\sGod\\s', False),
                         ['Error: File not found'])
         
    def test_incorrect_regex(self):
        self.assertIsNot(compile_regex('\\Jskdf'), re.Pattern)
        self.assertIsNot(compile_regex(')aeiou'), re.Pattern)

if __name__ == '__main__':
    unittest.main()
