import csv
import sqlite3
def main():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    # create customer table
    c.execute("""CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                first_name TEXT,
                last_name TEXT,
                company TEXT,
                city TEXT,
                country TEXT,
                phone1 INTEGER,
                phone2 INTEGER,
                email INTEGER,
                subscription_date TEXT,
                website TEXT,
                sales_2021 INTEGER,
                sales_2022 INTEGER
                )""")

    # read csv file and store into "data" array
    data = []
    with open("../testcases/customers_sales_2021_2022.csv", 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        # A single row from the CSV file is one element in the array
        for row in csvreader:
            data.append(row)

    # insert the data from every element into the customer table
    #for row in data:
        #c.execute(f"""INSERT INTO customer (customer_id, first_name, last_name, company, city, country, phone1, phone2, email, subscription_date, website, sales_2021, sales_2022) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  #(row['Customer Id'], row['First Name'], row['Last Name'], row['Company'], row['City'], row['Country'], row['Phone 1'], row['Phone 2'], row['Email'], row['Subscription Date'], row['Website'], row['SALES 2021'], row['SALES 2022']))
        #conn.commit()

    # test select query
    c.execute("SELECT * FROM customer WHERE country=?", ('Netherlands',))
    for result in c.fetchall():
        print(result)
    conn.close()

if __name__ == "__main__":
        main()