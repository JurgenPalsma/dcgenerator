import pandas as pd 

def generate(data, d=0.1):
    """Generates directional change events from time series.

    Based on:
        M. Aloud, E. Tsang, R. B. Olsen, and A. Dupuis, "A Directional-Change Events Approach for Studying Financial Time Series," 2012.

    Args:
        data: pandas.Series or array of floats
        d: Directional Change threshold

    Returns:
        A pandas series of Directional Change Events.

    """
    
    p = pd.DataFrame({
    "Price": data
    })
    p["Event"] = ''
    event = 'upturn'
    ph = p['Price'][0] # highest price
    pl = ph # lowest price

    for i in range(0, len(p)):

        if event is 'upturn':
            if p['Price'][i] <= (ph * (1 - d)):
                event = 'downturn'
                pl = p['Price'][i]
                p.at[i, 'Event'] = 'end downturn'
                p.at[i + 1, 'Event'] = 'start downward os'
            
            else:
                if ph < p['Price'][i]:
                    ph = p['Price'][i]
                    p.at[i, 'Event'] = 'start downturn'
                    p.at[i - 1, 'Event'] = 'end upward os'
        else:
            if p['Price'][i] >= (pl * (1 + d)):
                event = 'upturn'
                ph = p['Price'][i]
                p.at[i, 'Event'] = 'end upturn'
                p.at[i + 1, 'Event'] = 'start upward os'
            
            else:
                if pl > p['Price'][i]:
                    pl = p['Price'][i]
                    p.at[i, 'Event'] = 'start upturn'
                    p.at[i - 1, 'Event'] = 'end downward os'
    
    return p['Event']