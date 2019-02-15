# Author: Deep Datta deepdattax@gmail.com

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import mysql.connector as mc

app = Flask(__name__)

@app.route('/')
def display_orders():
    products = get_products()
    return render_template('wallet.html',products=products)

@app.route('/buy')
def index():
    products = get_products()
    return render_template('buy.html',products=products)

@app.route('/sell')
def sell():
    products = get_products()
    return render_template('sell.html',products=products)

# Sell code 1

@app.route('/sell_order',methods=['POST'])
def sell_order():
    quantity = request.form['quantity']
    product_name = request.form['product_name']
    nquantity = request.form['nquantity']
    update_order(quantity, product_name, nquantity)
    return redirect(url_for('display_orders'))

def update_order(quantity, product_name, nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `nquantity` = '+quantity+' - '+nquantity+' WHERE product_id = 1;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

# Sell code 2

@app.route('/sell_order2',methods=['POST'])
def sell_order2():
    quantity = request.form['quantity']
    product_name = request.form['product_name']
    nquantity = request.form['nquantity']
    update_order2(quantity, product_name, nquantity)
    return redirect(url_for('display_orders'))

def update_order2(quantity, product_name, nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `nquantity` = '+quantity+' - '+nquantity+' WHERE product_id = 2;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

# Sell code 3

@app.route('/sell_order3',methods=['POST'])
def sell_order3():
    quantity = request.form['quantity']
    product_name = request.form['product_name']
    nquantity = request.form['nquantity']
    update_order3(quantity, product_name, nquantity)
    return redirect(url_for('display_orders'))

def update_order3(quantity, product_name, nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `nquantity` = '+quantity+' - '+nquantity+' WHERE product_id = 3;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

def sell_products():
    connection = get_connection()
    result = connection.cmd_query("select * from inventory")
    rows = connection.get_rows()
    connection.close()
    return rows[0]

def get_connection():
    return mc.connect(user='root', password='password',
                              host='127.0.0.1', database='candystore',
                              auth_plugin='mysql_native_password')

# Buy code 1

@app.route('/orders',methods=['POST'])
def buy():
    product = request.form['product']
    quantity = request.form['quantity']
    nquantity = request.form['nquantity']
    insert_order(product,quantity,nquantity)
    return redirect(url_for('display_orders'))

def insert_order(product,quantity,nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `quantity` = '+quantity+' WHERE product_id = 1;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()
    connection = get_connection()
    sql2 = 'UPDATE `inventory` SET `nquantity` = '+nquantity+' + '+quantity+' WHERE product_id = 1;'
    print(sql2)
    connection.cmd_query(sql2)
    connection.commit()
    connection.close()

# Buy code 2

@app.route('/orders2',methods=['POST'])
def buy2():
    product = request.form['product']
    quantity = request.form['quantity']
    nquantity = request.form['nquantity']
    insert_order2(product,quantity,nquantity)
    return redirect(url_for('display_orders'))

def insert_order2(product,quantity,nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `nquantity` = '+quantity+' + '+nquantity+' WHERE product_id = 2;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

# Buy code 3

@app.route('/orders3',methods=['POST'])
def buy3():
    product = request.form['product']
    quantity = request.form['quantity']
    nquantity = request.form['nquantity']
    insert_order3(product,quantity,nquantity)
    return redirect(url_for('display_orders'))

def insert_order3(product,quantity,nquantity):
    connection = get_connection()
    sql = 'UPDATE `inventory` SET `nquantity` = '+quantity+' + '+nquantity+' WHERE product_id = 3;'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

def get_products():
    connection = get_connection()
    result = connection.cmd_query("select * from inventory")
    rows = connection.get_rows()
    connection.close()
    return rows[0]

def get_connection():
    return mc.connect(user='root', password='password',
                              host='127.0.0.1', database='candystore',
                              auth_plugin='mysql_native_password')

# connection = get_connection()
#   result = connection.cmd_query("select * from inventory")
#   rows = connection.get_rows()
#   answer = str(rows[0][0][2]) 
#   connection.close()
#   return render_template('wallet.html')
