from flask import Flask, request, render_template, redirect, url_for, flash
import os

from models import db, Product, Order

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'erp.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'erp-secret-key'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/seller')
def seller():
    products = Product.query.all()
    orders = Order.query.all()
    return render_template('seller.html', products=products, orders=orders)


@app.route('/buyer')
def buyer():
    products = Product.query.all()
    orders = Order.query.all()
    return render_template('buyer.html', products=products, orders=orders)


@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    product = Product(name=name, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    flash(f'✅ تم إضافة المنتج {name}', 'success')
    return redirect(url_for('seller'))


@app.route('/update_quantity', methods=['POST'])
def update_quantity():
    product_id = int(request.form['product_id'])
    new_quantity = int(request.form['new_quantity'])
    product = Product.query.get(product_id)
    if product:
        product.quantity = new_quantity
        db.session.commit()
        flash(f'✅ تم تحديث كمية {product.name} إلى {new_quantity}', 'success')
    return redirect(url_for('seller'))


@app.route('/delete_product', methods=['POST'])
def delete_product():
    product_id = int(request.form['product_id'])
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash(f'🗑️ تم حذف المنتج {product.name}', 'success')
    return redirect(url_for('seller'))


@app.route('/create_order', methods=['POST'])
def create_order():
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])
    customer_name = request.form.get('customer_name') or 'عميل'

    product = Product.query.get(product_id)
    if product and product.quantity >= quantity:
        product.quantity -= quantity
        order = Order(product_id=product_id, quantity=quantity, customer_name=customer_name)
        db.session.add(order)
        db.session.commit()
        flash(f'✅ تم شراء {quantity} من {product.name} بنجاح', 'success')
    else:
        flash('❌ الكمية المطلوبة غير متوفرة!', 'error')

    return redirect(url_for('buyer'))


def init_db():
    with app.app_context():
        db.create_all()
        if Product.query.count() == 0:
            sample = [Product(name='لابتوب', quantity=10), Product(name='ماوس', quantity=50)]
            db.session.add_all(sample)
            db.session.commit()
            print("✅ تم إضافة منتجات تجريبية")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
