from django.shortcuts import render

def userExist(userDetail,cur):
    sql = "SELECT email FROM register"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)

    for user in data:
        if userDetail['email'] in user:
            return True
    return False

def register(userDetail,cur):

    checkUser = userExist(userDetail,cur)

    if checkUser:
        return {'statusCode' : 503,'message' : 'user alredy exist'}
    else:
        return {'statusCode' : 200,'message' : 'registration success' }
    

def loginUser(userDetail,cur):
    
    check = userExist(userDetail,cur)

    if check:
        sql = "SELECT * FROM register"
        cur.execute(sql)

        userData = cur.fetchall()
        print(userData)
        for user in userData:
            if user['email'] == userDetail['email'] and user['password'] == userDetail['password']:
                return {'statusCode': 200,'message': 'logged in'}
    else:
        return {'statusCode': 503,'message': 'password error'}
    
def forgate_user_password(userDetail,cur):
    check = userExist(userDetail,cur)

    if check:
        return {'statusCode' : 200,'message' : 'you can chage'}
    else:
        return {'statusCode' : 503,'message' : 'Please registration first'}