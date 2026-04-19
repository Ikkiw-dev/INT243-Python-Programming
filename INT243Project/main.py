import numpy as np
import pandas as pd

df = pd.read_csv("asthma_disease_data_new.csv")


def overview():
    missing_pid = df[df["PatientID"].isna()]
    valid_pid   = df[df["PatientID"].notna()]

    total_rec = len(df)
    count_missing_pid = len(missing_pid)
    count_valid_pid = len(valid_pid)
    print("Overview datasets of asthma datasets")
    print("=" *60)
    print(f"Total Records : {total_rec}")
    # print("Invalid Patient : ", count_missing_pid)
    # print("Valid Patient : ", count_valid_pid)

def fillID():
    global df

    df = df.sort_values(by="PatientID", na_position='first').reset_index(drop=True)

    start_id = 5034

    for i in range(len(df)):
        if pd.isna(df.loc[i, "PatientID"]):
            if i == 0:
                df.loc[i, "PatientID"] = start_id
            else:
                df.loc[i, "PatientID"] = df.loc[i-1, "PatientID"] + 1

    df["PatientID"] = df["PatientID"].astype(int)

def fillage():
    missing_age = df["Age"].isna().sum()
    avg_age = df["Age"].mean().round()

    df["Age"] = df["Age"].fillna(avg_age)

def fillBMI():
    missing_BMI = df["BMI"].isna().sum()
    avg_BMI = df["BMI"].mean().round()

    df["BMI"] = df["BMI"].fillna(avg_BMI)


def mainrunner():
    overview()
    fillID()
    fillage()
    fillBMI()

mainrunner()

print(df.head(11))