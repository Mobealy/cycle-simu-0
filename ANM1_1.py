import numpy as np   # -*- coding: utf-8 -*-"""Created on Sun Jul  3 14:35:51 2022 @author: byw"""
import pandas as pd  # command: streamlit run C:\temp\LSTNet\Master20220611\ANM1_1.py
import time
import psutil
import matplotlib.pyplot as plt
import streamlit as st
#import SessionState

def main1(j):
    i = 0
    last_rows = rawdat[0, selected_gauge].reshape(1, -1)
    last_rows1 = rawdat[0, j].reshape(1, -1)
    while True:
        new_rows = rawdat[i+1, selected_gauge].reshape(1, -1) # new_rows = last_rows[-1, :] + np.array(psutil.cpu_percent()).reshape(1, -1)
        chart.add_rows(new_rows)
        last_rows = new_rows
        new_rows1 = rawdat[i+1, j].reshape(1, -1)
        chart1.add_rows(new_rows1)
        last_rows1 = new_rows1
        time.sleep(0.1)
        i += 1


DATPATH = "C:/temp/LSTNet/Master20220611/data/201910Win2_TCW2A1B1C1D1_E8_NO_TS.txt" # 201909Win2_TCW2A1B1C1D1_E8_NO_TS.txt
i = 0
j = 3
X, y = [], []

st.sidebar.title("Controls")
start = st.sidebar.button("Start")
stop = st.sidebar.button("Stop")
selected_gauge = st.sidebar.selectbox('Gauge', list(range(4)), on_change=main1, args=(j, ))

rawdat = pd.read_csv(DATPATH, sep=",", header=None);
rawdat =rawdat.apply(pd.to_numeric, errors = 'coerce').interpolate().to_numpy();
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
X.append(i)
y.append(rawdat[0, selected_gauge]) # y.append(psutil.cpu_percent())
last_rows = rawdat[0, selected_gauge].reshape(1, -1) # np.array(y).reshape(1, -1)
chart = st.line_chart(last_rows)
chart1 = st.line_chart(rawdat[0, j].reshape(1, -1))

main1(j)        
