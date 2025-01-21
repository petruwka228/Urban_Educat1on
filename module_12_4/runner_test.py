from rt_with_exceptions import Runner
import unittest
import logging
import tests_12_4

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_walk = Runner("TestRunnerWalk")
            for i in range(10):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_run = Runner("TestRunnerRun")
            for i in range(10):
                runner_run.run()
            self.assertEqual(runner_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

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
