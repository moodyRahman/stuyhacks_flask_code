
from flask import *
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    return {
        "current_date":date_time
    }

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html")



@app.route("/poke", methods=["POST"])
def poke():
    print("THIS IS THE FORM ATTACHED TO THIS REQUEST", request.form)
    poke = requests.get('https://pokeapi.co/api/v2/pokemon/{pokemon}'.format(pokemon=request.form["pokemon_query"]))
    
    if (poke.status_code == 404):
        return render_template("error.html")
    
    poke_data = poke.json()
    abilites = poke_data["abilities"]
    print(abilites)
    abilites_clean = [x["ability"]["name"] for x in abilites]
    
    # abilites_clean = []    
    # for x in abilites:
    #     abilites_clean.append(x["ability"]["name"])
    
    return render_template("ditto.html", abilites=abilites_clean, name=poke_data["name"])



if __name__ == '__main__':
    app.run(debug=True)
    
