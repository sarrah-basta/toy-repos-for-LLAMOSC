import re

class MarkdownCompiler:
    def __init__(self):
        pass
        
    def compile(self, text):
        lines = text.split('\n')
        html_lines = []
        
        for line in lines:
            line = self._parse_inline(line)
            if line.startswith('# '):
                html_lines.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                html_lines.append(f'<h2>{line[3:]}</h2>')
            else:
                html_lines.append(f'<p>{line}</p>')
                
        return '\n'.join(html_lines)
        
    def _parse_inline(self, text):
        # Basic bold and italic
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text
