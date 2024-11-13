from flask import Flask, render_template

app = Flask(__name__)

# функция, которая возвращает список сотрудников
def get_employees():
    employees = [
        {'name': 'Петр Семенов', 'position': 'Директор', 'email': 'ivan@example.com'},
        {'name': 'Настя Тарасова', 'position': 'Менеджер', 'email': 'petr@example.com'},
        {'name': 'Сергей Александров', 'position': 'Разработчик', 'email': 'sergey@example.com'},
        # ...
    ]
    return employees

@app.route('/base/<username>')
def index(username=None):
    employees = get_employees()
    return render_template('base.html', username=username.upper(), employees=employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)