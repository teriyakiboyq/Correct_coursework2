from flask import Flask, render_template, request, jsonify
from dao.candidates_dao import CandidatesDAO

app = Flask(__name__)
candidate_dao = CandidatesDAO('./data/data.json', './data/comments.json')


@app.route("/")
def page_index():
    post = candidate_dao.get_all()
    return render_template('index.html', posts=post)


@app.route('/posts/<int:uid>')
def load_posts(uid):
    post = candidate_dao.get_post_by_pk(uid)
    comment = candidate_dao.get_posts_by_comments(uid)
    return render_template('post.html', comment=comment, posts=post, comment_len=len(comment))


@app.route('/search/')
def search():
    search_by = request.args['s']
    if search_by:
        posts = candidate_dao.search_for_posts(search_by)
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts, posts_len=len(posts))


@app.route('/feed/<name>')
def user_feed(name):
    user_name = candidate_dao.get_posts_by_user(name)
    return render_template('user-feed.html', user_name=user_name)


@app.route("/api/posts")
def index_test():
    posts = candidate_dao.get_all()
    return jsonify(posts)


@app.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = candidate_dao.get_post_by_pk(uid)
    return jsonify(post)


if __name__ == "__main__":
    app.run()
