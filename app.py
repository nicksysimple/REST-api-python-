from flask import Flask,jsonify
#list of stores with dictionaries inside
stores = [

    {
        'name':'My wonderfull store',
        'items':[
            #list of items with a dictionary inside of name and price
            {
                'name':'My item',
                'price':10.5
            }
        ]

    }
]



app = Flask(__name__)

@app.route("/")
def home():
    return "hello rest"
@app.route('/store',methods = ['POST'])
def create_store():
    pass

#fetch a store
@app.route('/store/<string:name>')
def get_store(name):
    pass

#get stores
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

#create an item
@app.route('/store/<string:name>/item',methods = ['POST'])
def create_item_in_store(name):
    pass


#get items in store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass



# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#      return "<p>Hello, World!</p>"
