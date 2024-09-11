from pytc2.sistemas_lineales import analyze_sys,pretty_print_lti, tf2sos_analog,pretty_print_SOS
from pytc2.general import Chebyshev_polynomials,s,w,print_subtitle
import sympy as sp 
from scipy import signal as sig
from pytc2.sistemas_lineales import bodePlot, pzmap, GroupDelay, analyze_sys

import matplotlib as mpl
from matplotlib import pyplot as plt

import numpy as np
import math

Q=5
norma=2*math.pi*50

num_notch= [1.0 , 0, (norma)**2]
den_notch=[1.0, norma/Q , (norma)**2]

filter_names = []
all_sys=[]

n=2

this_aprox= 'Notch'
this_label=this_aprox + '_ord_' + str(n) + '_rip_' +'at=1rad/seg'


filter_names.append(this_label)
all_sys.append(sig.TransferFunction(num_notch,den_notch))

analyze_sys(all_sys,filter_names)

print_subtitle(this_label)
