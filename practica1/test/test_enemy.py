#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from app.enemy import *

class TddInPythonExample(unittest.TestCase):

    def test_enemy(self):
        e = Enemy(0,0)
        self.assertEqual(e.hp, 0)
        self.assertEqual(e.dmg, 0)
        self.assertTrue(e.is_alive())

    def test_partialexam(self):
        pe = PartialExam(12,35)
        self.assertEqual(pe.hp, 12)
        self.assertEqual(pe.dmg, 35)
        
