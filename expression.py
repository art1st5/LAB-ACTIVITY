"""ITECC04 Laboratory 4, Parts B and C: the converter and the evaluator.

Part B turns infix into postfix using the Shunting Yard algorithm.
Part C evaluates a postfix expression.

Both use your own stack. Import it, do not use a bare Python list. If your
ArrayStack is not finished, these functions cannot work, so finish Part A
first.

TOKENS ARE SEPARATED BY SPACES. "3 + 4" is valid input, "3+4" is not. This
is deliberate: writing a real tokeniser is a different exercise, and mixing
it in here hides the algorithm you are meant to be learning.
"""

from stack_array import ArrayStack

# Written for you. Higher number binds tighter.
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

# Written for you. 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2), not (2 ^ 3) ^ 2.
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression):
    """Written for you. Splits on whitespace."""
    return expression.split()


def infix_to_postfix(expression, trace=None):
    output = []
    operators = ArrayStack()
    for token in tokenize(expression):
        if token in PRECEDENCE:
            while(not operators.is_empty() 
                    and operators.peek() != "(" 
                    and (PRECEDENCE[operators.peek()] > PRECEDENCE[token] 
                    or (PRECEDENCE[operators.peek()] == PRECEDENCE[token] 
                        and token not in RIGHT_ASSOCIATIVE))):
                output.append(operators.pop())
            operators.push(token)
            action = "push operator"
        elif token == "(":
            operators.push(token)
            action = "push ("
        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())
            if operators.is_empty():
                raise ValueError("Unbalanced parenthesis: missing '('")
            operators.pop()
            action = "pop  to ("
        else:
            output.append(token)
            action = "operand to output"

        if trace is not None:
            trace.append((token, action, " ".join(output), "".join(operators._items)))
    while not operators.is_empty(): 
        if operators.peek() == "(":
            raise ValueError("error")
        output.append(operators.pop())
    if trace is not None:
        trace.append(("end", "pop all", "".join(output)," ".join(operators._items)))
    return " ".join(output )
        
 
    raise NotImplementedError("Step 1: implement the Shunting Yard algorithm")


def evaluate_postfix(expression, trace=None):
    values = ArrayStack()
    for token in tokenize(expression):
        if token in PRECEDENCE:
            if values.size() < 2:
                raise ValueError ("error")
            right = values.pop()
            left = values.pop()
            _fmt = format
            result = apply_operator(token, left, right)
            values.push(result)
        else:
            values.push(float(token))

        if trace is not None:
            trace.append((token, " ".join(_fmt(v) for v in values._items)))
    if values.size() != 1:
        raise ValueError("error")
    return values.pop()


    """Step 2. Evaluate a postfix expression. Return a float.

    Walk the tokens once, with a stack of values:

      operand      push float(token)
      operator     pop TWICE. The FIRST pop is the RIGHT operand, the second
                   is the left. Getting this backwards passes for + and *
                   and quietly fails for - and /, so it survives careless
                   testing. Push the result.

    Guards you must write:
      fewer than two values when an operator arrives -> ValueError
      more than one value left at the end            -> ValueError
      division or modulo by zero                     -> ZeroDivisionError

    Return the single remaining value.
    """
    raise NotImplementedError("Step 2: implement the postfix evaluator")


def apply_operator(operator, left, right):
    if operator == "+":
        return left + right
    if operator ==  "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError ("error")
        return left / right
    if operator == "%": 
        if right == 0:
            raise ZeroDivisionError ("error")

        return left % right
    if operator == "^":
        return left ** right
    raise ValueError (f"unknown operator'{operator}'")
        
 
 
 
 
 
 
 
 
    """Step 3. Return the result of `left operator right`.

    Handle + - * / % ^. Raise ZeroDivisionError with a message for / and %
    when right is 0. Raise ValueError for any operator you do not know.
    """
    raise NotImplementedError("Step 3: implement the six operators and their guards")


def convert_and_evaluate(expression):
    """Written for you. Used by the test file and by the classwork demo."""
    postfix = infix_to_postfix(expression)
    return postfix, evaluate_postfix(postfix)


if __name__ == "__main__":
    # Once Steps 1 to 3 are written, this prints the worked example from the
    # lecture. Until then it reports which step is still missing.
    try:
        postfix, value = convert_and_evaluate("3 + 4 * 2")
        print("infix   : 3 + 4 * 2")
        print("postfix :", postfix)
        print("value   :", value)
    except NotImplementedError as unfinished:
        print("Not written yet ->", unfinished)
