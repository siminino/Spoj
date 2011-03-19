from codigo import life_main
from unittest import TestCase
import unittest

class TestLifeUniverseEverything(TestCase):
    def test_mostra_o_primeiro_numero(self):
        self.assertTrue('1' in life_main())
        self.assertTrue('2' in life_main())
        self.assertTrue('4' in life_main())
        self.assertTrue('6' in life_main())
        self.assertTrue('28' in life_main())
        self.assertTrue('42' in life_main())
        
    def test_verifica_se_numero_errado_aparece(self):
        self.assertFalse('3' in life_main())
        
    def test_verifica_se_numero_errado_com_dois_numeros_aparece(self):
        self.assertFalse('21' in life_main()) 
        
    def test_veridica_se_88_aparece(self):
        self.assertFalse('88' in life_main())
        
    
    
        
unittest.main()
