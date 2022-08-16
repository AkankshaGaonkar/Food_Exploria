import sqlite3
#define connection and cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#create food table
def table_creation(connection, cursor):
    command1 = "CREATE TABLE IF NOT EXISTS Food(price FLOAT, food_name TEXT PRIMARY KEY);"
    cursor.execute(command1)
    #create prize table
    command2 = "CREATE TABLE IF NOT EXISTS Cart(order TEXT, FOREIGN KEY (food_name) REFERENCES Food(food_name));"
    cursor.execute(command2)

#add items to food table
def insert_table_food(connection, cursor, price, foodName):
    q = "INSERT INTO Food(price, food_name) VALUES(" + str(price) + " , '" + foodName + "');"   
    cursor.execute(q)
    connection.commit()

def insert_table_cart(connection, cursor, order):
    q = "INSERT INTO Cart(order) VALUES(" + order + ");"   
    cursor.execute(q)
    connection.commit()

#creating table function call

#inserting into table Food using function call, pass the food_id and food_name as arguments to the function
insert_table_food(connection, cursor, 300, "Black Forest")
insert_table_food(connection, cursor, 450, "Choco Lava")
insert_table_food(connection, cursor, 400, "Red Velvet")
insert_table_food(connection, cursor, 550, "Ferrero Rocher")

insert_table_cart(connection, cursor, "Black Forest")
insert_table_cart(connection, cursor, "Choco Lava")
insert_table_cart(connection, cursor, "Red Velvet")
insert_table_cart(connection, cursor, "Ferrero Rocher")
#inserting into table Prize using function call, pass the prize_id and price as arguments to the function
# insert_table_price(connection, cursor, 6, 80)
# insert_table_price(connection, cursor, 1, 400)
# insert_table_price(connection, cursor, 2, 300)
# insert_table_price(connection, cursor, 3, 450)
# insert_table_price(connection, cursor, 4, 500)

'''
here your work is to insert into Price in which for all the foods in table Food, assign the proper price for it.

Note: keep in mind that here prize id in the price table is foreign key so if u insert a price value for the food_id which is not present in the table Food then it will show the integrity error
'''
