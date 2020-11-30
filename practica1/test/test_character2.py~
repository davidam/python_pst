#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from app.root import Root
from app.character2 import Character2

class TddInPythonExample(unittest.TestCase):

    def test_init(self):
        ch = Character2(25,52)
        self.assertEqual(ch.hp, 25)
        self.assertEqual(ch.dmg, 52)
        self.assertTrue(ch.is_alive())
