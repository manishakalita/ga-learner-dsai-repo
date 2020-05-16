# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here
categorical_var=bank.select_dtypes(include='object')
print(categorical_var.shape)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)

banks=bank.drop(['Loan_ID'],axis=1)

print(banks.isnull().sum())

bank_mode=banks.mode()

banks=banks.fillna(bank_mode.iloc[0])

print(banks.isnull().sum().values.sum())


avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1])

loan_approved_se=banks[(banks['Self_Employed']== 'Yes') &  (banks['Loan_Status'] == 'Y')].shape


loan_approved_nse=banks[(banks['Self_Employed']== 'No') &  (banks['Loan_Status'] == 'Y')].shape

Loan_Status =614

percentage_se=(loan_approved_se[0]/Loan_Status)*100

percentage_nse=(loan_approved_nse[0]/Loan_Status)*100
print(percentage_se)
print(percentage_nse)

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)

loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
mean_values.iloc[1,0]


