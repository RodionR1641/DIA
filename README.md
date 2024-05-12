link: https://github.com/RodionR1641/DIA

Modification of the BSE environment that introduces noise and uncertainty experiments for traders. Includes time delays, market shocks and new insider trading agent

major changes/additions are identified by "#==========" comments

BSE.py includes the code to run the experiments at the bottom of the file
processResults.py includes code to display different kinds of graphs to show either trader performance or equilibrium over time

To run experiments:
- choose the type of experiment to run in the BSE.py starting at line 2730. Setting one of these to true and the rest to false allows you to conduct the corresponding experiments.
- this should generate appropriate graphs given some time, such as the average profit graph. processResults.py contains the functions that generate such graphs

Based on work from the original BSE: https://github.com/davecliff/BristolStockExchange and peer-reviewed paper that describes BSE:
- Cliff, D. (2018). BSE: A Minimal Simulation of a Limit-Order-Book Stock Exchange. In M. Affenzeller, et al. (Eds.), Proceedings 30th European Modeling and Simulation Symposium (EMSS 2018), pp. 194-203. DIME University of Genoa.

