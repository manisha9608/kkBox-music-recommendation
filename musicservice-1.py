import numpy as np
import pandas as pd


# Read data - members.csv
members_org = pd.read_csv('C:/IDSDatasets/members_v3.csv')
## Drop null values - members.csv
members = members_org.dropna()
print("\n-------- after dropping null values - members.csv ------------\n")
print(members.info())
print(members.head(6))
print(members['msno'].value_counts())
#drop duplicates - members.csv 
members.drop_duplicates(subset=['msno'], keep='first', inplace=True)
print("\n-------- Drop duplicate records - members.csv -----------------\n")
print(members['msno'].value_counts())

# Read data - train.csv
train_org = pd.read_csv('C:/IDSDatasets/train.csv')
# ## Drop null values - train.csv
train = train_org.dropna()
print("\n-------- after dropping null values - train.csv ------------\n")
print(train.info())
print(train.head(6))
print(train['msno'].value_counts())
#drop duplicates - train.csv 
train.drop_duplicates(subset=['msno'], keep='first', inplace=True)
print("\n-------- Drop duplicate records - train.csv -----------------\n")
print(train['msno'].value_counts())

# Read data - transactions.csv
transactions_org = pd.read_csv('C:/IDSDatasets/transactions.csv')
# ## Drop null values - transactions.csv
transactions = transactions_org.dropna()
print("\n-------- after dropping null values - transactions.csv ------------\n")
print(transactions.info())
print(transactions.head(6))
print(transactions['msno'].value_counts())
#drop duplicates - transactions.csv 
transactions.drop_duplicates(subset=['msno'], keep='first', inplace=True)
print("\n-------- Drop duplicate records - transactions.csv -----------------\n")
print(transactions['msno'].value_counts())

# Read data - sample_submission_zero.csv
sample_submission_zero_org = pd.read_csv('C:/IDSDatasets/sample_submission_zero.csv')
## Drop null values - sample_submission_zero.csv
sample_submission_zero = sample_submission_zero_org.dropna()
print("\n-------- after dropping null values - sample_submission_zero.csv ------------\n")
print(sample_submission_zero.info())
print(sample_submission_zero['msno'].value_counts())
#drop duplicates - sample_submission_zero.csv 
sample_submission_zero.drop_duplicates(subset=['msno'], keep='first', inplace=True)
print("\n-------- Drop duplicate records - sample_submission_zero.csv -----------------\n")
print(sample_submission_zero['msno'].value_counts())

# Read data - user_logs.csv
user_logs_org = pd.read_csv('D:/BITS-PILANI/PythonWorkspace/SecondSemester/user_logs.csv')
## Drop null values - user_logs.csv
user_logs = user_logs_org.dropna()
print("\n-------- after dropping null values - user_logs.csv ------------\n")
print(user_logs.info())
print(user_logs.head(6))
print(user_logs['msno'].value_counts())
#drop duplicates - user_logs.csv 
user_logs.drop_duplicates(subset=['msno'], keep='first', inplace=True)
print("\n-------- Drop duplicate records - user_logs.csv -----------------\n")
print(user_logs['msno'].value_counts())


