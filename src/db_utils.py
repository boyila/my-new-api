import pandas as pd
from pathlib import Path
from common_utils import CommonUtils
import random
import os


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
    
    def verify_user(self, fname,lname,dob):
        df = pd.read_csv(os.path.join(self.data_path,"user.csv"))
        
        user_record = df[(df['First_Name']==fname) & 
                         (df['Last_Name']==lname) &
                         (df['Date_Of_Birth']==CommonUtils().convert_date(dob))]
        
        if not user_record.empty:
            # return user_record['user_id'].item()
            return "existing user"
        else:
            return "New user"


    
    def add_new_user(self, fname, lname, dob):
        df = pd.read_csv(os.path.join(self.data_path,"user.csv"))
        dob_formatted = CommonUtils().convert_date(dob)
        new_user_id = self.generate_user_id(df)
        new_record = {
                'user_id':new_user_id,
                'First_Name': fname,
                'Last_Name': lname,
                'Date_Of_Birth': dob_formatted
            }
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df.to_csv(os.path.join(self.data_path, "user.csv"), index=False)
        return new_user_id

    def generate_user_id(self,df):

        existing_user_ids = set(df['user_id'])
        while True:
            # Generate a 6 digit random user_id
            random_user_id = random.randint(100000, 999999)

            if random_user_id not in existing_user_ids:
                return random_user_id
            
    def update_record(self,table_name, user_id,column, value):
        df = pd.read_csv(os.path.join(self.data_path,f"{table_name}.csv"))
        df.loc[df['user_id'] == int(user_id), column] = value
        print(df.loc[df['user_id'] == int(user_id), column].head() )
        df.to_csv(os.path.join(self.data_path, f"{table_name}.csv"), index=False)
        print(os.path.join(self.data_path, f"{table_name}.csv"))
    


if __name__=='__main__':
    db = DbUtils()
    columns_needed = ["user_id",	"transactional_Dates",	"Transactional_catogories",	"Amount",	"description",	"type_of_transactions","Monthly_Income",	"Annual_income"]
    # df = db.get_data('transactional_data','user',columns_needed,'user_id')
    # print(df.head())
    # user= db.verify_user('lakshmi','narayan','1983-05-13')
    # if user is None:
    #     new_user=db.add_new_user('lakshmi','narayan','1983-05-13')
    #     print(f"new user: {new_user}")
    # else:
    #     print(f'existing user: {user}')
    db.update_record('user','410860','Occupation','software Engineer')
