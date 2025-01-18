import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrei = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    def tearDownClass(self):
        for key, value in self.all_results.items():
            print(f'{key}: {value}')

    def test_1(self):
        tournament = runner_and_tournament.Tournament(90, [self.usain, self.nik])
        result = tournament.start()
        self.all_results[0] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_2(self):
        tournament = runner_and_tournament.Tournament(90, [self.andrei, self.nik])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_3(self):
        tournament = runner_and_tournament.Tournament(90, [self.usain, self.andrei, self.nik])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

if __name__ == "__main__":
    unittest.main()
