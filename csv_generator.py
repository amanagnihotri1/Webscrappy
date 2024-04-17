import psycopg2 # type: ignore
import csv
def createCSV():
     conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Kalaana1@",
    host="localhost",
    port="5432"
      )

# Create a cursor object
     cur = conn.cursor()

# Execute SQL query to retrieve data
     cur.execute("select * from FoodData")
# Fetch all rows
     rows = cur.fetchall()
     print(rows)
# Define the path for the CSV file
     csv_file_path = "output.csv"

# Write data to CSV file
     with open(csv_file_path, "w", newline="") as csv_file:
      csv_writer = csv.writer(csv_file)
    # Write the header row if needed
    # csv_writer.writerow(["column1", "column2", ...])
    # Loop through the rows and write them to the CSV file
      for row in rows:
         csv_writer.writerow(row)

# Close the cursor and connection
     cur.close()
     conn.close()

print("CSV file created successfully!")   
createCSV()