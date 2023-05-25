from flask import Flask, render_template, request
import smtplib


FROM_EMAIL = "angela4udemy@gmail.com"
TO_EMAIL = "monthakan.lert@gmail.com"
MY_PASSWORD = "tddjqrjafyawbtsj"


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        msg_sent = "Successful sent your message"

        # sending the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # securing the connection
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: {subject}\n\nName: {name}\nEmail Address: {email}\nMessage: {message}"
            )
        return render_template("index.html", msg_sent=msg_sent)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
