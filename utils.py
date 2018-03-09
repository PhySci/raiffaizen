

def haversine(pos1, pos2):
    """
    Calculate the great circle distance between two points
    """
    return (pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2

def clean_mcc(df):
    c = lambda s: int(s.replace(',', '')) if isinstance(s, str) else s
    df.mcc = df.mcc.apply(c)
    return df


