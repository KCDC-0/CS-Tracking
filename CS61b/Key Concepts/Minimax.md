## Minimax algorithm

The minimax algorithm drives AI decision-making in turn-based games by evaluating possible future moves through a game tree.

In the tree, there are two types of nodes:
- Max-nodes: Represent the primary player, who attempts to maximize the game score
- Min-nodes: Represent the opponent, who attempts to minimize the primary player's score

Tree layers alternate between max-nodes and min-nodes to simulate players taking turns. Working from the bottom of the tree up, max-nodes select the highest value from their children, while min-nodes select the lowest. The search depth is capped to prevent the game tree from calculating an infinite or unmanageable number of nodes.

<br>

A heuristic function evaluates the board state when the tree reaches its depth limit and assigns a numerical score, where +ve indicates that the primary player is winning and vice versa.


<br>

## Alpha beta pruning

Alpha beta pruning can be used to optimise the Minimax tree by ignoring (pruning) branches that optimal players would never choose, saving computational power. It does this by tracking 2 parameters - alpha and beta;
- Alpha starts out as negative infinity and is set by max nodes to their current value
- Beta starts out as positive infinity and is set by min nodes to their current value

Alpha and beta values are passed down from parent nodes to their children. If Alpha ≥ Beta at any point, the remaining branches for that node are pruned and skipped entirely.