# INTEL CORPORATION CONFIDENTIAL AND PROPRIETARY
#
# Copyright © 2021-2022 Intel Corporation.
#
# This software and the related documents are Intel copyrighted
# materials, and your use of them is governed by the express
# license under which they were provided to you (License). Unless
# the License provides otherwise, you may not use, modify, copy,
# publish, distribute, disclose or transmit  this software or the
# related documents without Intel's prior written permission.
#
# This software and the related documents are provided as is, with
# no express or implied warranties, other than those that are
# expressly stated in the License.

import unittest

from lava.magma.core.learning.symbolic_equation import *


class TestSymbolList(unittest.TestCase):
    def test_append(self) -> None:
        y1, _ = Variable.find("y1")
        addition, _ = Addition.find("+")
        literal, _ = Literal.find("2")
        list_of_symbols = [y1, addition, literal]

        symbol_list = SymbolList()
        symbol_list.append(y1)
        symbol_list.append(addition)
        symbol_list.append(literal)

        self.assertIsInstance(symbol_list, SymbolList)

        for idx, symbol in enumerate(symbol_list.list):
            self.assertEqual(symbol, list_of_symbols[idx])

    def test_str(self) -> None:
        y1, _ = Variable.find("y1")
        addition, _ = Addition.find("+")
        literal, _ = Literal.find("2")
        str_output = f"[{y1}, {addition}, {literal}]"

        symbol_list = SymbolList()
        symbol_list.append(y1)
        symbol_list.append(addition)
        symbol_list.append(literal)

        self.assertEqual(symbol_list.__str__(), str_output)

    def test_nested_bracket_str(self) -> None:
        y1, _ = Variable.find("y1")
        addition, _ = Addition.find("+")

        bracket_expr, _ = BracketExpression.find("(w - 2)")
        w, _ = Variable.find("w")
        subtraction, _ = Subtraction.find("-")
        literal, _ = Literal.find("2")
        sub_symbol_list = SymbolList()
        sub_symbol_list.append(w)
        sub_symbol_list.append(subtraction)
        sub_symbol_list.append(literal)
        bracket_expr.symbol_list = sub_symbol_list

        str_output = f"[{y1}, {addition}, " \
                     f"BracketExpression([{w}, {subtraction}, {literal}])]"

        symbol_list = SymbolList()
        symbol_list.append(y1)
        symbol_list.append(addition)
        symbol_list.append(bracket_expr)

        self.assertEqual(symbol_list.__str__(), str_output)

    def test_nested_sgn_str(self) -> None:
        y1, _ = Variable.find("y1")
        addition, _ = Addition.find("+")

        sgn_expr, _ = SgnExpression.find("sgn(w - 2)")
        w, _ = Variable.find("w")
        subtraction, _ = Subtraction.find("-")
        literal, _ = Literal.find("2")
        sub_symbol_list = SymbolList()
        sub_symbol_list.append(w)
        sub_symbol_list.append(subtraction)
        sub_symbol_list.append(literal)
        sgn_expr.symbol_list = sub_symbol_list

        str_output = f"[{y1}, {addition}, " \
                     f"SgnExpression([{w}, {subtraction}, {literal}])]"

        symbol_list = SymbolList()
        symbol_list.append(y1)
        symbol_list.append(addition)
        symbol_list.append(sgn_expr)

        self.assertEqual(symbol_list.__str__(), str_output)


