import numpy as np
import pandas as pd

df = pd.read_csv("ds_salaries.csv")

print(len(df))
print(df[['experience_level','salary']].dtypes)
print(df['job_title'].nunique())
print(df['job_title'].unique().shape)



df["experience_level"] = df['experience_level'].replace({'EN':'Entry-level','MI':'Mid-level','SE':'Senior-level','EX':'Executive-level'})
df['company_size'] = df['company_size'].replace({'S':'Small','M':'Medium','L':'Large'})

df.to_csv("submission.csv", index=False)

print(df.head(5))