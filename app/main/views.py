from flask import render_template, Blueprint

from app.models import Blog, User, Comment
from ..requests import get_quote
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm
from .. import db
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


@main.route('/new/blog', methods=['GET', 'POST'])
@login_required
def new_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data

        new_blog = Blog(body=title, content=blog,
                        user_id=current_user.id, likes=0, dislikes=0)

        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'new.blog'

    return render_template('newblog.html', title=title, blog_form=blog_form)


@main.route('/blog/<int:id>', methods=['GET', 'POST'])
@login_required
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.timestamp.strftime('%b %d,%Y')

    if request.args.get('likes'):
        blog.likes = blog.likes+1

        db.session.add(blog)
        db.session.commit()
        return redirect('/blog/{blog_id}'.format(blog_id=blog.id))

    elif request.args.get('dislikes'):
        blog.dislikes = blog.dislikes+1

        db.session.add(blog)
        db.session.commit()
        return redirect('/blog/{blog_id}'.format(blog_id=blog.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        new_comment = Comment(
            comment=comment, user=current_user, blog_id=blog)

        new_comment.save_comments()

    comments = Comment.get_comments(blog)
    return render_template('userposts.html', blog=blog, comment_form=comment_form, comment=comments, date=posted_date)
