import time
#import glob
import json
import unittest
#import pandas as pd
import os
#import xml.etree.ElementTree as ET
#from extract_lexicons import extract_lexicons_fun
#from generate_skos import generate_skos_fun
#from Tests.Integration.extract_skosfile import skos_extraction_fun


#import json
#import os
#import sys
#import pytest
#import subprocess
#import coverage
#import site
#import re

class TestExtractSkosExport(unittest.TestCase):
    def test_add(self):
        a=7+3
        self.assertEqual(a, 10) 

    def test_mul(self):
        b=3*7
        self.assertEqual(b, 21) 
    
    def test_mul1(self):
        b=7*7
        self.assertEqual(b, 49)

    def test_mul2(self):
        b=5*7
        self.assertEqual(b, 35)  

    def test_mul3(self):
        b=6*7
        self.assertEqual(b, 42)  



if __name__ == '__main__':
    unittest.main()