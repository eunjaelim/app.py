from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    review_receive = request.form['review_give']

    doc = {
        'title':title_receive,
        'review':review_receive
    }

    db.dict.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.dict.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


@app.route('/api/delete', methods=['POST'])
def delete_reviews():
    title_receive = request.form['title_give']
    db.dict.delete_one({'title': title_receive})
    return jsonify({'msg': '삭제 완료!'})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)