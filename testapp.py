import streamlit as st
import numpy as np
import pandas as pd
import time

st.header('Hello! ')
def balloons():
  if st.button('Balloons?'):
    st.balloons()
    st.image('images/alfa.jpeg')
    st.markdown("**Alfa**")

def df_sample():
  df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50]
  })
  df
  option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

  'You selected: ', option

def line_chart():
  chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

  st.sidebar.line_chart(chart_data)

def line_plot():
  map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

  st.map(map_data)

def sidebar_vis():
  left_column, right_column = st.beta_columns(2)
  pressed = left_column.button('Press me?')
  if pressed:
    right_column.write("Woohoo!")

  expander = st.beta_expander("FAQ")
  expander.write("Here you could put in some really, really long explanations...")

def progress():
  latest_iteration = st.empty()
  bar = st.progress(0)
  for i in range(10):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

  '...and now we\'re done!'

df_sample()
progress()
line_chart()
line_plot()
sidebar_vis()
balloons()
