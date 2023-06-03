
## Memoization Recipe

1. Make it work.
  - Visualize the problem as a tree
  - Implement the tree using recursion
    - Thing of the end nodes as the base case for your recursion
  - test it, it may take a long time to run, i.e. brute force.

2. Make it efficient.
  - add a memo object.
    - Make sure the object is shared.
  - Add a base case to return memo values ( memo fetching logic )
  - Store values into the memo, i.e. pass along the values to future calls

  ## Tabulation Recipe

  Visualize the problem as a table.

  Size the table based on the inputs.

  Initialize the table with default values.
  Seed the trivial answer into the table.

  Iterate through the table.
  By iterating, fill the further positions of the table.


  source: freecodecamp dp video