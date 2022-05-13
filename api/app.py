from flask import Flask, request, jsonify

app = Flask(__name__)

productList = [
    {
      "key": 1,
      "productName": "Book",
      "description": "Leather bound, soft paper",
      "price": 10,
    },
    {
      "key": 2,
      "productName": "Phone",
      "description": "Suspiciously low cost phone",
      "price": 399,
    },
    {
      "key": 3,
      "productName": "Desk",
      "description": "Just as good as the real oak",
      "price": 99,
    },
    {
      "key": 4,
      "productName": "Weird thing",
      "description": "Unknown materials used",
      "price": 1025,
    },
]

@app.route('/search', methods=['GET'])
def getProduct():
    searchTerm = request.get_json()
    itemsFound = []
    for product in productList:
        if searchTerm["searchTerm"].lower() in product["productName"].lower():
            itemsFound.append(product)
    if len(itemsFound) > 0:
        return jsonify(itemsFound)
    return('Not found')

# Searchbar endpoint receives a string and returns a list of product names that match
@app.route('/searchBar', methods=['GET'])
def searchBar():
    searchTerm = request.get_json()
    itemsFound = []
    for product in productList:
        if searchTerm["searchTerm"].lower() in product["productName"].lower():
            itemsFound.append(product["productName"])
    if len(itemsFound) > 0:
        return jsonify(itemsFound)
    return('Not found')


if __name__ == '__main__':
    app.run(debug=True)