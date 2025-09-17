import pandas as pd
from sqlalchemy import create_engine
import gc # garbage collector

## load in .sql file as string:
with open('Module2_dbs/patient_query.sql', 'r') as file:
    sql_depression_query = file.read()


db_location = 'example.db'

engine = create_engine(f'sqlite:///{db_location}')

patients_df = pd.read_csv('assignments/assignment2_files/patients.csv')

patients_df.to_sql('patients_details', con=engine, if_exists='replace', index=False)

query_anxiety = "SELECT * FROM patients_details WHERE primary_icd10 = 'F41.9'"

results_df = pd.read_sql_query(query_anxiety, con=engine)
len(results_df)




query_x = "SELECT * FROM patients_details WHERE primary_icd10 = 'M54.5'"
results_x_df = pd.read_sql_query(query_x, con=engine)
len(results_x_df)