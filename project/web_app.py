from flask import Flask, render_template
app = Flask(__name__)

@app.route("/contact")
def coco():
   return render_template("contactme.html")


@app.route("/about")
def abab():
   return render_template("aboutme.html")


@app.route("/home")
def hoho():
   return render_template("home.html")


@app.route("/painting")
def papa():
   return render_template("mypainting.html")














if __name__ == "__main__":
	app.debug = True    
	app.run()
