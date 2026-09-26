import unittest
import os

class TestOperacaoBoliviana(unittest.TestCase):
    
    def setUp(self):
        # Lê o conteúdo do HTML antes de cada teste
        with open('index.html', 'r', encoding='utf-8') as f:
            self.html_content = f.read()

    # Teste 1: Verifica se o arquivo da aplicação existe
    def test_arquivo_existe(self):
        self.assertTrue(os.path.exists('index.html'))

    # Teste 2: Verifica o título da missão
    def test_titulo_missao(self):
        self.assertIn('Operação', self.html_content)

    # Teste 3: Verifica o local de operação
    def test_localizacao(self):
        self.assertIn('Bolívia', self.html_content)

    # Teste 4: Verifica o alvo principal
    def test_alvo_principal(self):
        self.assertIn('El Sueño', self.html_content)

    # Teste 5: Verifica a estrutura básica do código
    def test_estrutura_html(self):
        self.assertIn('<!DOCTYPE html>', self.html_content)

if __name__ == '__main__':
    unittest.main()
