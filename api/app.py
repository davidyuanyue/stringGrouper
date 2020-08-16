from flask import Flask, request, jsonify
from flask_cors import CORS
from service import StringGrouper
app = Flask(__name__)
CORS(app)

@app.route("/stringGroup", methods=['POST'])
def stringGroup():
    list_of_string = request.json
    stringGrouper = StringGrouper(list_of_string)
    string_group_by_prefix = stringGrouper.divid_to_groups()
    return jsonify(string_group_by_prefix)

if __name__ == '__main__':
    app.run(debug=True)