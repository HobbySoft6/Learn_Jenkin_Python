import json
import os
import sys
 #import pytest
import subprocess
#import coverage
import site
import re

def test_add():
    a=7+3
    assert a==7

def test_mul():
    b=3*7
    assert b==21 