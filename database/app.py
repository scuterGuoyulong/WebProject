# -*- coding:gbk -*-
import datetime

from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


# �������ݿ�sqlite��
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


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/')
def website1():  # put application's code here
    sql = '''select *
         from inf


        '''
    datalist = use_db(sql)
    import json

    return render_template("index.html", reports=datalist)


# ���ձ������ʱ��report�ɽ���Զ����(time)
@app.route('/report')
def website2():  # put application's code here
    sql = '''select *
         from inf
         order by time desc'''
    datalist = use_db(sql)
    return render_template("report1.html", reports=datalist)


# ���ձ������ʱ��report����(time)
@app.route('/reportAsc')
def website21():  # put application's code here
    sql = '''select *
         from inf
         order by time asc'''
    datalist = use_db(sql)
    return render_template("reportAsc.html", reports=datalist)


# ���ձ��淢��ʱ��release�ɽ���(rel_time)
@app.route('/order&release')
def website3():  # put application's code here
    sql = '''select *
         from inf
         order by rel_time desc'''
    datalist = use_db(sql)
    return render_template("anounce.html", reports=datalist)


# ���ձ��淢��ʱ��release����(rel_time)
@app.route('/releaseAsc')
def website31():  # put application's code here
    sql = '''select *
         from inf
         order by rel_time asc'''
    datalist = use_db(sql)
    return render_template("anounceAsc.html", reports=datalist)


# �������Ĺ���year(time)
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


# ���һ����Ĺ���year(time)
@app.route('/order-year')
def website41():  # put application's code here
    sql = '''select *
         from inf
         where time like '%2022%'
         order by time desc
         '''
    datalist = use_db(sql)
    return render_template("year2.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/qh')
def website1_1():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "�廪��ѧ"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school1.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/xin')
def website1_2():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "��Ϣ��ȫ�����ص�ʵ����"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school2.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/sc')
def website1_3():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "�Ĵ���ѧ"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school3.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/bj')
def website1_4():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "�������պ����ѧ"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school4.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/sd')
def website1_5():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "ɽ����ѧ"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school5.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
@app.route('/zj')
def website1_6():  # put application's code here
    sql = '''select *
         from inf
        where inf.university == "�㽭��ѧ"
        order by time desc
        '''
    datalist = use_db(sql)
    return render_template("school6.html", reports=datalist)


# ·�ɽ�����ͨ���û����ʵ�·����ƥ����Ӧ����
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
