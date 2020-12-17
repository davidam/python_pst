#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.


import unittest
from app.character import Character
from app.game import Game
from app.worker import Worker
from app.enemy import PartialExam

class TddInPythonExample(unittest.TestCase):

    def test_init(self):
        g = Game()
        self.assertEqual(g.turn, 0)
        self.assertEqual(g.level, 0)
        self.assertEqual(g.list_enemies, [])
        self.assertEqual(g.list_characters, [])                        
        
    def test_initialize_enemy(self):
        g = Game()
        self.assertEqual(len(g.initialize_enemies()), 4)
        
    def test_attack_1to1(self):
        g = Game()
        one = PartialExam()
        uno = Worker()
        before = uno.hp
        g.attack(one, uno)
        self.assertTrue(before > uno.hp)
