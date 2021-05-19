import csv
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if(username == "user" and password == "password"):
        return render(request,"dashboard.html")
    else:
        return render(request,"index.html",{"errorMessage":"Either Username or Password is Wrong"})

def readURL():
    with open("C:/sers/vikas/Desktop/myProject/vikasSingh/url.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        li = []
        for row in csv_reader:
            li.append(row[0])
        return (li)
    