class TestAddition(unittest.TestCase):
    def test_addition_present(self) -> None:
        expr = "+"

        symbol, remaining_expr = Addition.find(expr)

        self.assertIsInstance(symbol, Addition)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_addition_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Addition.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestSubtraction(unittest.TestCase):
    def test_subtraction_present(self) -> None:
        expr = "-"

        symbol, remaining_expr = Subtraction.find(expr)

        self.assertIsInstance(symbol, Subtraction)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_subtraction_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Subtraction.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestMultiplication(unittest.TestCase):
    def test_multiplication_present(self) -> None:
        expr = "*"

        symbol, remaining_expr = Multiplication.find(expr)

        self.assertIsInstance(symbol, Multiplication)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_multiplication_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Multiplication.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestX0(unittest.TestCase):
    def test_x0_present(self) -> None:
        expr = "x0"

        symbol, remaining_expr = X0.find(expr)

        self.assertIsInstance(symbol, X0)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_x0_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = X0.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestY0(unittest.TestCase):
    def test_y0_present(self) -> None:
        expr = "y0"

        symbol, remaining_expr = Y0.find(expr)

        self.assertIsInstance(symbol, Y0)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_y0_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Y0.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestUk(unittest.TestCase):
    def test_u5_present(self) -> None:
        expr = "u5"

        symbol, remaining_expr = Uk.find(expr)

        self.assertIsInstance(symbol, Uk)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.decimate_exponent, 5)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_only_u_present(self) -> None:
        expr = "u"

        symbol, remaining_expr = Uk.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "u")

    def test_uk_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Uk.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestVariable(unittest.TestCase):
    def test_x_traces_present(self) -> None:
        expr = "x1"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "x2"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_y_traces_present(self) -> None:
        expr = "y1"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "y2"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "y3"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_synaptic_variables_present(self) -> None:
        expr = "w"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "d"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "t"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsInstance(symbol, Variable)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_nothing_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Variable.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestBracketExpression(unittest.TestCase):
    def test_bracket_expression_present(self) -> None:
        sub_expr = "w + 3"
        expr = f"({sub_expr})"

        symbol, remaining_expr = BracketExpression.find(expr)

        self.assertIsInstance(symbol, BracketExpression)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(sub_expr, symbol.sub_expr)
        self.assertEqual(remaining_expr, "")

    def test_missing_closing_bracket(self) -> None:
        sub_expr = "w + 3"
        expr = f"({sub_expr}"

        with self.assertRaises(ValueError):
            BracketExpression.find(expr)

    def test_bracket_expression_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = BracketExpression.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestSgnExpression(unittest.TestCase):
    def test_sgn_expression_present(self) -> None:
        sub_expr = "w + 3"
        expr = f"sgn({sub_expr})"

        symbol, remaining_expr = SgnExpression.find(expr)

        self.assertIsInstance(symbol, SgnExpression)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(sub_expr, symbol.sub_expr)
        self.assertEqual(remaining_expr, "")

    def test_missing_closing_bracket(self) -> None:
        sub_expr = "w + 3"
        expr = f"sgn({sub_expr}"

        with self.assertRaises(ValueError):
            SgnExpression.find(expr)

    def test_bracket_expression_not_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = SgnExpression.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestLiteral(unittest.TestCase):
    def test_x2y_present(self):
        expr = "1*2^3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(8, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "+2*2^-3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        # CHECK THIS!!
        self.assertEqual(0, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "-3*2^+3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(-24, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_2y_present(self):
        expr = "2^3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(8, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "+2^-3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        # CHECK THIS!!
        self.assertEqual(0, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "-2^+3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(-8, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_x_present(self):
        expr = "1"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(1, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "+2"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(2, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

        expr = "-3"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsInstance(symbol, Literal)
        self.assertEqual(expr, symbol.expr)
        self.assertEqual(remaining_expr, "")
        self.assertEqual(-3, symbol.val)
        self.assertEqual(symbol.__str__(),
                         symbol.__class__.__name__ + f"({expr})")

    def test_nothing_present(self) -> None:
        expr = "n"

        symbol, remaining_expr = Literal.find(expr)

        self.assertIsNone(symbol)
        self.assertEqual(remaining_expr, "n")


class TestSymbolicEquation(unittest.TestCase):
    def test_symbolic_equation(self) -> None:
        target = "dw"
        str_learning_rule = 'x0*(-1)*2^-1*y1 + y0*1*2^1*x1'
        str_output = "[X0(x0), Multiplication(*), " \
                     "BracketExpression([Subtraction(-), Literal(1)])," \
                     " Multiplication(*), Literal(2^-1), Multiplication(*)," \
                     " Variable(y1), Addition(+), Y0(y0), Multiplication(*)," \
                     " Literal(1*2^1), Multiplication(*), Variable(x1)]"

        se = SymbolicEquation(target, str_learning_rule)

        self.assertIsInstance(se, SymbolicEquation)
        self.assertEqual(se.target, target)
        self.assertIsInstance(se.symbol_list, SymbolList)

        # __str__ of a SymbolList goes through every element of the symbol list
        # and "uses" them to write a human readable expression.
        # Checking it is a proxy for checking the SymbolList is correct
        self.assertEqual(se.symbol_list.__str__(), str_output)


if __name__ == "__main__":
    unittest.main()
