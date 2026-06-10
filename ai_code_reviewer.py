import ast

class CodeChecker:
    def __init__(self):
        self.feedback = []

    def analyze(self, code):
        self.feedback.clear()

        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            self.feedback.append(f"Syntax Error: {e}")
            return

        self.check_functions(tree)
        self.check_classes(tree)
        self.check_variables(tree)
        self.check_imports(tree)
        self.check_comments(code)
        self.check_line_length(code)
        self.check_todos(code)
        self.check_blank_lines(code)

    def check_functions(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    self.feedback.append(
                        f"Function '{node.name}' has no docstring."
                    )

                if len(node.body) > 20:
                    self.feedback.append(
                        f"Function '{node.name}' is very long."
                    )

                if len(node.args.args) > 5:
                    self.feedback.append(
                        f"Function '{node.name}' has many parameters."
                    )

    def check_classes(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if not ast.get_docstring(node):
                    self.feedback.append(
                        f"Class '{node.name}' has no docstring."
                    )

    def check_variables(self, tree):
        defined = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    defined.add(node.id)

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Load):
                    if node.id not in defined and node.id not in dir(__builtins__):
                        self.feedback.append(
                            f"Variable '{node.id}' may be undefined."
                        )

    def check_imports(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.feedback.append(
                        f"Imported module: {alias.name}"
                    )

            elif isinstance(node, ast.ImportFrom):
                self.feedback.append(
                    f"Imported from module: {node.module}"
                )

    def check_comments(self, code):
        for i, line in enumerate(code.splitlines(), 1):
            s = line.strip()

            if s.startswith("#"):
                if len(s) == 1:
                    self.feedback.append(
                        f"Empty comment on line {i}"
                    )

                elif len(s) > 1 and s[1] != " ":
                    self.feedback.append(
                        f"Comment formatting issue on line {i}"
                    )

    def check_line_length(self, code):
        for i, line in enumerate(code.splitlines(), 1):
            if len(line) > 79:
                self.feedback.append(
                    f"Line {i} exceeds 79 characters."
                )

    def check_todos(self, code):
        for i, line in enumerate(code.splitlines(), 1):
            if "TODO" in line.upper():
                self.feedback.append(
                    f"TODO found on line {i}"
                )

    def check_blank_lines(self, code):
        blank = 0

        for i, line in enumerate(code.splitlines(), 1):
            if line.strip() == "":
                blank += 1
            else:
                blank = 0

            if blank > 2:
                self.feedback.append(
                    f"Too many blank lines near line {i}"
                )

    def get_feedback(self):
        return self.feedback
# Minor update 5621

# Minor update 6960

# Minor update 3393

# Minor update 4451

# Minor update 5549

# Minor update 4518

# Minor update 5055

# Minor update 1357

# Minor update 3591

# Minor update 6420

# Minor update 9646

# Minor update 4716

# Minor update 1280

# Minor update 5486
