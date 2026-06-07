import ast

class CodeChecker:
    def __init__(self):
        self.feedback = []

    def analyze(self, code):
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return [f"Syntax Error: {e}"]

        defined = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.Name):
                if isinstance(n.ctx, ast.Store):
                    defined.add(n.id)
                elif isinstance(n.ctx, ast.Load) and n.id not in defined:
                    self.feedback.append(f"'{n.id}' may be undefined.")

        for i, line in enumerate(code.splitlines(), 1):
            s = line.strip()
            if s.startswith("#") and (len(s) == 1 or s[1] != " "):
                self.feedback.append(f"Bad comment on line {i}")

        return self.feedback

code = """
def add(a, b):
    result = a + b
    print(result)
"""

for msg in CodeChecker().analyze(code):
    print(msg)