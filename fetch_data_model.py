import mysql.connector

import pandas as pd
class fetch_data_model:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="bishwa",
                                            database="pharmanuman")  
            self.cur = self.conn.cursor(dictionary=True)
            print("connection sucessfully")
            self.cur.execute("SELECT * FROM medicine_for_prediction")
            result = self.cur.fetchall()
            print(result)
            df = pd.DataFrame(result)
            df.to_csv("artifacts/database_data/sales.csv",index=False)
            
        except:
            print("Error in connection")
        


    def get_data_all(self):
        
    
        return "Sucessfully"
    