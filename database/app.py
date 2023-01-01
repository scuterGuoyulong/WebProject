# -*- coding:gbk -*-
import datetime

from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


# 调用数据库sqlite：
def use_db(sql_order):
    conn = sqlite3.connect('lecture.db')
    datalist = []
    cur = conn.cursor()
    cur.execute(sql_order)
    results = cur.fetchall()
    for row in results:
        datalist.append(row)
    conn.commit()
    conn.close()
    return datalist


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/')
def website1():  # put application's code here
    sql = '''select *
         from inf


        '''
    datalist = use_db(sql)
    import json

    return render_template("index.html", reports=datalist)


# 按照报告举行时间report由近及远排序(time)
@app.route('/report')
def website2():  # put application's code here
    sql = '''select *
         from inf
         order by time desc'''
    datalist = use_db(sql)
    return render_template("report1.html", reports=datalist)


# 按照报告举行时间report升序(time)
@app.route('/reportAsc')
def website21():  # put application's code here
    sql = '''select *
         from inf
         order by time asc'''
    datalist = use_db(sql)
    return render_template("reportAsc.html", reports=datalist)


# 按照报告发布时间release由降序(rel_time)
@app.route('/order&release')
def website3():  # put application's code here
    sql = '''select *
         from inf
         order by rel_time desc'''
    datalist = use_db(sql)
    return render_template("anounce.html", reports=datalist)


# 按照报告发布时间release升序(rel_time)
@app.route('/releaseAsc')
def website31():  # put application's code here
    sql = '''select *
         from inf
         order by rel_time asc'''
    datalist = use_db(sql)
    return render_template("anounceAsc.html", reports=datalist)


# 最近两年的公告year(time)
@app.route('/order&year')
def website4():  # put application's code here
    sql = '''select *
         from inf
         where time like '%2021%'
         or time like '%2022%'
         order by time desc
         '''
    datalist = use_db(sql)
    return render_template("year.html", reports=datalist)


# 最近一个年的公告year(time)
@app.route('/order-year')
def website41():  # put application's code here
    sql = '''select *
         from inf
         where time like '%2022%'
         order by time desc
         '''
    datalist = use_db(sql)
    return render_template("year2.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/qh')
def website1_1():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "清华大学"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school1.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/xin')
def website1_2():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "信息安全国家重点实验室"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school2.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/sc')
def website1_3():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "四川大学"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school3.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/bj')
def website1_4():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "北京航空航天大学"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school4.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/sd')
def website1_5():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "山东大学"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school5.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/zj')
def website1_6():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "浙江大学"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school6.html", reports=datalist)


# 路由解析，通过用户访问的路径，匹配相应函数
@app.route('/recent')
def website_recent():  # put application's code here
    time = datetime.date.today()
    sql = '''select *
         from inf
        where inf.time between date('now','start of day','-30 days') and date('now')
        or inf.time like '%2022-06%'
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("recent.html",  reports=datalist)


if __name__ == '__main__':
    app.run(debug=True)
