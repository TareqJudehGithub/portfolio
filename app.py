from flask import Flask, render_template, request, redirect
from time import sleep

app = Flask(__name__)


@app.route("/")
def my_home():
    """Main webpage"""
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    """Accessing HTML pages dynamically:"""
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Flask requests"""
    if request.method == "POST":
        data = request.form.to_dict()
        name = request.form["username"]
        print(data)
        print(name)
        # return redirect("/thankyou.html")

        return render_template("thankyou.html", name=name)


    else:
        return "Something went wrong."


if __name__ == '__main__':
    app.run()
