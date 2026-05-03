#### Interpreters for Languages with Abstraction


## Key ideas:
# - Structure
# - Eval/apply cycle
# - Environment model and frames
# - Data as Programs


# To allow for abstraction, the scheme calculator from chapter 3-4 needs to be extended with the following modules:

# Parsing: 
# Uses scheme_reader and scheme_tokens to convert text into nested Pair objects 
# It must handle specialized syntax like quotation (') and dotted lists

# Evaluation: A function that dispatches based on expression type:
# Symbols: Looked up in the current environment
# Literals: Returned as-is
# Special Forms: (e.g., define, lambda) Handled by specific logic
# Call Expressions: Evaluated by applying a procedure to arguments

# Application: Handles two types of procedures:
# Primitive Procedures: Python functions applied directly.
# Lambda Procedures: User-defined Scheme functions. Applying these involves creating a new environment frame and evaluating the function's body.



# The core of the interpreter is a mutually recursive cycle (eval/apply):
# eval calls apply when it encounters a call expression
# apply calls eval to compute operand values and to evaluate the body of user-defined functions
# The recursion ends when it reaches primitives (like numbers) or primitive procedures (implemented in the underlying Python code)



# Environments manage the "state" of the program by binding names to values:
# Frame Objects: Each contains a dictionary of local bindings and a reference to a parent frame
# Lookup: If a symbol isn't in the current frame, the interpreter searches the parent frame, continuing until the global frame is reached
# Define: Always adds or updates a binding in the current frame


# Here is an example:
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)

# Check the format of the expression to ensure that it is a well-formed Scheme list with at least two elements following the keyword define.
# Analyze the first element, to find the function name factorial and formal parameter list (n)
# Create a LambdaProcedure with the supplied formal parameters, body, and parent environment
# Bind the symbol factorial to this function, in the first frame of the current environment. In this case, the environment consists only of the global frame.



# The scheme interpreter is seen to be a universal machine
# It mimics other machines when these are described as Scheme programs
# It acts as a bridge between the data objects that are manipulated by our programming language and the programming language itself

# Languages like Scheme and Python allow programmers to bridge the gap between the user's programs are the interpreter's data using functions like eval, 
# which treat data strings or lists as executable code during runtime.

four = eval('2+2')


