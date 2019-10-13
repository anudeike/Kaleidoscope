from flask import Flask, render_template
from flask import flash, url_for
from flask import redirect
from testScript import sayHello # it works!
from forms import GeneratorForm
app = Flask(__name__)

#config stuff
app.config['SECRET_KEY'] = '637b57da81bd97bf47f971161a050c0d530238d7784692a72aa1cddcf3d4d38b'

@app.route("/")
@app.route("/home")
def home():
    sayHello()
    return render_template("home.html")

# main app route (for the entry into the app)
@app.route("/app", methods=['GET', 'POST'])
def application():
    form = GeneratorForm()

    # tell if the form is valid
    if form.validate_on_submit():
        # the second string is the bootstrap class you want to use
        flash(f'Query recieved: {form.query.data}!', 'success')

        # print into the console
        return redirect(url_for('home'))
    return render_template("app.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

# run the actual server
if __name__ == "__main__":
    app.run(debug=True)