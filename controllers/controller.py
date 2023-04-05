from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="Bethazon", orders=orders)

@app.route('/orders/<int:id>')
def single_task(id):
    return render_template('order.html', title='Single Task', order=orders[id])
