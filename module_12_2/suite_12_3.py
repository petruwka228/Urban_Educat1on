import runner_test
import TournamentTest
import unittest

suite = unittest.TestSuite()

suite.addTest(runner_test.RunnerTest('test_challenge'))
suite.addTest(runner_test.RunnerTest('test_run'))
suite.addTest(runner_test.RunnerTest('test_walk'))
suite.addTest(TournamentTest.TournamentTest('test_first_tournament'))
suite.addTest(TournamentTest.TournamentTest('test_second_tournament'))
suite.addTest(TournamentTest.TournamentTest('test_third_tournament'))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite)

