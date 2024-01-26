import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    # Run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(suite)