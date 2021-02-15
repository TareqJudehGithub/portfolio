from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    """Main webpage"""
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    """Accessing HTML pages dynamically:"""
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        name = data["username"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(
            f"\n"
            f"Name:    {name}\n"
            f"Email:   {email}\n"
            f"Subject: {subject}\n"
            f"Message: {message}\n"
        )


def write_to_csv(data):
    with open("database.csv",  newline="", mode="a") as database2:
        name = data["username"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(
            database2,
            delimiter=",",  # separator type .
            quotechar="'",  # quote type for special characters.
            quoting=csv.QUOTE_MINIMAL
        )

        # contain the data we need and save it:
        csv_writer.writerow(
            [
                name,
                email,
                subject,
                message
            ]
        )


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Flask requests"""
    if request.method == "POST":
        data = request.form.to_dict()
        name = request.form["username"]

        write_to_csv(data)

        # return redirect("/thankyou.html")
        return render_template("thankyou.html", name=name)

    else:
        return "Something went wrong."


if __name__ == '__main__':
    app.run()

