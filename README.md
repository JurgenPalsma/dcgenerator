# dcgenerator
Generate directional change events - a technical indicator - from time series

Credit for the idea and pseudocode:
M. Aloud, E. Tsang, R. B. Olsen, and A. Dupuis, "A Directional-Change Events Approach for Studying Financial Time Series," 2012.

## Usage
Install
```
pip install .
```

Import
```
>>> import dcgenerator as dg
```

Call
```
>>> dg.generate(<your data>, <your dc threshold>)
```
