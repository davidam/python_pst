#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from app.root import Root

class TddInPythonExample(unittest.TestCase):

    def test_init(self):
        ch = Root(25,52)
        self.assertEqual(ch.hp, 25)
        self.assertEqual(ch.dmg, 52)
        self.assertTrue(ch.is_alive())
