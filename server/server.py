from datetime import date
from flask import Flask, jsonify, request
from subprocess import run
from os import chdir

app = Flask("Лабораторная Работа 1. Гутник Вадим")

class Phone:
    def __init__(self, TypeID: int, CountryCode: int, Operator: int, Number: int):
        self.TypeID = TypeID
        self.CountryCode = CountryCode
        self.Operator = Operator
        self.Number = Number

class Contact:
    def __init__(self, ID: int, Username: str, GivenName: str, FamilyName: str,
                 Phone: dict, Email: str, Birthdate: date):
        self.ID = ID
        self.Username = Username
        self.GivenName = GivenName
        self.FamilyName = FamilyName
        self.Phone = Phone
        self.Email = Email
        self.Birthdate = Birthdate

class Group:
    def __init__(self, ID: int, Title: str, Description: str, Contacts: [int]):
        self.ID = ID
        self.Title = Title
        self.Description = Description
        self.Contacts = Contacts

# for github
@app.route('/webhook', methods=["POST"])
def webhook():
    if request.headers.get("X-GitHub-Event") == "push":
        chdir("/server")

        run(["git", "pull"])

        run(["pkill", "-f", "python server.py"])
        run(["python", "server.py"])

        return jsonify({"status": "success", "message": "Application updated and restarted"}), 200
    
    return jsonify({"status": "ignored", "message": "Not a push event"}), 200

# WORK WITH OBJECTS

def return_contact():
    return jsonify(Contact(0, "Vadim", "Vadimka", "Vadik",
                   Phone(0, 0, 0, 0).__dict__, "dsrase201@gmail.com", date.today()).__dict__)

def return_group():
    return jsonify(Group(0, "TEST", "LABA", [0, 0, 0]).__dict__)


# =====================================================CONTACT==========================================================
@app.route("/api/v1/contact", methods=["PUT"])
def put_contact():
    return return_contact()

@app.route("/api/v1/contact", methods=["POST"])
def post_contact():
    return return_contact()

@app.route("/api/v1/contact", methods=["DELETE"])
def delete_contact():
    return return_contact()

@app.route("/api/v1/contact") # GET by default
def get_contact():
    return return_contact()

# =====================================================GROUPS===========================================================


@app.route("/api/v1/group", methods=["PUT"])
def put_group():
    return return_contact()

@app.route("/api/v1/group", methods=["POST"])
def post_group():
    return return_contact()

@app.route("/api/v1/group", methods=["DELETE"])
def delete_group():
    return return_group()

@app.route("/api/v1/group") # GET by default
def get_group():
    return return_group()

if __name__ == "__main__":
    # we need port 6080
    app.run(debug=True, port=6080, host="127.0.0.1")

