import pandas as pd
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
class DbUtils:

    def __init__(self):
        self.data_path = os.path.join(ROOT_DIR,"data")
    
    def get_data(self, table1, table2, columns,user_id):
        df1 = pd.read_csv(os.path.join(self.data_path,f"{table1}.csv"))
        df2 = pd.read_csv(os.path.join(self.data_path,f"{table2}.csv"))

        combined_data = pd.merge(df1,df2,on=user_id,how="left")
        columns_drop = [col for col in combined_data.columns if col not in columns]
        combined_data = combined_data.drop(columns=columns_drop, axis=1)
        
        return combined_data
    
if __name__=='__main__':
    db = DbUtils()
    columns_needed = ["user_id",	"transactional_Dates",	"Transactional_catogories",	"Amount",	"description",	"type_of_transactions","Monthly_Income",	"Annual_income"]
    df = db.get_data('transactional_data','user',columns_needed,'user_id')
    print(df.head())
