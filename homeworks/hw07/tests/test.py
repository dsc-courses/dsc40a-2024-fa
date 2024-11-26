import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from hw7code import *
import babypandas as bpd
import numpy as np

popular = bpd.read_csv('popular.csv').set_index('name')

comics = bpd.read_csv('comics.csv').set_index('name')

custom = bpd.read_csv('custom.csv').set_index('name')


class Test(unittest.TestCase):

    @weight(1)
    @visibility('after_published')
    def test_1(self):
        """Part (b) test case 1"""
        self.assertTrue(predict_align(comics, "Public Identity", "Female Characters", "Living Characters", "DC") in ['Good Characters', 'Bad Characters'])

    @weight(2)
    @visibility('after_published')
    def test_2(self):
        """Part (b) test case 2"""
        popular_results = np.array([])
        for identity in ["Public Identity", "Secret Identity"]:
            for sex in  ["Male Characters", "Female Characters"]:
                for alive in ["Living Characters", "Deceased Characters"]:
                    for company in ["DC", "Marvel"]:
                        popular_results = np.append(popular_results, predict_align(popular, identity, sex, alive, company))
        self.assertTrue(np.all(popular_results=='Good Characters'))

    @weight(2)
    @visibility('after_published')
    def test_3(self):
        """Part (b) test case 3"""
        comics_results = np.array([])
        for identity in ["Public Identity", "Secret Identity"]:
            for sex in  ["Male Characters", "Female Characters"]:
                for alive in ["Living Characters", "Deceased Characters"]:
                    for company in ["DC", "Marvel"]:
                        comics_results = np.append(comics_results, predict_align(comics, identity, sex, alive, company))
        self.assertTrue(np.all(comics_results==['Good Characters', 'Good Characters', 'Bad Characters',
       'Bad Characters', 'Good Characters', 'Good Characters',
       'Good Characters', 'Good Characters', 'Bad Characters',
       'Bad Characters', 'Bad Characters', 'Bad Characters',
       'Good Characters', 'Good Characters', 'Bad Characters',
       'Bad Characters']))

    @weight(2)
    @visibility('after_published')
    def test_4(self):
        """Part (b) test case 4"""
        custom_results = np.array([])
        for identity in ["Public Identity", "Secret Identity"]:
            for sex in  ["Male Characters", "Female Characters"]:
                for alive in ["Living Characters", "Deceased Characters"]:
                    for company in ["DC", "Marvel"]:
                        custom_results = np.append(custom_results, predict_align(custom, identity, sex, alive, company))
        self.assertTrue(np.all(custom_results== ['Good Characters', 'Neutral Characters', 'Bad Characters',
       'Neutral Characters', 'Good Characters', 'Neutral Characters',
       'Neutral Characters', 'Neutral Characters', 'Bad Characters',
       'Neutral Characters', 'Bad Characters', 'Neutral Characters',
       'Good Characters', 'Neutral Characters', 'Bad Characters',
       'Neutral Characters']))

 