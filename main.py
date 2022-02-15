from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/')
def page1():
    return '<H1>Миссия Колонизация Марса</H1>'


@app.route('/index')
def page2():
    return '<H1>И на Марсе будут яблони цвести!</H1>'


@app.route('/promotion')
def page3():
    ans = '<br>'.join(['Человечество вырастает из детства.',
                       'Человечеству мала одна планета.',
                       'Мы сделаем обитаемыми безжизненные пока планеты.',
                       'И начнем с Марса!',
                       'Присоединяйся!'])
    return ans


@app.route('/image_mars')
def page4():
    page = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Привет, Марс!</title>
        <meta charset="utf-8">
    </head>
    <body>
        <H1>Жди нас, Марс!</H1>
        <IMG SRC="{url_for('static', filename='img/mars.png')}">
    </body> 
    </html>'''
    return page


@app.route('/promotion_image')
def page5():
    page = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Привет, Марс!</title>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
        </head>
        <body>
            <H1>Жди нас, Марс!</H1>
            <IMG SRC="{url_for('static', filename='img/mars.png')}">
        <p>
            <div class="alert alert_dark" role="alert">
            Человечество вырастает из детства.
            </div>
            <div class="alert alert_success" role="alert">
            Человечеству мала одна планета
            </div>
            <div class="alert alert_secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
            </div>
            <div class="alert alert_warning" role="alert">
            И начнем с Марса!
            </div>
            <div class="alert alert_danger" role="alert">
            Присоединяйся!
            </div>
        </p>
        </body> 
        </html>'''
    return page


@app.route('/choice/<planet_name>')
def choice(planet_name):
    Planets = {
        'Марс': 'Эта планета близка к земле',
        'Земля': 'Лучшая планета для жизни',
        'Нептун': 'Планета то существует, то не существует в солничной системе'
    }
    Planets1 = {
        'Марс': 'На ней много необходимых ресурсов',
        'Земля': 'На ней живёт много людей',
        'Нептун': 'Интересная газовая планета'
    }
    Planets2 = {
        'Марс': 'На ней есть вода и атмосфера',
        'Земля': 'Перспективная планета для освоения ресурсов',
        'Нептун': 'Самая маленькая планета'
    }

    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Ваш вариант: {planet_name}</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}!</h1>
                  <p>
                      <div class="alert alert_dark" role="alert">
                      {Planets[planet_name]}
                      </div>
                      <div class="alert alert_success" role="alert">
                      {Planets1[planet_name]}
                      </div>
                      <div class="alert alert_secondary" role="alert">
                      {Planets2[planet_name]}
                      </div>
                  </p>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <label>Фамилия</label>
                                    <br><input type="text" name="fam">
                                    <br><label>Имя</label><br>
                                    <input type="text" name="name">
                                    <br>
                                    <br><input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Высшее</option>
                                          <option>Среднее</option>
                                          <option>Без образования</option>
                                        </select>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prophecy" name="prophecy">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prophecy" name="prophecy">
                                        <label class="form-check-label" for="acceptRules">пилот</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prophecy" name="prophecy">
                                        <label class="form-check-label" for="acceptRules">строитель</label>
                                     </div>

                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prophecy" name="prophecy">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                     </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['fam'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['prophecy'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
