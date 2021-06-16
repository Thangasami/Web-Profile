from flask import Flask, redirect, url_for, render_template, send_file

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("front.html")
@app.route("/app")
def ad():
    return "Hi Everyone. this is inside app"
@app.route("/")
def hm():
    return render_template("front.html")
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
@app.route("/exp")
def exp():
    return render_template("contact.html")
@app.route("/reach")
def reach():
    return render_template("reach.html")
@app.route("/gal")
def gal():
    return render_template("gallery.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/download")
def download_file():
    p = "resume.pdf"
    return send_file(p,as_attachment=True)


if __name__ == "__main__":
    app.run()