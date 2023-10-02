import unittest
from mbsite import age,names,secondnames,lastnames, rain, month, uvlech

class TestSite(unittest.TestCase):

    def test_string(self):
        self.assertEqual(age("1"), 1)
        self.assertEqual(age("-2"), "That's wrong")
        self.assertEqual(age(" "), "That's wrong")
        self.assertEqual(age("#"), "That's wrong")
        self.assertEqual(age("121"), "That's wrong")
        self.assertEqual(age("mathematic"), "That's wrong")
        self.assertEqual(age(1.2), "That's wrong")

    def test_rain(self):
        self.assertEqual(rain(" "), "That's wrong")
        self.assertEqual(rain("Выключаю дождь"), "That's wrong")

    def test_uvlech(self):
        self.assertEqual(uvlech("Ничего"), "Ничего")
        self.assertEqual(uvlech(" "), "That's wrong")

    def month(self):
        self.assertEqual(month("Октябрь"), "Октябрь")
        self.assertEqual(month("октябрь"), "Октябрь")
        self.assertEqual(month("октрь"), "That's wrong")

    def test_names(self):
        self.assertEqual(names("Даниил"), "Даниил")
        self.assertEqual(names(1.2), "That's wrong")
        self.assertEqual(names(" "), "That's wrong")

    def test_secondname(self):
        self.assertEqual(secondnames("Ануфриев"), "Ануфриев")
        self.assertEqual(secondnames(1.2), "That's wrong")
        self.assertEqual(secondnames(" "), "That's wrong")

    def test_lastnames(self):
        self.assertEqual(lastnames("Олегович"), "Олегович")
        self.assertEqual(lastnames(1.2), "That's wrong")
        self.assertEqual(lastnames(" "), "That's wrong")