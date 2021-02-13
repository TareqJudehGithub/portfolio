from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_home():
    """Main webpage"""
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    """Accessing HTML pages dynamically:"""
    return render_template(page_name)


if __name__ == '__main__':
    app.run()
