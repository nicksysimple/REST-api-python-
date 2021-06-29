from flask import Flask

app = Flask(__name__)
#create a store
@app.route('/store',methods = ['POST'])
def create_store():
    pass

#fetch a store
app.route('/store/<string:name>')
def get_store(name):
    pass


#get stores
app.route('/store')
def get_store():
    pass

#create an item
@app.route('/store/<string:name>/item',method = ['POST'])
def create_item_in_store():
    pass


#get items in store
app.route('/store/<string:name>/item')
def get_items_in_store():
    pass


app.run(port=5000)
