## Asymptotic analysis
Asymptotic analysis evaluates how a function or program behaves as its input sizes grow extremely large

Measurement metrics:

- Time: Evaluates execution duration, heavily impacted by operations like loops and recursion
- Space: Evaluates memory usage, impacted by large lists or holding massive amounts of individual objects
- Complexity: A generalized, theoretical cost where every basic operation (addition, printing, etc) is assigned a value of 1 and tallied up

To simplify the functions, only keep the fastest growing term, and remove all constants and other variables ( $5log(3n) + 4n$ -> $n$ )

<br>

3 big bounds:
- Big O ($O$): upper bound. The algorithm's growth rate will be slower than or equal to this function (worst-case scenario)
- Big Omega ($\Omega$): lower bound. The algorithm's growth rate will be faster than or equal to this function (best-case scenario)
- Big Theta ($\Theta$): exact bound. This only exists if the Big O and Big Omega bounds are identical

<br>

Orders of growth:
- $\Theta(1)$: Constant
- $\Theta(\log n)$: Logarithmic
- $\Theta(n)$: Linear
- $\Theta(n \log n)$: Linearithmic
- $\Theta(n^2)$: Quadratic
- $\Theta(2^n)$: Exponential
- $\Theta(n!)$: Factorial
- $\Theta(n^n)$: Tetration


<br>
<br>


## Amortisation
Amortization means to spread out the cost of operations. When an operation's runtime varies based on the input n, amortization averages the costs across all operations to report an amortized runtime