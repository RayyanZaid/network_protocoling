import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load groups from file if it exists, otherwise start with an empty list
try:
    with open('groups.pickle', 'rb') as f:
        groups = pickle.load(f)
except FileNotFoundError:
    groups = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    group_name = request.form['group_name']
    groups.append(group_name)
    # Save groups to file after adding new group
    with open('groups.pickle', 'wb') as f:
        pickle.dump(groups, f)
    return render_template('create.html', group_name=group_name)

@app.route('/join', methods=['POST'])
def join():
    group_name = request.form['group_name']
    if group_name not in groups:
        return render_template('join.html', error='Group does not exist')
    return render_template('join.html', success=True, group_name=group_name)

@app.route('/groups')
def list_groups():
    return render_template('list_groups.html', groups=groups)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
