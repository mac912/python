import json as simplejson
import os
if os.path.isfile("./score.json") and os.stat("./score.json").st_size!=0:
    oldfile = open("./score.json", "r+")
    data = simplejson.loads(oldfile.read())
    print("current age is ", data["age"])
    data["age"] = data["age"]+"1"
    print("after adding one year", data["age"])
else:
    oldfile = open("./score.json", "w+")
    data = {"name":"manish", "age": 20}
    print("no such file found", data["age"])

oldfile.seek(0)
oldfile.write(simplejson.dumps(data))
