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
