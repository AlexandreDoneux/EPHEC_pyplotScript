import unittest

#from main_pyplot_script import clean_lines, group_figures, LineSyntaxError
from test_functions import clean_lines, group_figures, LineSyntaxError
# Besoin de créer un fichier avec les fonctions séparées de argparse car problème  -> chercher pourquoi


class TestCleanLines(unittest.TestCase):
    def test_clean_lines_1(self):
        initial_lines = ["\n", "\n", "P1 2 7\n", "P2 21 2\n", "P3 2 4\n", "\n", "\n", "\n", "P4 3 3\n", "P5 9 5\n",
                         "\n", "\n", "P6 22 1\n", "\n"]
        excepected = ["", "P1 2 7", "P2 21 2", "P3 2 4", "", "P4 3 3", "P5 9 5", "", "P6 22 1", ""]
        self.assertEqual(excepected, clean_lines(initial_lines))

    def test_clean_lines_2(self):
        initial_lines = ["P1 3 4\n", "\n", "\n", "\n", "\n", "P2 3 8\n", "\n", "\n", "P3 8 5\n", "P3 8 5\n"]
        excepected = ["P1 3 4", "", "P2 3 8", "", "P3 8 5"]
        self.assertEqual(excepected, clean_lines(initial_lines))

    def test_clean_lines_3(self):
        initial_lines = ["\n", "\n", "P1 67 87", "P1 67 87", "P1 67 87", "P2 3 4", "\n"]
        excepected = ["", "P1 67 87", "P2 3 4", ""]
        self.assertEqual(excepected, clean_lines(initial_lines))

    def test_clean_lines_all_empty(self):
        initial_lines = ["\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",]
        excepected = [""]
        self.assertEqual(excepected, clean_lines(initial_lines))

    def test_clean_lines_all_same(self):
        initial_lines = ["P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", ]
        excepected = ["P1 3 4", ]
        self.assertEqual(excepected, clean_lines(initial_lines))

    def test_clean_lines_empty(self):
        initial_lines = []
        excepected = []
        self.assertEqual(excepected, clean_lines(initial_lines))

    # Pas vraiment d'autres cas. Vu qu'on lis d'un fichier on aura tout le temps des tring dans la liste de départ


class TestGroupFigures(unittest.TestCase):
    def test_group_figures_1(self):
        initial_lines = ["\n", "\n", "P1 2 7\n", "P2 21 2\n", "P3 2 4\n", "\n", "\n", "\n", "P4 3 3\n", "P5 9 5\n",
                         "\n", "\n", "P6 22 1\n", "\n"]
        excepected = [["P1 2.0 7.0", "P2 21.0 2.0", "P3 2.0 4.0"], ["P4 3.0 3.0", "P5 9.0 5.0"], ["P6 22.0 1.0"]]
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_2(self):
        initial_lines = ["P1 3 4\n", "\n", "\n", "\n", "\n", "P2 3 8\n", "\n", "\n", "P3 8 5\n", "P3 8 5\n"]
        excepected =[["P1 3.0 4.0"], ["P2 3.0 8.0"], ["P3 8.0 5.0"]]
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_3(self):
        initial_lines = ["\n", "\n", "P1 67 87", "P1 67 87", "P1 67 87", "P2 3 4", "\n"]
        excepected = [["P1 67.0 87.0", "P2 3.0 4.0"]]
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_all_empty(self):
        initial_lines = ["\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",]
        excepected = []
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_all_same(self):
        initial_lines = ["P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", "P1 3 4\n", ]
        excepected = [["P1 3.0 4.0"]]
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_empty(self):
        initial_lines = []
        excepected = []
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_float(self):
        initial_lines = ["\n", "\n", "P1 2.4 7\n", "P2 21 2\n", "P3 2 4.88\n", "\n", "\n", "\n", "P4 3 3.1\n", "P5 9 5\n",
                         "\n", "\n", "P6 22.09 1\n", "\n"]
        excepected = [["P1 2.4 7.0", "P2 21.0 2.0", "P3 2.0 4.88"], ["P4 3.0 3.1", "P5 9.0 5.0"], ["P6 22.09 1.0"]]
        self.assertEqual(excepected, group_figures(initial_lines)[0])

    def test_group_figures_non_float_error(self):
        """
        Teste le renvoi de l'erreur LineSyntaxError lorsqu'une des coordonnées dans une ligne n'est pas un nombre.
        """
        initial_lines = ["\n", "\n", "P1 2 7\n", "P2 t 2\n", "P3 2 4\n", "\n", "\n", "\n", "P4 3 3\n", "P5 9 5\n",
                         "\n", "\n", "P6 22 1\n", "\n"]
        self.assertRaises(LineSyntaxError)

    def test_group_figures_too_much_per_line(self):
        """
        Teste le renvoi de l'erreur LineSyntaxError lorsqu'une des lignes possède trop d'arguments.
        """
        initial_lines = ["\n", "\n", "P1 2 7\n", "P2 21 2 5\n", "P3 2 4\n", "\n", "\n", "\n", "P4 3 3\n", "P5 9 5\n",
                         "\n", "\n", "P6 22 1\n", "\n"]
        self.assertRaises(LineSyntaxError)






