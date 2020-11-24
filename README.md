# EA_Project
first semester project for the energy analytics stream


# Things to do

Optimize metrics: **Find which correlates best**
- Well length
- Frac stages
- Ammount of proppant
    - approach, have multiple different methods to find the
        1. Average
        2. Median
        3. Max
        4. Min
    - Choose the one with the lowest mean squared error
- Pump rate 
  - Same approach as propant

Finding correlations - Useful for Dimension redcution and (pca)
===
Pearsons Co-effecient for linear
Spearmans for non-linear

Pump rate and propant are directly correlated???
=== 
Lets proove it
Optimize proppant weight to increase pump weight?

Find location on map for attributes.

To get **Maximum Production**

Calculate all of these bois
1. Oil 1-12 Q_i
2. Qec - economic limit rate of prod
3. Life of resivoir - t
4. Rate of initial prod q_t == -(qi^2)/ec
5. Cumulative prod

Calculate Variable:
- Life of resivoir
- **Rate of initial production** 
- Original oil in Place
- Recoverable reserves
- Rate of initial production
- Cumulative production

Create a Cumulative Model
====
| Well name | Cumulative Production | Well Length | Frac Stages | Amount of Propant | Pump Rate |
|-----------|-----------------------|-------------|-------------|-------------------|-----------|
| ...       | ...                   | ...         | ...         | ...               | ...       |



# The final result

1. How long the well is
2. Where it starts
3. Life time of well?
4. and expected cumulative production
