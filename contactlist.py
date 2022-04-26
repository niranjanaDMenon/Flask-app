from flask import Flask,jasonify,request

contactlist=Flask(__name__)


tasks = [

{

"id"=1,
"name"="Sreelakshmi",
"number"="9447881485"

}
{

"id"=2,
"name"="Deepesh",
"number"="9895055277"

}

{
"id"=3,
"name"="neghibour's Landline",
"number"="2282555"

}

]


GET,PUT,POST,DELETE
@contactlist.route("/add-data",methods="POST")

def add_task():
    if not request.jason:
        return jasoinify(
           {'status':'error',"message":"PLEASE PROVIDE SOME DATA FOR YOUR INFORMATION !"} ,
            400 )
