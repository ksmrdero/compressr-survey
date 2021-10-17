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
    for k, rank in data.items():
        # ex: https://compressrimages.blob.core.windows.net/801/bmshj2018-factorized2/0.png
        img_set, model, name = k.split('/')[-3:] 
        db.insert(
            imageSet=int(img_set), 
            imageName=int(name.split('.')[0]),
            rank=int(rank), 
            model=model
        )

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
