from flask import Flask, render_template, request, redirect,url_for
import sys
application = Flask(__name__)
import database
import tensorflow as tf 
import pandas as pd
import numpy as np
import aiconv

@application.route("/") #메인 페이지
def hello():
    return render_template("hello.html")

@application.route("/apply") #입력 페이지
def apply():
    return render_template("apply.html")

@application.route("/question") #문제 풀이 페이지
def photo_apply():
    sex = request.args.get("sex")
    age = request.args.get("age")
    person = request.args.get("person")
    return render_template("question.html",sex=sex,age=age,person=person)

@application.route("/conclude") #설명하는 페이지, <<<< 데이터 처리 >>>>
def conclude():
    sex = request.args.get("sex")
    age = request.args.get("age")
    person = request.args.get("person")
    
    quiz1 = request.args.get("quiz1") #나의 1번 풀이
    quiz2 = request.args.get("quiz2") #나의 2번 풀이
    quiz3 = request.args.get("quiz3") #나의 3번 풀이
    
    num1 = 'quiz1'
    num2 = 'quiz2'
    num3 = 'quiz3'
    pre1 = aiconv.aiconv_set(num1,sex,age,person) #인공지능이 예측한 나의 1번 풀이
    pre2 = aiconv.aiconv_set(num2,sex,age,person) #인공지능이 예측한 나의 2번 풀이
    pre3 = aiconv.aiconv_set(num3,sex,age,person) #인공지능이 예측한 나의 3번 풀이
    
    database.save(sex, age, person,quiz1,quiz2,quiz3) # 데이터베이스 저장
    
    return render_template("conclude.html",sex=sex,age=age,person=person,quiz1=quiz1,quiz2=quiz2,quiz3=quiz3,pre1=pre1,pre2=pre2,pre3=pre3)

@application.route("/conclude2") #최종 결론 페이지, 가져온 결론들을 변수로 모두 가져온다.
def conclude2():
    sex = request.args.get("sex")
    age = request.args.get("age")
    person = request.args.get("person")
    
    quiz1 = request.args.get("quiz1")
    quiz2 = request.args.get("quiz2")
    quiz3 = request.args.get("quiz3")
    
    pre1 = request.args.get("pre1")
    pre2 = request.args.get("pre2")
    pre3 = request.args.get("pre3")
    
    return render_template("conclude2.html",sex=sex,age=age,person=person,quiz1=quiz1,quiz2=quiz2,quiz3=quiz3,pre1=pre1,pre2=pre2,pre3=pre3)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
