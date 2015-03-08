from enum import Enum


class Syntax(Enum):
    AssignmentExpression = "AssignmentExpression"
    ArrayExpression = "ArrayExpression"
    ArrowFunctionExpression = "ArrowFunctionExpression"
    BlockStatement = "BlockStatement"
    BinaryExpression = "BinaryExpression"
    BreakStatement = "BreakStatement"
    CallExpression = "CallExpression"
    CatchClause = "CatchClause"
    ClassBody = "ClassBody"
    ClassDeclaration = "ClassDeclaration"
    ClassExpression = "ClassExpression"
    ConditionalExpression = "ConditionalExpression"
    ContinueStatement = "ContinueStatement"
    DoWhileStatement = "DoWhileStatement"
    DebuggerStatement = "DebuggerStatement"
    EmptyStatement = "EmptyStatement"
    ExpressionStatement = "ExpressionStatement"
    ForStatement = "ForStatement"
    ForInStatement = "ForInStatement"
    FunctionDeclaration = "FunctionDeclaration"
    FunctionExpression = "FunctionExpression"
    Identifier = "Identifier"
    IfStatement = "IfStatement"
    Literal = "Literal"
    LabeledStatement = "LabeledStatement"
    LogicalExpression = "LogicalExpression"
    MemberExpression = "MemberExpression"
    MethodDefinition = "MethodDefinition"
    NewExpression = "NewExpression"
    ObjectExpression = "ObjectExpression"
    Program = "Program"
    Property = "Property"
    ReturnStatement = "ReturnStatement"
    SequenceExpression = "SequenceExpression"
    SwitchStatement = "SwitchStatement"
    SwitchCase = "SwitchCase"
    ThisExpression = "ThisExpression"
    ThrowStatement = "ThrowStatement"
    TryStatement = "TryStatement"
    UnaryExpression = "UnaryExpression"
    UpdateExpression = "UpdateExpression"
    VariableDeclaration = "VariableDeclaration"
    VariableDeclarator = "VariableDeclarator"
    WhileStatement = "WhileStatement"
    WithStatement = "WithStatement"

Statements = [
    Syntax.Program,
    Syntax.IfStatement,
    Syntax.TryStatement
]