from flask import Flask, jsonify, request

app = Flask(__name__)

spisok = [
    {'id': 1, 'name': 'Артем', 'familia': 'Дегтярев', 'country': 'Россия', 'city': 'Москва', 'date_start': '2023-10-26', 'date_end': '2023-10-30'},
    {'id': 2, 'name': 'Антон', 'familia': 'Дегтярев', 'country': 'Франция', 'city': 'Париж', 'date_start': '2024-01-15', 'date_end': '2024-01-20'},
    {'id': 3, 'name': 'Артур', 'familia': 'Дегтярев', 'country': 'Италия', 'city': 'Рим', 'date_start': '2024-03-08', 'date_end': '2024-03-12'}
]

@app.route('/zap', methods=['GET', 'POST'])
def zap_func():
    if request.method == 'GET':
        return jsonify(spisok)
    elif request.method == 'POST':
        data = request.get_json()
        spis = {
            'id': len(spisok) + 1,
            'name': data['name'],
            'familia': data['familia'],
            'country': data['country'],
            'city': data['city'],
            'date_start': data['date_start'],
            'date_end': data['date_end']
        }
        spisok.append(spis)
        return jsonify(spis), 201


@app.route('/del/<int:spisok_id>', methods=['DELETE'])
def del_func(spisok_id):
    spisok_id -= 1
    if spisok_id < 0 or spisok_id >= len(spisok):
        return jsonify({'error': 'Плохие данные'}), 404
    del spisok[spisok_id]
    return jsonify({'message': 'Данные удалены'}), 204

@app.route('/update/<int:spisok_id>', methods=['PUT'])
def update_func(spisok_id):
    spisok_id -= 1
    if spisok_id < 0 or spisok_id >= len(spisok):
        return jsonify({'error': 'Плохие данные'}), 404

    data = request.get_json()
    spisok[spisok_id]['name'] = data.get('name', spisok[spisok_id]['name'])
    spisok[spisok_id]['familia'] = data.get('familia', spisok[spisok_id]['familia'])
    spisok[spisok_id]['country'] = data.get('country', spisok[spisok_id]['country'])
    spisok[spisok_id]['city'] = data.get('city', spisok[spisok_id]['city'])
    spisok[spisok_id]['date_start'] = data.get('date_start', spisok[spisok_id]['date_start'])
    spisok[spisok_id]['date_end'] = data.get('date_end', spisok[spisok_id]['date_end'])
    return jsonify(spisok[spisok_id]), 200

if __name__ == '__main__':
    app.run(debug=True)