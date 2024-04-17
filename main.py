import requests # type: ignore
import psycopg2 # type: ignore
import csv
from psycopg2 import sql
from bs4 import BeautifulSoup # type: ignore
responseData = requests.get("https://food-guide.canada.ca/en/recipes")
soup = BeautifulSoup(responseData.text,"html.parser")
selectedElements = soup.find_all(class_="views-field-field-featured-image")
mainData=[]  #To Store Data in list
for item in selectedElements:
    receipeUrl=item.find("img")["src"]
    receipeImage=item.find("a")["href"]
    receipeName=item.find_next("div",class_="views-field views-field-title").get_text(strip=True)
    newtuple=(receipeImage,receipeName,receipeUrl)
    mainData.append(newtuple)
def connectDB():
  try:
      conn = psycopg2.connect( dbname="postgres",
                user="postgres",
                password="Kalaana1@",
                host="localhost",
                port="5432"
            )
      print("Connected to PostgreSQL database!")
      comm = conn.cursor()
      createQuery="""CREATE Table IF NOT EXISTS FoodData(
                     receipeName VARCHAR(255),
                    receipeUrl VARCHAR(255),
                   receipeImageUrl VARCHAR(255))"""
      comm.execute(createQuery)
      conn.commit()
      print("task completed")
      insertCommand=sql.SQL("INSERT INTO FoodData(receipeName,receipeUrl,receipeImageUrl) VALUES (%s,%s,%s)")
      for item in mainData:
            comm.execute(insertCommand,item)
            conn.commit()
      d=comm.execute("SELECT * FROM FoodData")
      print(d)
      allData=comm.fetchall()
      print(allData)
      comm.close()     
  except (Exception,psycopg2.Error) as error: # to catch any error
       print("Error while connecting to PostgreSQL database:", error)
  finally: 
        conn.close()
        print("Connection closed successfully")     
connectDB()
