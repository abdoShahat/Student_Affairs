import pandas as pd 
import numpy as np 

database = {
    'Full_name':["Spark","PySpark","Hadoop","Python"],
    'Date_of_birth' :['12/05/2023','26/07/2023','22/02/2023','19/08/2023'],
    'Email' :['abdo@gmail.com','mo@gmail.com','n@gmail.com','m@gmail.com'],
    'Mobile_number' :['011585','010055','010088','01044'],
    'Gender' :['male','male','male','male'],
    'Militry_id' :[1234,5432,6789,7654]
          }
df = pd.DataFrame(database)

df.to_csv("database.csv")