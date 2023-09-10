from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.contrib.sessions.backends.db import SessionStore
import psycopg2
from .utils import register,loginUser,forgate_user_password

try:
    conn = psycopg2.connect(
        host = 'localhost',
        port = '5432',
        user = 'postgres',
        password = 'root',
        dbname = 'mydb'
    )

    conn.autocommit = True

    cur = conn.cursor()
    print("\nDatabase connected...\n")
except Exception as e:
    print("Error : ",e)


s = SessionStore()

def checkSession():
    try:
        email = s['email']
        return True
    except Exception as e:
        print("Error : ",e)
        return False
    

def Home(request):
    return render(request,'home.html')


def registration(request):
    check = checkSession()

    if check == False:
        if request.method == 'POST':
            name = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            contact = request.POST['contact']

            user = {
                'name' : name,
                'email' : email,
                'password' : password,
                'contact' : contact
            }

            print('name :',name)
            print('email :',email)
            print('password :',password)
            print('contact :',contact)

            response = register(user,cur)

            if response['statusCode'] == 200:
                sql = "INSERT INTO register (name,email,password,contact) VALUES (%s,%s,%s,%s)"
                values = (name,email,password,contact)

                cur.execute(sql,values)

                return  redirect('login')
                # return render(requt,'signuesp.html',{'message': 'register'})
            else:
                return render(request,'signup.html',{'message' : 'alredy exist'})
        else:
            return render(request,'signup.html')
    else:
        return render(request,'signup.html')
    

def login(request):
    check = checkSession()

    if check:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = {
                'email' : email,
                'password' : password
            }

            response = loginUser(user,cur)

            if response['statusCode'] == 200:

                return redirect("movies")
            else:
                return render(request,'login.html',{'message' : 'password Error'})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html',{'message' : 'Please register'})

def forgate(request):
    check = checkSession()

    if check == False:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = {
                'email' : email,
                'password' : password
            }

            print('email :',email)
            print('password :',password)

            response = forgate_user_password(user,cur)

            if response['statusCode'] == 200:


                sql = "UPDATE register SET password = %s WHERE email=%s"
                values = (password,email)

                cur.execute(sql,values)

                return redirect('login')
                # return render(request,'forgate.html',{'message': 'password changed'})
            else:
                return render(request,'forgate.html',{'message' : 'Please register first'})
            
        else:
            return render(request,'forgate.html')   
    else:
        return render(request,'login.html')
     


def movies(request):
    if request.method == 'POST':
        try:
            search = request.POST['search']
            response =  requests.get(f"http://www.omdbapi.com/?apikey=e498f053&s={search}")
            response_json = response.json()
            response_json = response_json['Search']

        except Exception as e:
            return render(request,'movieShow.html',{'message':'Search Not found'})
        
        return render(request,'movieShow.html',{'responce': response_json})
    else:
        try:
            response =  requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=e498f053")
            response_json = response.json()
            # response_json = response_json['Search']
            print(response_json)
        except Exception as e:
            print("Error:",e)
        return render(request,'movieShow.html',{'response_get':response_json})