from flask import Flask, redirect

app = Flask(__name__)

# Programatically create new routes
# https://production-my-menu.herokuapp.com/yanncouvreur
@app.route('/yanncouvreur')
def redirect_to_menu():
    # This function should find the latest menu available

    return redirect("https://ycharrods1.s3.eu-west-2.amazonaws.com/Menus/Menu+YCH.pdf")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
