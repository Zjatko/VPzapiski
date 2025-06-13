from flask import Flask, render_template, request, redirect
import datetime
import subprocess

app = Flask(__name__)
content = [
    {
        'title': 'First Post',
        'body': 'This is my first post!',
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'image': 'https://via.placeholder.com/150',
    },
]

@app.route('/')
def index():
    return render_template('index.html', content=content)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/images/<path:path>')
def images(path):
    res = subprocess.run(['curl', f'{path}'], stdout=subprocess.PIPE)
    return res.stdout

@app.route('/api/new', methods=['POST'])
def api_new():
    title = request.form.get('title')
    body = request.form.get('body')
    image = request.form.get('image')
    content.append({
        'title': title,
        'body': body,
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'image': image,
    })
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
