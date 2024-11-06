## Import flask
from flask import Flask, request  # type: ignore

app = Flask(__name__)


## Basic Routes
@app.route('/')
def hello():
    return ("Hello world")


@app.route("/welcome")
def welcome():
    return ("Welcome to the API!")


@app.route("/goodbye")
def goodbye():
    return ("Goodbye from the API!")


# 2. GET and POST REQUESTS
@app.route("/info", methods=["GET"])
def info():
    return ("Send a POST request with your name and age.")


@app.route("/submit", methods=["POST"])
def handle_submit():
    data = request.json
    title = data.get("title")
    year = data.get("year")
    if not title or not year:
        return {"Error": "Title and year are required"}, 400
    else:
        return {"Message": f"The book is, {title} and was published year {year}"}


## 2. Handle different HTTP Methods
@app.route("/data", methods=["POST"])
def handle_data():
    data = request.json  # type: ignore
    return {
        "message": "Data Recieved succesfully",
        "data": data,
    }


## 3. Dynamic route parameter parsing
@app.route("/greet/<username>", methods=["POST", "GET"])
def greet_user(username):
    age = request.args.get("age")
    if username and username.isalpha():
        if request.method == 'POST':
            if age:
                return {"Message": f"Hello, {username} You are {age} years old!"}
            else:
                return {"Message": f"Hello, {username}"}
        if request.method == "GET":
            return (f"Hello {username}!")
    else:
        return {"error": "Invalid username."}, 400


## 4. CRUD Operations Simulation
# users_list_format={
#     "id": int,
#     "name": str,
#     "favorite_color": str
#     }
List_example_one = {"id": 1, "name": "sarah","age": 23, "favorite_color": "red"}
List_example_two = {"id": 2, "name": "Marc","age": 18, "favorite_color": "blue"}
user_list = []
user_list.append(List_example_one)
user_list.append(List_example_two)

def exists_usr_name(name):
    for i in user_list:
        if i["name"]==name: # if Username exists, return True
            return True
        else:
            return False
def exists_usr_id(id):
    for i in user_list:
        if i["id"]==id: # if user id exists, return True
            return i

def unique_usr_id(list):
    id = max(i["id"] for i in list)
    return (id + 1)


@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == 'GET':
        return (user_list)
    elif request.method == "POST":
        data = request.json
        # id=data.get("id")
        name = data.get("name")
        color = data.get("favorite_color")
        age = data.get("age")
        if name and color:
            new_user = {
                "id": int(unique_usr_id(user_list)),
                "name": name,
                "favorite_color": color,
                "age": age
            }
        user_list.append(new_user)
        return user_list

@app.route("/users/<user_id>", methods=["PUT", "GET", "DELETE"])
def user_id_mgmt(user_id):
    data = request.json
    if request.method == "PUT":
        usrfnd=exists_usr_id(int(user_id))
        if usrfnd:
            v_name=data.get("name")
            v_age=data.get("age")
            if not v_name and not v_age:
                return "You need to provide name or age, or both."
            if v_name:
                usrfnd.update({"name": v_name})
            if v_age:
                usrfnd.update({"age": v_age})
            if v_age or v_name:
                user_list.append()
            return user_list
        else:
            return f"String was returned empty {usrfnd}, user ID provided: {user_id}"
    if request.method == "GET":
        for i in user_list:
            if i["id"]==int(user_id):
                return f"Found user {i}"
        return f"No user exists with the id {user_id}"
    if request.method == "DELETE":
        usrfnd=exists_usr_id(int(user_id))
        if usrfnd:
            x=user_list.remove(usrfnd)
            if x:
                return ("User has been succesfull deleted")
            else:
                return ("failed removing user")
        else:
            return "No such users exists."