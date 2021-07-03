#!/usr/bin/python3

from flask import Flask
from flask import json
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

ontap_now = [{"Tap_position": "1", "Name": "Graf", "Description": "50% beer,50% cider. large malt up front, clean appley finish"},{"Tap_position": "2", "Name": "IPA", "Description": "American IPA well balanced malt, body and hops (Cascade, Chinook, Citra)"},{"Tap_position": "3", "Name": "Cream Ale", "Description": "Light and refreshing ale. perfect for hot summer days"},{"Tap_position": "4", "Name": "Dry Irish Stout", "Description": "Dark, malty and full bodied. everything you would expect from a dry stout"},{"Tap_position": "5", "Name": "Peach Iced Tea", "Description": "Non-Alcoholic flavored iced tea.  don't judge me ..."}]

coming_soon = [{"Name": "New England Hazy IPA", "Description": "Juicy and bitter in just the right ratio"},{"Name": "English IPA", "Description": "Taditional English IPA like they used to make it"},{"Name": "Hefeweisen", "Description": "Traditional German Weiss beer. hints of banana (cause cloves are yucky)"}]

suggestion_box = [{"Name": "Brent", "suggestion": "Start an Octoberfest now so its ready in time!"}]

# if user sends GET to /ontap
@app.route("/ontap")
def ontap():
    json_ontap = []
    for d in ontap_now:
        ontap_dict = {}
        ontap_dict["Tap_position"] = d["Tap_position"]
        ontap_dict["Name"] = d["Name"]
        ontap_dict["Description"] = d["Description"]
        json_ontap.append(ontap_dict)
    return json.dumps(json_ontap, sort_keys=False)

# if user sends GET to /comingsoon
@app.route("/comingsoon")
def comingsoon():
    json_comingsoon = []
    for d in coming_soon:
        comingsoon_dict = {}
        comingsoon_dict["Name"] = d["Name"]
        comingsoon_dict["Description"] = d["Description"]
        json_comingsoon.append(comingsoon_dict)
    return json.dumps(json_comingsoon, sort_keys=False)

# if user sends GET to /comingsoon
@app.route("/suggestionbox")
def suggestionbox():
    json_suggestionbox = []
    for d in suggestion_box:
        suggestionbox_dict = {}
        suggestionbox_dict["Name"] = d["Name"]
        suggestionbox_dict["suggestion"] = d["suggestion"]
        json_suggestionbox.append(suggestionbox_dict)
    return json.dumps(json_suggestionbox, sort_keys=False)

# if user makes a suggestion
@app.route("/makesuggestion", methods = ["POST"])
def makesuggestion():
    content = request.json
    new_suggestion = {}
    new_suggestion["Name"] = content["Name"]
    new_suggestion["suggestion"] = content["suggestion"]
    suggestion_box.append(new_suggestion)
    # I'm not sure why the client doesnt get this?
    return "Your suggestion has been received! Thank you."


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
