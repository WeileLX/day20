import dbutils.pooled_db
import pymysql
from flask import Blueprint, render_template, request,redirect, session

from utils import db


#蓝图对象
ac = Blueprint('account', __name__)



@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

#wtforms 干嘛的

    role = request.form.get('role')
    mobile = request.form.get('mobile')
    password = request.form.get('pwd')
    print(role,mobile,password)

#connect to MYSQL to check if the user is in the database
    result = db.fetch_one("select * from user_database where role=%s and mobile=%s and password=%s", (role, mobile, password))

    if result:
        session["user_id"] = {"role":role,"real_name":result['real_name'],"id":result['id']}
        return redirect("/order/list") #跳转其他网址
    else:
        return render_template("login.html",error="登陆失败，请重试")





    return "good"



@ac.route('/users')
def users():
    return "用户列表"