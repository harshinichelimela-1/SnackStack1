from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",         # change if needed
    password="root",     # your MySQL password
    database="food_order"  # your database name (matches your SQL script)
)


@app.route('/')
def home():
    return """
    <h2>Welcome!</h2>
    <p><a href='/users'>View Users</a></p>
    <p><a href='/restaurants'>View Restaurants</a></p>
    <p><a href='/menu_items'>View Menu Items</a></p>
    <p><a href='/orders'>View Orders</a></p>
    <p><a href='/payments'>View Payments</a></p>
    <p><a href='/delivery_staff'>View Delivery Staff</a></p>
    """

@app.route('/menu_items')
def show_menu_items():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu_items;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Menu Items", data=data)

@app.route('/ordered_items')
def show_ordered_items():
   
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Ordered Items", data=data)

@app.route('/delivery_staff')
def show_delivery_staff():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM delivery_staff;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Delivery Staff", data=data)


@app.route('/users')
def show_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Users", data=data)

@app.route('/restaurants')
def show_restaurants():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Restaurants", data=data)

@app.route('/orders')
def show_orders():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Orders", data=data)

@app.route('/payments')
def show_payments():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title="Payments", data=data)


if __name__ == '__main__':
    app.run(debug=True)
