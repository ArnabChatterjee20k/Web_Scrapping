import pandas as pd
import sqlite3 as sql,os


class Read:
    
    def __init__(self):
        print("Initialised")
        try:
            self.db="Oneplus earphones.sqlite"
            self.connection=sql.connect(self.db)
            self.cursor=self.connection.cursor()
        except:
            raise Exception("Not found")


    def export(self,csv_file="Amazon review.csv"):
        table_name="REVIEW"

        def add_data(df):
            """Here the data is taken from dataframe of csv file and inserted into db"""
            row_data=[]
            
            col=["customer_name","ReviewTitle","Rating","COntent"]

            for index,row in df.iterrows():
                row_data.append(row[col[0]])               
                row_data.append(row[col[1]])               
                row_data.append(row[col[2]])               
                row_data.append(row[col[3]])               
                self.cursor.execute(f"insert into {table_name} values{(tuple(row_data))}")
                # print(row_data)
                row_data.clear()
            
            self.connection.commit()


        check=self.cursor.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='REVIEW' ''')#checking if the table exists
        if check.fetchall()==[]:
            self.data=pd.DataFrame(pd.read_csv(csv_file))
            self.cursor.executescript(f"create table {table_name}(NAME text UNIQUE,TITLE text,RATINGS text,CONTENT text)")
            self.connection.commit()
            print(f"TABLE {table_name} created")
            add_data(self.data)

        elif check.fetchall()[0][0]!="REVIEW":
            self.data=pd.DataFrame(pd.read_csv(csv_file))
            self.cursor.executescript(f"create table {table_name}(NAME text UNIQUE,TITLE text,RATINGS text,CONTENT text)")
            self.connection.commit()
            print(f"TABLE {table_name} created")   
            add_data(self.data)

        else:
            print("TABLE ALREADY PRESENT SO WE R INSERTING DATA") 
            self.data=pd.DataFrame(pd.read_csv(csv_file))
            add_data(self.data)
    # print(self.data)
        return "DONE"
    

    def view(self):
        data=self.cursor.execute("select * from REVIEW")
        for i in data.fetchall():
            print(i[0],i[1],i[2],i[3])

a=Read()
a.export()
# a.view()
