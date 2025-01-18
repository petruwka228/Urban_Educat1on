import runner_test
import TournamentTest
import unittest

suite = unittest.TestSuite()

suite.addTest(runner_test.RunnerTest('test_challenge'))
suite.addTest(runner_test.RunnerTest('test_run'))
suite.addTest(runner_test.RunnerTest('test_walk'))
suite.addTest(TournamentTest.TournamentTest('test_1'))
suite.addTest(TournamentTest.TournamentTest('test_2'))
suite.addTest(TournamentTest.TournamentTest('test_3'))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite)
