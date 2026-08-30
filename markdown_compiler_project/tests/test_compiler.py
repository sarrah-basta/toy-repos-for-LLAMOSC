import unittest
from compiler.compiler import MarkdownCompiler

class TestMarkdownCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = MarkdownCompiler()
        
    def test_headers(self):
        self.assertEqual(self.compiler.compile('# Hello'), '<h1>Hello</h1>')
        self.assertEqual(self.compiler.compile('## Subheader'), '<h2>Subheader</h2>')
        
    def test_inline(self):
        self.assertEqual(self.compiler.compile('This is **bold** text.'), '<p>This is <strong>bold</strong> text.</p>')
        self.assertEqual(self.compiler.compile('This is *italic* text.'), '<p>This is <em>italic</em> text.</p>')
