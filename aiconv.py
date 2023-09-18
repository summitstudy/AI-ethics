from flask import Flask, render_template, request, redirect,url_for
import sys
application = Flask(__name__)
import tensorflow as tf 
import pandas as pd
import numpy as np

def softmax(a):
    c = np.max(a)   
    exp_a = np.exp(a - c)       # 오버플로우를 막기 위해서
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def aiconv_set(quiz,sex,age,person): #매개변수: 문제,성별,나이,성격
    alltable = pd.read_csv('./database.csv')
    # 원핫인코딩
    print(alltable.dtypes)
    intable = pd.get_dummies(alltable,columns=[quiz])
    print(intable)
    # 독립변수(indepen), 종속변수(depen)
    
    indepen = intable[['sex', 'age', 'person']]
    depen = intable[[quiz+'_1', quiz+'_2', quiz+'_3']]
    X = tf.keras.layers.Input(shape=[3])
    Y = tf.keras.layers.Dense(3, activation='softmax')(X)
    model = tf.keras.models.Model(X, Y)
    model.compile(loss='categorical_crossentropy',metrics='accuracy')
    
    # 3.가져온 독립 종속 데이터로 모델 학습
    model.fit(indepen, depen, epochs=3)
    
    # 학습된 AI모델 완성 이 AI모델을 바탕으로 새 데이터 한 줄을 받음
    dap_df = pd.DataFrame({0:[sex],1:[age],2:[person]}) #예측 데이터 프레임
    dap_df = dap_df.astype('float32') #추가
    pre_tmp = model.predict(dap_df)
    
    print(pre_tmp)
    pre_tmp = softmax(pre_tmp)
    print(pre_tmp)
    
    pre_table = pd.DataFrame(pre_tmp)
    D1 = pre_table.loc[0,0]
    D2 = pre_table.loc[0,1]
    D3 = pre_table.loc[0,2]
    
    if (max(D1,D2,D3) == D1):
        return 1
    elif(max(D1,D2,D3) == D2):
        return 2
    elif(max(D1,D2,D3) == D3):
        return 3
    return None