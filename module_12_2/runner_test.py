from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_walk = Runner("TestRunnerWalk")
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_run = Runner("TestRunnerRun")
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner("TestRunner1")
        runner_2 = Runner("TestRunner2")
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
        
if __name__ == "__main__":
    unittest.main()