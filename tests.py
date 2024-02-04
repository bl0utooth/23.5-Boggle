import unittest
from boggle import BoggleGame

class TestBoggleGame(unittest.TestCase):

    def setUp(self):
        self.boggle_game = BoggleGame()

    def test_board_generation(self):
        self.assertEqual(len(self.boggle_game.board), self.boggle_game.BOARD_SIZE)
        for row in self.boggle_game.board:
            self.assertEqual(len(row), self.boggle_game.BOARD_SIZE)

    def test_word_validation_valid(self):
        valid_word = "python"
        self.assertTrue(self.boggle_game.is_valid_word(valid_word))

    def test_word_validation_invalid(self):
        invalid_word = "invalid"
        self.assertFalse(self.boggle_game.is_valid_word(invalid_word))

    def test_word_score(self):
        word = "python"
        expected_score = len(word) - self.boggle_game.MIN_WORD_LENGTH + 1
        self.assertEqual(self.boggle_game.calculate_score(word), expected_score)

    def test_word_score_invalid(self):
        invalid_word = "invalid"
        self.assertEqual(self.boggle_game.calculate_score(invalid_word), 0)

    def test_word_path(self):
        word = "python"
        path = self.boggle_game.find_word_path(word)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), len(word))

if __name__ == '__main__':
    unittest.main()
