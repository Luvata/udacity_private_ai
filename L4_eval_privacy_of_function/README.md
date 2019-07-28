# Evaluate the Privacy of a Function
Evaluate whether the result of our query is leaking private information, in other words, evaluate whether the output of 
the query changes when removing an individual from the database

## Definitions
### Sensitivity (or L1 sensitivity)
The Maximum amount that the query changes when removing an individual from the database

Example: Sensitivity of `sum` query is 1
#### Non data conditioned sensitivity
- Sensitivity is only based on the function and prior knowledge about the potential range of the data
- Example query: `sum`, `mean`
#### Data conditioned sensitivity
- Not only conditioned on the potential range of the data, but also the **actual values in the database**
- Example query: `threshold` 
### Differencing attack
Compare results of **two different queries**, one that include a data subject, and one that exclude it, in order to
divulge the value of this data subject