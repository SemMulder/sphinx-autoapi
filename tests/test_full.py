import os
import shutil
import subprocess as sp
import unittest

__author__ = 'swenson'


class FullPythonTests(unittest.TestCase):

    def test_full_py(self):
        os.chdir('tests/pyexample')
        try:
            if os.path.exists('_build'):
                shutil.rmtree('_build')
            os.mkdir('_build')
            sp.check_call('sphinx-build -b text -d ./.doctrees . _build/text', shell=True)

            with open('_build/text/autoapi/example/index.txt') as fin:
                text = fin.read().strip()
            self.assertEquals(text, '''example
*******


Function
========

   example.example_function()

      Compute the square root of x and return it.''')

        finally:
            os.chdir('../..')


class FullJavaScriptTests(unittest.TestCase):

    def test_full_js(self):
        os.chdir('tests/jsexample')
        try:
            if os.path.exists('_build'):
                shutil.rmtree('_build')
            os.mkdir('_build')
            sp.check_call('sphinx-build -b text -d ./.doctrees . _build/text', shell=True)

            with open('_build/text/autoapi/Circle/index.txt') as fin:
                text = fin.read().strip()
                self.assertIn('Creates an instance of Circle', text)
        finally:
            os.chdir('../..')
