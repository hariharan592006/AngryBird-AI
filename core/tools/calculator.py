import ast
import operator


class Calculator:

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    def calculate(self, expression: str):

        try:

            node = ast.parse(expression, mode="eval").body

            return self._evaluate(node)

        except Exception:

            return "Invalid expression."

    def _evaluate(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)

            right = self._evaluate(node.right)

            operator_type = type(node.op)

            if operator_type not in self.OPERATORS:
                raise ValueError("Unsupported operator")

            return self.OPERATORS[operator_type](left, right)

        raise ValueError("Unsupported expression")