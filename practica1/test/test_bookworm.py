#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from app.character import Character
from app.bookworm import Bookworm

class TddInPythonExample(unittest.TestCase):

    def test_init(self):
        player = Bookworm()
        self.assertEqual(player.hp, 25)
        self.assertEqual(player.dmg, 9)
#        self.assertEqual(player.__str__(), "Skill: Una vez cada 4 rondas puede resucitar a otro jugador que haya perdido todos los puntos de vida.\nSi se utiliza la habilidad y no hay ningún jugador sin puntos de vida no cuenta como usada.")   
        
