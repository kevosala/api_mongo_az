from flask import Flask, request,jsonify,Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_pymongo.wrappers import MongoClient

app = Flask(__name__)
uri = "mongodb://db-mongo-testing:eUBR2eC7siOk9KdWE6RqUgPnux9rOXjmLU1QUgJsVMFQWwB7TiaIekamhWozeKt6AB8htUAvTOtGdnmx5RPiTA==@db-mongo-testing.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@db-mongo-testing@" #Primary Connection String
client = MongoClient(uri) #Se instancia el cliente de mongoDB
db = client.dbmongopy #Seleccionar la base de datos 
azData = db.inventory #Seleccionar la colección



@app.route('/inventory',methods=['POST'])
def create_item():
    item = request.json['item']
    qty = request.json['qty']
    status = request.json['status']

    if item and qty and status:
        id = azData.insert(
            {'item':item,'qty':qty,'status':status}
        )
        response = {
            'id': str(id),
            'item': item,
            'qty': qty,
            'status': status
        }
        return response
    else:
        return not_found()

    return {'message':'received'}

@app.route('/inventory', methods=['GET'])
def get_items():
    items = azData.find()
    response = json_util.dumps(items)
    return Response(response,mimetype='application/json')
    
@app.route('/inventory/<id>', methods=['GET'])
def get_item(id):
    item = azData.find()
    response = json_util.dumps(item) #Convierte en un json
    return Response(response,mimetype='application/json')

@app.route('/inventory/<id>', methods=['DELETE'])
def delete_item(id):
    azData.delete_one({'_id':ObjectId(id)})
    response = jsonify({'message': 'Item ' + id + 'was Deleted succesfully'})
    return response

@app.route('/inventory/<id>', methods=['PUT'])
def update_item(id):
    item = request.json['item']
    qty = request.json['qty']
    status = request.json['status']

    if item and qty and status:
        azData.update_one({'_id':ObjectId(id)}, {'$set': {
            'item': item,
            'qty': qty,
            'status': status
        }})
        response = jsonify({'message': 'Item ' + id + 'was Updated succesfully'})
        return response

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource not found: ' + request.url,
        'status':404
    })
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True)