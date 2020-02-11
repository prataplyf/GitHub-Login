from flask import Flask, redirect, url_for, request
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.config['SECRET_KEY']= 'thisissecretkey'

# Github client ID and client secet Key
github_blueprint = make_github_blueprint(client_id='your client ID', client_secret='Your Client secret Key')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

# https://github.com/settings/applications/1219523
# to get emailid and name such variable
# https://developer.github.com/v3/users/
@app.route('/github')
def github_login():
    if not github.authorized:
        # after login we need to authorized the account
        # to authorize write the foliwing code (export OAUTHLIB_INSECURE_TRANSPORT=1) on the terminal
        # where this file execute...
        return redirect(url_for('github.login'))
    account_info = github.get('/user')
    if account_info.ok:
        account_info_json = account_info.json()
        return '<h1>export OAUTHLIB_INSECURE_TRANSPORT=1<br>Your Github name is <font color="blue">{}</font><br>Email ID <font color="blue">{}</font></h1>'.format(account_info_json['login'],account_info_json['email'])
    return '<h1>Request failed!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
