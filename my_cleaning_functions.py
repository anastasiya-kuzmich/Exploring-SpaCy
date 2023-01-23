def restructure_test_dataframe(data, labels):
    
    "Restructures the Toxic-Comments dataframe for modelling"

    import pandas as pd
    
    test_df = pd.concat([data, labels], axis=1)
    test_df = test_df.drop("id", axis=1)
    test_df = test_df[test_df["toxic"] != -1]
    
    del data, labels
    
    test_df['total_score'] = (test_df['toxic'] + 
                              test_df["severe_toxic"] + 
                              test_df["obscene"] + 
                              test_df["threat"] + 
                              test_df["insult"] + 
                              test_df["identity_hate"])
    
    test_df["non_toxic"] = test_df["total_score"].map(non_toxic_mapper)
    test_df = test_df.drop("total_score", axis=1)
    
    y = test_df[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate', 'non_toxic']]
    y = y.to_dict("index")
    
    restructured_data = list(zip(test_df['comment_text'],[{'cats': cats} for cats in y.values()]))
    
    del test_df, y
    
    print("First data entry: ", restructured_data[0])
    
    return restructured_data

def non_toxic_mapper(x):
    
    """Maps the non-toxic column based on the total score column."""
    
    if x == 0: 
        return 1
    else:
        return 0

def add_non_toxic_column(df):
    
    """Adds a non-toxic column."""
    
    df['total_score'] = (df['toxic'] + df["severe_toxic"] 
                         + df["obscene"] + df["threat"]
                         + df["insult"] + df["identity_hate"])

    df["non_toxic"] = df["total_score"].map(non_toxic_mapper)
    df = df.drop("total_score", axis=1)
    
    return df

def clean_comments_column(df):
    
    """Cleans the comments column."""
    
    import re
    
    IpAddressRegex = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    DateTimeRegex = "(\d{2}\:\d{2}\, [A-Z][a-z]{2,8}\ \d{1,2}\, \d{4}\ \([A-Z]{3}\))|(\d{2}\:\d{2}\, \d{2}\ [A-Z][a-z]{2}\ \d{4}\ \([A-Z]{3}\))|(\d{2}\:\d{2}\, \d{1,2}\ [A-Z][a-z]{2,8} \d{4})|(\d{1,2}\ [A-Z][a-z]{2,8}\ \d{4}\ \([A-Z]{3}\))|(\d{1,2}\ [A-Z][a-z]{1,7}\ \d{4})|(\d{2}\:\d{2}\, \d{1,2})|([A-Z][a-z]{2,8}\ \d{4}\ \([A-Z]{3}\))"
    
    features_to_remove = [IpAddressRegex,
                          DateTimeRegex,
                          '\\n', r'\\']
    
    for feature in features_to_remove:
        df["comment_text"] = df["comment_text"].replace(feature,' ', regex=True)
 
    df['comment_text'] = df['comment_text'].replace(u'\xa0', u' ')
    
    return df