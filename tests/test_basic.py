__author__ = 'kristian'

import unittest
import jscodegen


class BaseTestCase(unittest.TestCase):

    def test_literals(self):
        # true
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"Literal","value":True,"raw":"true"}}]})
        self.assertEqual("true;", result)

        # false
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"Literal","value":False,"raw":"true"}}]})
        self.assertEqual("false;", result)

        # null
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"Literal","value":None,"raw":"null"}}]})
        self.assertEqual("null;", result)


    def test_update_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"UpdateExpression","operator":"++","argument":{"type":"Identifier","name":"i"},"prefix":True}}]})
        self.assertEqual("++i;", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"UpdateExpression","operator":"++","argument":{"type":"Identifier","name":"i"},"prefix":False}}]})
        self.assertEqual("i++;", result)

    def test_unary_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"BinaryExpression","operator":"-","left":{"type":"Literal","value":5,"raw":"5"},"right":{"type":"UnaryExpression","operator":"-","argument":{"type":"Literal","value":5,"raw":"5"}}}}]})
        self.assertEqual("5 - -5;", result)

    def test_binary_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"BinaryExpression","operator":"+","left":{"type":"Literal","value":4,"raw":"4"},"right":{"type":"Literal","value":5,"raw":"5"}}}]})
        self.assertEqual( "4 + 5;", result)

    def test_member_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"CallExpression","callee":{"type":"MemberExpression","computed":False,"object":{"type":"Identifier","name":"Math"},"property":{"type":"Identifier","name":"cos"}},"arguments":[{"type":"MemberExpression","computed":False,"object":{"type":"Identifier","name":"Math"},"property":{"type":"Identifier","name":"PI"}}]}}]})
        self.assertEqual("Math.cos(Math.PI);", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"MemberExpression","computed":True,"object":{"type":"MemberExpression","computed":False,"object":{"type":"Identifier","name":"obj"},"property":{"type":"Identifier","name":"a"}},"property":{"type":"UpdateExpression","operator":"++","argument":{"type":"Identifier","name":"i"},"prefix":False}}}]})
        self.assertEqual("obj.a[i++];", result)

    def test_parenthesis(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"BinaryExpression","operator":"*","left":{"type":"BinaryExpression","operator":"+","left":{"type":"Literal","value":4,"raw":"4"},"right":{"type":"Literal","value":5,"raw":"5"}},"right":{"type":"Literal","value":10,"raw":"10"}}}]})
        self.assertEqual("(4 + 5) * 10;", result)

    def test_call(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"CallExpression","callee":{"type":"Identifier","name":"func"},"arguments":[{"type":"Literal","value":5,"raw":"5"},{"type":"Identifier","name":"a"}]}}]})
        self.assertEqual("func(5, a);", result)

    def test_declaration(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"a"},"init":None}],"kind":"var"}]})
        self.assertEqual("var a;", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"a"},"init":{"type":"Literal","value":5,"raw":"5"}}],"kind":"var"}]})
        self.assertEqual("var a = 5;", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"a"},"init":{"type":"Literal","value":5,"raw":"5"}},{"type":"VariableDeclarator","id":{"type":"Identifier","name":"b"},"init":None},{"type":"VariableDeclarator","id":{"type":"Identifier","name":"c"},"init":{"type":"Literal","value":0.9,"raw":"0.9"}}],"kind":"var"}]})
        self.assertEqual("var a = 5, b, c = 0.9;", result)

    def test_function_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"a"},"init":{"type":"FunctionExpression","id":None,"params":[],"defaults":[],"body":{"type":"BlockStatement","body":[]},"rest":None,"generator":False,"expression":False}}],"kind":"var"}]})
        self.assertEqual("var a = function() {\n};", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"a"},"init":{"type":"FunctionExpression","id":None,"params":[{"type":"Identifier","name":"a"},{"type":"Identifier","name":"b"},{"type":"Identifier","name":"c"}],"defaults":[],"body":{"type":"BlockStatement","body":[]},"rest":None,"generator":False,"expression":False}}],"kind":"var"}]})
        self.assertEqual("var a = function(a, b, c) {\n};", result)

    def test_new_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"NewExpression","callee":{"type":"Identifier","name":"Something"},"arguments":[{"type":"Identifier","name":"p"},{"type":"Identifier","name":"p2"}]}}]})
        self.assertEqual("new Something(p, p2);", result)

    def test_for_statement(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ForStatement","init":{"type":"AssignmentExpression","operator":"=","left":{"type":"Identifier","name":"i"},"right":{"type":"Literal","value":0,"raw":"0"}},"test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"i"},"right":{"type":"Literal","value":10,"raw":"10"}},"update":{"type":"UpdateExpression","operator":"++","argument":{"type":"Identifier","name":"i"},"prefix":False},"body":{"type":"BlockStatement","body":[{"type":"ExpressionStatement","expression":{"type":"CallExpression","callee":{"type":"Identifier","name":"print"},"arguments":[{"type":"Literal","value":"Hallo","raw":"\"Hallo\""}]}}]}}]})
        self.assertEqual("for (i = 0; i < 10; i++) {\nprint('Hallo');\n}", result)

    def test_conditional_expression(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"ExpressionStatement","expression":{"type":"ConditionalExpression","test":{"type":"Identifier","name":"a"},"consequent":{"type":"BinaryExpression","operator":"-","left":{"type":"Identifier","name":"a"},"right":{"type":"Identifier","name":"b"}},"alternate":{"type":"Identifier","name":"c"}}}]})
        self.assertEqual("a ? a - b : c;", result)

    def test_if_statement(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"IfStatement","test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"a"},"right":{"type":"Identifier","name":"b"}},"consequent":{"type":"BlockStatement","body":[]},"alternate":None}]})
        self.assertEqual("if (a < b) {\n}", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"IfStatement","test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"a"},"right":{"type":"Identifier","name":"b"}},"consequent":{"type":"BlockStatement","body":[]},"alternate":{"type":"BlockStatement","body":[{"type":"ExpressionStatement","expression":{"type":"UpdateExpression","operator":"--","argument":{"type":"Identifier","name":"a"},"prefix":False}}]}}]})
        self.assertEqual("if (a < b) {\n} else {\na--;\n}", result)

    def test_while_statement(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"WhileStatement","test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"a"},"right":{"type":"Literal","value":5,"raw":"5"}},"body":{"type":"BlockStatement","body":[]}}]})
        self.assertEqual("while (a < 5) {\n}", result)

    def test_array_expression(self):
        # no elements
        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"c"},"init":{"type":"ArrayExpression","elements":[]}}],"kind":"var"}]})
        self.assertEqual("var c = [];", result)

        #with elements
        result = jscodegen.generate({"type":"Program","body":[{"type":"VariableDeclaration","declarations":[{"type":"VariableDeclarator","id":{"type":"Identifier","name":"c"},"init":{"type":"ArrayExpression","elements":[{"type":"Literal","value":1,"raw":"1"},{"type":"Literal","value":2,"raw":"2"},{"type":"BinaryExpression","operator":"+","left":{"type":"Literal","value":3,"raw":"3"},"right":{"type":"Literal","value":4,"raw":"4"}}]}}],"kind":"var"}]})
        self.assertEqual("var c = [1, 2, 3 + 4];", result)

    def test_break_statement(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"WhileStatement","test":{"type":"Literal","value":True,"raw":"true"},"body":{"type":"BlockStatement","body":[{"type":"IfStatement","test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"a"},"right":{"type":"Literal","value":5,"raw":"5"}},"consequent":{"type":"BlockStatement","body":[{"type":"BreakStatement","label":None}]},"alternate":None}]}}]})
        self.assertEqual("while (true) {\nif (a < 5) {\nbreak;\n}\n}", result)

    def test_function_declaration(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"FunctionDeclaration","id":{"type":"Identifier","name":"f"},"params":[],"defaults":[],"body":{"type":"BlockStatement","body":[]},"rest":None,"generator":False,"expression":False}]})
        self.assertEqual("function f() {\n}", result)

        result = jscodegen.generate({"type":"Program","body":[{"type":"FunctionDeclaration","id":{"type":"Identifier","name":"f"},"params":[{"type":"Identifier","name":"a"},{"type":"Identifier","name":"b"},{"type":"Identifier","name":"c"},{"type":"Identifier","name":"d"}],"defaults":[],"body":{"type":"BlockStatement","body":[]},"rest":None,"generator":False,"expression":False}]})
        self.assertEqual("function f(a, b, c, d) {\n}", result)

    def test_return_statement(self):
        result = jscodegen.generate({"type":"Program","body":[{"type":"FunctionDeclaration","id":{"type":"Identifier","name":"f"},"params":[{"type":"Identifier","name":"a"},{"type":"Identifier","name":"b"},{"type":"Identifier","name":"c"},{"type":"Identifier","name":"d"}],"defaults":[],"body":{"type":"BlockStatement","body":[{"type":"IfStatement","test":{"type":"BinaryExpression","operator":"<","left":{"type":"Identifier","name":"a"},"right":{"type":"Identifier","name":"b"}},"consequent":{"type":"ReturnStatement","argument":None},"alternate":None},{"type":"ReturnStatement","argument":{"type":"BinaryExpression","operator":"*","left":{"type":"Identifier","name":"c"},"right":{"type":"Identifier","name":"d"}}}]},"rest":None,"generator":False,"expression":False}]})
        self.assertEqual("function f(a, b, c, d) {\nif (a < b) return;\nreturn c * d;\n}", result)


if __name__ == '__main__':
    unittest.main()
