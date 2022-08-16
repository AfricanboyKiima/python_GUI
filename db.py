import sqlite3

class Database:
    def __init__(self, db): #python constructor to create attributes
        """
        for us to query postgres using python,we need two objects, a connection object and a cursor object
        """
        self.conn = sqlite3.connect(db)
        #create database connection to sqlite()
        self.cur = self.conn.cursor()#crete cursor object to execute queries in the connected database.
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text,customer text, retailer text, price text)")
        self.conn.commit()
        """
        The sum of the above code creates a connection and enables us carry out a query using the
        """
    
    #WE NEED TO CARRY OUT CRUD OPERATIONS NOW
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",(part,customer,retailer,price))
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,part,customer,retailer,price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?", (part,customer,retailer,price,id))
        self.conn.commit()  
    
    def __del__(self): #python destructor that enables me close the database
        self.conn.close()

db = Database("store.db")
db.insert("4GB DDR4 Ram","John Doe", "Microcenter","160")
db.insert("Asus Mobo","Mike Henry", "Microcenter","360")
db.insert("500w PSU","Karen Johnson", "Newegg","80")
db.insert("2GB DDR4 Ram","Karen Johnson", "Newegg","70")
db.insert("24 inch Samsung Monitor","Sam Smith", "Best Buy","180")
db.insert("NVIDIA RTX 2000","Albert Kingston", "Newegg","679")
db.insert("600w Corsair PSU","Karen Johnson", "Newegg","130")