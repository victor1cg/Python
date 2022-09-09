#! Ainda Não funciona completamente !#
#! Criando o database via Terminal

No terminal Python:
In [1]: from app_copy import db
In [2]: db.create_all()
In [3]: from app_copy import User, Reward

>> one = User(name='Joao',role ='seller',password='1234')
>> two = Sellout(id_user = 1 ,name_product='LAC12',qty = 87)
db.session.add_all([one,two])
db.session.commit()

>> first = Reward(name_reward = 'Reward Money',user = one)
>> second = Reward(name_reward = 'Reward Travel',user = two)
db.session.commit()

### Criar uma API LOCAL ###
app = Flask(__name__)
@app.route(‘/’)
def hello_world():
    return ‘Hello, World!’
if __name__ == ‘__main__’:
    app.run(debug=True)


