from flask import render_template, Blueprint
from ..requests import get_quote

from flask import render_template, request, redirect, url_for

# Views
main = Blueprint('main', __name__)


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title_dict = get_quote()
    title = title_dict["quote"]
    author = title_dict["author"]
    return render_template('index.html', title=title, author=author)


@main.route('/movie/<int:quote_id>')
def quote(quote_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('qoute.html', id=quote_id)
