import unittest

# Découvre tous les fichiers de test dans src/
suite = unittest.defaultTestLoader.discover('src', pattern='test_*.py')

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
