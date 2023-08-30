from flask import Flask, render_template, url_for


app = Flask(__name__)


menu = ['Группы', 'Чаты', 'Профиль']


@app.route('/')
async def index():
    print(url_for('index'))
    return render_template('index.html', title='NotNotion', menu=menu)


@app.route('/about')
async def about():
    return render_template('about.html', title='О сервисе')


if __name__ == '__main__':
    app.run(debug=True)
