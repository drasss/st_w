import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math


st.latex(r""" W((t)xe^{ax}) """)

f=st.text_input("fonction a plot en fonction de x et a ( lisible en python ) ","a*x")

a=st.number_input("a", 0.01, 100.,value=1.)

intervallex=st.slider("intervalle du plot de x", 0.0, 100.0, (0., 50.))

t=st.slider("t", 0.,a,value=1.)

pas=st.slider("pas en 10^-1", 1,4)

ecart=np.arange(intervallex[0],intervallex[1],10**(-pas))

fig1 = plt.figure()



def func(x,a,f):
    return eval(f)


W=np.array([sp.special.lambertw((t)*i*np.exp(a*i))for i in ecart])
plt.plot(ecart,W)


if f!="":
    valf=np.array([func(i,a,f) for i in ecart])
    plt.plot(ecart,valf)
st.latex(r""" W((t)xe^{ax})""")
st.text("en fonction de x")
st.pyplot(fig1)

x=st.slider("x", 0.,100.,value=1.)

intervallet=st.slider("intervalle du plot de t", 0.0, 20., (1., 10.))

ecart=np.arange(intervallet[0],intervallet[1],10**(-pas))

fig2=plt.figure()
W=np.array([sp.special.lambertw((i)*x*np.exp(a*x))for i in ecart])
plt.plot(ecart,W)

if f!="":
    valf=np.array([func(i,a,f) for i in ecart])
    plt.plot(ecart,valf)
st.latex(r""" W((t)xe^{ax}) """)
st.text("en fonction de t")
st.pyplot(fig2)
