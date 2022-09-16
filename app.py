#http://127.0.0.1:5000/api/v1/resources/data?distance=1200 -- url to check reponse

from crypt import methods
from flask import Flask, jsonify,request

app=Flask(__name__)

def create_data():
    data =[
        {
            "order_items": [
                {
                "name": "bread",
                "quantity": 2,
                "price": 2200
                },
                {
                "name": "butter",
                "quantity": 1,
                "price": 5900
                }
            ],
            "distance": 1200,
            "offer": {
                "offer_type": "FLAT",
                "offer_val": 1000
            }
            ,
            "order_items": [
                {
                "name": "bread",
                "quantity": 2,
                "price": 2200
                },
                {
                "name": "butter",
                "quantity": 1,
                "price": 5900
                }
            ],
            "distance": 1250,
            "offer": {
                "offer_type": "DELIVERY",
                "offer_val": 1000
            }
        }
    ]
    return data

@app.route('/')
def index():
    return "Welcome"

    

@app.route('/api/v1/resources/data/all', methods=['GET'])
def api_all():
    return jsonify(create_data)


def calculate_cost(dist):

    data=create_data()
    for book in data:

        item_cost=0
        for i in book['order_items']:
            item_cost+=i['price']*i['quantity']
        print(item_cost)

        delivery_charge=0
        
        if(dist>=50000):
            delivery_charge=1000
        
        elif (dist>=20000 and dist<50000):
            delivery_charge=500

        elif (dist>=10000 and dist<20000):
            delivery_charge=100

        else:
            delivery_charge=50
        

        print(delivery_charge*100)

        if book["offer"]['offer_type']=='FLAT':
            discount = book["offer"]['offer_val']
        elif book["offer"]['offer_type']=='DELIVERY':
            discount=delivery_charge*100

        total_cost=item_cost+(delivery_charge*100)-discount
        print(total_cost)

        total_cost={'order_total':total_cost}
        return total_cost


@app.route('/api/v1/resources/data', methods=['GET'])
def api_id():

    if 'distance' in request.args:
        dist = int(request.args['distance'])
    else:
        return "Error: No id field provided. Please specify an id."

    return jsonify(calculate_cost(dist))


if __name__=="__main__":
    app.run(debug=True)