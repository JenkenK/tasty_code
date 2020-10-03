from flask import Flask, render_template

from controllers.customer_controller import customers_blueprint
from controllers.cuisine_controller import cuisine_blueprint

app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(cuisine_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)