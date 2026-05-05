;;;; Functional Programming

;; Key Ideas
; - Expressions in Scheme
; - Defenitions
; - Compound values
; - Turtle Graphics


; Operations in scheme follow prefix notation:
; (operator operand1 operand2)

(quotient 10 2)

(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))

; The if and cond expressions are special forms that have the syntax:
; (if <predicate> <consequent> <alternative>)
; (cond
;   (<p1> <e1>)
;   (<p2> <e2>)
;   ...
;   (<pn> <en>)
;   (else <else-expression>))

; Cond works as follows: 
; Evaluate the predicates <p1>, <p2>, ..., <pn> in order until one evaluates to a true value (anything but #f) and return the value of its coressponding <e>
; If none of the predicates evaluate to true values and there is an else clause, evaluate and return <else-expression>



; Like Python, Scheme evaluates the operator and operands first, 
; then applies the resulting function to the resulting arguments

; Certain expressions, like if, and, or, and not, have unique evaluation rules for control flow 
; for example, short-circuiting in boolean logic
; (or <e1> ... <en>)
; if e1 is True, the rest if the <e>s are not evaluated and True is returned as the value of the or expression

(and (>= 2 1) (#t) (not #f))


; The define form associates a symbol with a value: 
; (define variable_name value)
; The general form of a procedure definition is:
; (define (<name> <formal parameters>) <body>)

; Local variable assigment can also be done through let expressions:
; (let ((var1 val1) (var2 val2) ...) body)

(let ((x 10)
      (y 20))
   (foo x y))


; Scheme supports nested definitions and recursion, following the same scoping rules as Python

(define pi 3.14)


(define (abs x)
    (if (< x 0)
        (- x)
        x))

(define (average x y)
  (/ (+ x y) 2))

(define (square x) (* x x))

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))


; Anonymous functions are created using the lambda special form
; (lambda (<formal-parameters>) <body>)

((lambda (x y z) (+ x y (square z))) 1 2 3)


; Created using cons, pairs are the building blocks of data
; Elements are accessed via car (first) and cdr (rest).
; Recursive Lists: Lists are sequences of pairs ending in nil (or '())


(define x (cons 1 2))
(define one-through-four (list (car x) (cdr x) 3 4))
        
(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

; The single quote ' is used to treat code or symbols as literal data 
; rather than expressions to be evaluated

(define a 2)
(define b 2)

(define c (list a 'b))

; The normal quote ' and the quasiquote ` are both valid ways to quote an expression
; However, the quasiquoted expression can be unquoted with the "unquote" , (represented by a comma)
; When a term in a quasiquoted expression is unquoted, the unquoted term is evaluated, similar to f-strings in python


`(* ,(+ a b) b)
; returns (* 4 b)


; Scheme includes a "Turtle" graphics environment where a cursor moves and draws on a canvas based on procedural commands
; The begin form allows the execution of multiple sub-expressions in sequence

(define (repeat k fn)
    (if (> k 0)
        (begin (fn) (repeat (- k 1) fn))
        nil))

(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
    (tri (lambda ()
           (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
    (sier (/ d 2) (- k 1))
    (penup)
    (fd d)
    (pendown))


; A macro is an operation performed on the source code of a program before evaluation

; Here are the evaluation steps in a macro:
; Evaluate the operator sub-expression, which evaluates to a macro
; Call the macro procedure on the operand expressions without evaluating them first
; Evaluate the expression returned from the macro procedure

(define-macro (second expr) (car (cdr expr)))
(second (+ 5 7))
; returns 5



