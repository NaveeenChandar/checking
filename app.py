import streamlit as st
import pandas as pd
import numpy as np

st.title('This is heading')
st.subheader('the sub heading')
st.write('sasdfasdf')
#st.write(pd.DataFrame ({'first':[1,2,3,4], 'second':[1,5,6,7]}))

df = pd.DataFrame ({'first':[1,2,3,4], 'second':[1,5,6,7]})

df

option = st.selectbox('a',('asd','wfqa', 'fadv'))

#st.write('f', option)

st.text_input("Variable 1")
st.button('add')