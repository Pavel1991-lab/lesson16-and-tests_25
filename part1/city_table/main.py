# Городская таблица
# Определите поля для модели City по таблице city:
# +----+---------+------------+------------+
# | id |   name  | country_ru | population |
# +----+---------+------------+------------+
# | 1  |   Рим   |   Италия   |  2873000   |
# | 2  |  Милан  |   Италия   |  1333000   |
# | 3  | Венеция |   Италия   |   265000   |
# +----+---------+------------+------------+
#
#
import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



with app.app_context():
    class City(db.Model):
        __tablename__ = 'city'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        country_ru = db.Column(db.String(100))
        population = db.Column(db.Integer)


    db.drop_all()
    db.create_all()


    # TODO определите поля модели здесь


# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла
with app.app_context():

    db.create_all()
    session = db.session()
    cursor = session.execute(text(f"SELECT * from {City.__tablename__}")).cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
