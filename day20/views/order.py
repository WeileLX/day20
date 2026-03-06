from flask import Blueprint, session

od = Blueprint('od', __name__)

@od.route('/order/list')
def order_list():
    #读取cookie&解密获取用户信息

    user_info = session.get("user_id")
    print(user_info,type(user_info))
    return "订单列表"

@od.route('/order/create')
def order_create():
    return "创建订单"