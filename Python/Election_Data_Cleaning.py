import pandas as pd
df = pd.read_csv("Indian_election_dataset.csv")  
df.drop(['partyabbre','pc_name','pc_no'],axis=1, inplace=True)
df.rename(columns={
    'st_name': 'State',
    'pc_no': 'Constituency_No',
    'pc_type': 'Constituency_Type',
    'cand_name': 'Candidate_Name',
    'cand_sex': 'Candidate_Gender',
    'totvotpoll': 'Votes_Polled',
},inplace=True)
df.drop_duplicates(inplace=True)
df['State'] = df['State'].astype("string")
df['Candidate_Name'] = df['Candidate_Name'].astype("string")
df['Candidate_Gender'] = df['Candidate_Gender'].astype("string")
df['partyname'] = df['partyname'].astype("string")
df['Constituency_Type'] = df['Constituency_Type'].astype("string")
df=df.dropna(subset=(['State','year']))
df=df.dropna(subset=(['Candidate_Name','partyname']))
df=df.dropna(subset=(['Candidate_Gender']))
df['electors']=df['electors'].fillna(df['electors'].median())
df['year']=df['year'].astype(int)
df['Candidate_Gender'] = df['Candidate_Gender'].replace('F', 'Female')
df['Constituency_Type'] = df['Constituency_Type'].fillna('Other')
df['Votes_Polled']=df['Votes_Polled'].fillna(df['Votes_Polled'].median())
df.to_csv('election_clean_data.csv' , index = False)