import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math


st.latex(r""" W(xe^{ax}) """)

f=st.text_input("fonction a plot en fonction de x et a ( lisible en python ) ","a*x")

a=st.number_input("a", 0., 10.,1.)

intervalle=st.slider("intervalle du plot", 0.0, 100.0, (0., 50.))

pas=st.slider("pas en 10^-1", 1,4)

fig = plt.figure()

ecart=np.arange(intervalle[0],intervalle[1],10**(-pas))

def func(x,a,f):
    return eval(f)


W=np.array([sp.special.lambertw(i*np.exp(a*i))for i in ecart])
plt.plot(ecart,W)


if f!="":
    valf=np.array([func(i,a,f) for i in ecart])
    plt.plot(ecart,valf)

st.pyplot(fig)


