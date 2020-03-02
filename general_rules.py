
import pandas as pd


def enrich_lexicon_fun(data_frame):
    # change pct:355 lexicon to lower case
    for rowindex, row in data_frame.iterrows():
        if row['ContentType'] == 'urn:pct:355' or row['ContentType'] == 'urn:pct:225':
            data_frame.at[rowindex,'Title'] = row['Title'].lower()
            #data_frame.at[rowindex,'Title'] = row['Title'].upper()
    return data_frame

if __name__=='__main__':
    df_test=pd.read_csv('Data/dataframe_to_test_enrich_lexicon_fun/data_frame_for_enrich.csv')
    df = enrich_lexicon_fun(df_test)
    print(df)



