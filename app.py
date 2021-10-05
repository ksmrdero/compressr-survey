from flask import Flask, request, render_template, redirect, url_for
from sqldb import SqlDb
from util import retrieve_imgs

app = Flask(__name__)
db = SqlDb()

@app.route('/')
def home():
    imgs = retrieve_imgs()
    data = {'img'+ str(i) : imgs[i] for i in range(len(imgs))}
    return render_template('index.html', data=data)

@app.route('/forward/', methods=["POST"])
def insert():
    data = request.form

    if len(set(data.values())) != 4:
        return redirect(url_for('home'))

    for k, rank in request.form.items():
        img_set, name = k.split('/')[-2:]
        db.insert(int(img_set), int(name.split('.')[0]), int(rank))

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(threaded=True)
