import sqlite3
#define connection and cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#create food table
def table_creation(connection, cursor):
    command1 = "CREATE TABLE IF NOT EXISTS Food(food_id INTEGER PRIMARY KEY, food_name TEXT);"
    cursor.execute(command1)
    #create prize table
    command2 = "CREATE TABLE IF NOT EXISTS Prize(prize_id INTEGER, price FLOAT, FOREIGN KEY (prize_id) REFERENCES Food(food_id));"
    cursor.execute(command2)

#add items to food table
def insert_table_food(connection,cursor, foodId, foodName):
    q = "INSERT INTO Food(food_id, food_name) VALUES(" + str(foodId) + " , '" + foodName + "');"   
    cursor.execute(q)
    connection.commit()

def insert_table_price(connection,cursor, prizeId, price):
    q = "INSERT INTO Prize(prize_id, price) VALUES(" + str(prizeId) + " , " + str(price) + ");"   
    cursor.execute(q)
    connection.commit()

#creating table function call
#table_creation(connection, cursor)

#inserting into table Food using function call, pass the food_id and food_name as arguments to the function
# insert_table_food(connection, cursor, 6, "Dairy Milk Silk")

#inserting into table Prize using function call, pass the prize_id and price as arguments to the function
insert_table_price(connection, cursor, 6, 80)

'''
here your work is to insert into Price in which for all the foods in table Food, assign the proper price for it.

Note: keep in mind that here prize id in the price table is foreign key so if u insert a price value for the food_id which is not present in the table Food then it will show the integrity error
'''