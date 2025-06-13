from flask import Flask, render_template_string, request, redirect
from flask_cors import CORS
import datetime
import subprocess
from html import escape


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
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
    data = [f'''
        <div class="container">
            <h3>{post["title"]}</h3>
            <p>{post["body"]}</p>
            <p style="color:gray;">Created at: {post["created"]}</p>
            <img src="/images/{post["image"]}" class="img-fluid" alt="Responsive image">
        </div>
    ''' for post in content]
    return render_template_string('''
        {% extends 'base.html' %}

        {% block content %}
        ''' + "\n".join(data) + '''
        {% endblock %}
    ''')

@app.route('/new')
def new():
    invitation = request.args.get('invitation')
    return render_template_string('''
        {% extends 'base.html' %}

        {% block content %}
        <div class="content">
            <h2>New Post</h2>
            ''' + (f'<p>Invitation code: {invitation}</p>' if invitation else '') + '''
            <form action="/api/new" method="post">
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" id="title" name="title">
                </div>
                <div class="form-group">
                    <label for="body">Body</label>
                    <textarea class="form-control" id="body" name="body" rows="3"></textarea>
                </div>
                <div class="form-group">
                    <label for="image">Image</label>
                    <input type="text" class="form-control" id="image" name="image">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        {% endblock %}
    ''')

@app.route('/images/<path:path>')
def images(path):
    res = subprocess.run(['curl', f'{path}'], stdout=subprocess.PIPE)
    return res.stdout

@app.route('/api/new', methods=['POST'])
def api_new():
    title = escape(request.form.get('title'));
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
