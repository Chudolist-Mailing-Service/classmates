#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Read classmates data from classmates class, display as full list, by group or as individual page.
   Collect facebook ids by controller. 
"""


from flask import Flask, render_template, session, request, url_for, redirect
from operator import itemgetter

from flask_oauthlib.client import OAuth, OAuthException, OAuthResponse
from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, FACEBOOK_CALLBACK

from classmates import Classmates

MAIN_PAGE_TEMPLATE  = "table.html"
GROUP_PAGE_TEMPLATE = "group.html"
USER_PAGE_TEMPLATE  = "user.html"

my_class = Classmates()

application = Flask("application")

# FB auth setup
oauth = OAuth()

facebook = oauth.remote_app(
    'facebook',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'public_profile'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    access_token_method='GET',
    authorize_url='https://www.facebook.com/dialog/oauth'
)
        
@application.route("/")
def hello():
    return render_template(MAIN_PAGE_TEMPLATE, persons=my_class.get_class())
    
@application.route('/user/<username>')
def show_user_profile(username):         
    if username in my_class.get_translit_names():
        p = my_class.get_user(username)
        session['username'] = username
        return render_template(USER_PAGE_TEMPLATE, person=p)        
    else:
        return 'Cannot find %s' % username

@application.route('/group/<int:group_n>')
def show_post(group_n):
    if group_n in [x for x in range(401,412+1)]:
        return render_template(GROUP_PAGE_TEMPLATE, persons=my_class.get_group(group_n))
    else:
        return 'Illegal group number: %d' % group_n
    

# ---- FACEBOOK ----
@application.route('/oauth/authorize/facebook', methods=['GET', 'POST'])
def oauth_authorize_facebook():
    return facebook.authorize(callback=FACEBOOK_CALLBACK)


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('facebook_token')


@application.route('/oauth/callback/facebook/', methods=['GET', 'POST'])
def oauth_authorized_fb():
    next_url = request.args.get('next') or url_for('hello')
    resp = facebook.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    if isinstance(resp, OAuthException):
        return 'OAuthException: %s' % resp.message

    session['facebook_token'] = (resp['access_token'], '')
    me = facebook.get('/me?fields=id')
    fb_id = me.data['id']
    user = session['username']
    
    my_class.set_facebook_id(user,fb_id)
    
    return redirect(next_url)

# ---- END OF FACEBOOK CODE ----


if __name__ == "__main__":
    print()
    application.secret_key = 'super secret key'
    application.run(debug = True)