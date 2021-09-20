import camelCase
import unittest


class TestCamelCase(unittest.TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('hello', camelCase.to_camel_case('Hello'))
        self.assertEqual('hello', camelCase.to_camel_case('☘️🌺🍎Hello☘️'))
        self.assertEqual(
            'helloWorld', camelCase.to_camel_case('HeLLO WorLD'))
        self.assertEqual('helloWorld', camelCase.to_camel_case('Hello World'))
        self.assertEqual(
            'helloWorld', camelCase.to_camel_case(' Hello World '))


if __name__ == '__main__':
    unittest.main()
