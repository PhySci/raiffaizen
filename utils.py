import pandas as pd

def haversine(pos1, pos2):
    """
    Calculate the great circle distance between two points
    """
    return (pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2

def clean_mcc(df):
    c = lambda s: int(s.replace(',', '')) if isinstance(s, str) else s
    df.mcc = df.mcc.apply(c)
    return df


def clean_df(pth):
    df = pd.read_csv(pth)
    replace_dict = {'pos_adress_lat': 'pos_address_lat', 'pos_adress_lon': 'pos_address_lon'}
    for k in replace_dict.keys():
        if k in df.columns:
            df.rename(columns = {k: replace_dict[k]}, inplace= True)

    df.loc[:,'mcc'] = clean_mcc(df)
    df['pos_address'] = df.atm_address.fillna('')+df.pos_address.fillna('')
    df.drop(['atm_address'], axis=1, inplace=True)
    df['pos_address_lon'] = df.atm_address_lon.fillna(0)+df.pos_address_lon.fillna(0)
    df['pos_address_lat'] = df.atm_address_lat.fillna(0)+df.pos_address_lat.fillna(0)



    return df.drop(['atm_address_lon', 'atm_address_lat'], axis=1)

def get_target_distances(df):
    dist_home_sq = (df.pos_address_lat_mean-df.home_add_lat_mean)**2+(df.pos_address_lon_mean-df.home_add_lon_mean)**2
    dist_work_sq = (df.pos_address_lat_mean-df.work_add_lat_mean)**2+(df.pos_address_lon_mean-df.work_add_lon_mean)**2
    return pd.concat([dist_home_sq, dist_work_sq], axis=1).rename(columns = {0: 'dist_home', 1: 'dist_work'} )