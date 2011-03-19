from codigo import life_main
from unittest import TestCase
import unittest

class TestLifeUniverseEverything(TestCase):
    def test_mostra_os_numeros_devem_ser_exibidos(self):
        self.assertTrue('1' in life_main())
        self.assertTrue('2' in life_main())
        self.assertTrue('88' in life_main())
        
    def test_verifica_se_numero_42_aparece(self):
        self.assertFalse('42' in life_main())
        
    def test_veridica_se_99_aparece(self):
        self.assertFalse('99' in life_main())
        
    
    
        
unittest.main()
