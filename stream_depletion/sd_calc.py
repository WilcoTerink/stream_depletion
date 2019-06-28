# -*- coding: utf-8 -*-
#
# stream_depletion: Calculates stream depletion effect of a pumping well using the Jenkins (1968) / Theis (1941) solutions
#
# Copyright (C) 2019  Wilco Terink & Matt Smith
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#-Authorship information-########################################################################################################################
__author__ = 'Wilco Terink & Matt Smith'
__copyright__ = 'Wilco Terink & Matt Smith'
__version__ = '1.0.0'
__date__ ='June 2019'
#################################################################################################################################################

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc
from math import sqrt

#-Calculate the Stream Depletion Factor
def sdf(L,S,T):
    '''
    Calculates Stream Depletion Factor given:
        L - Shortest distance from well to stream (m)
        S - Storage coefficient (-)
        T - Transmissivity (m2/d)
    Returns:
        y - stream depletion factor
    '''
    y = (L**2)*S/T
    print('Stream Depletion Factor (SDF) for L:%.2f, S:%.2f, and T:%.2f = %.2f' %(L,S,T, y))
    
    return y

#-SD for on/off pumping at various rates
def SD(L, S, T, Qpump):
    '''
    Calculates stream depletion effect given:
        L - Shortest distance from well to stream (m)
        S - Storage coefficient (-)
        T - Transmissivity (m2/d)
        Qpump - NumPy 1D array with dynamic pumping rates (L/d)
    Returns:
        sd_matrix - NumPy 1D array with stream depletion rate (L/d) based on dynamic pumping rate Qpump - unit is same as provided in the pumping rate: e.g. if pumping rate is in liters per second, then so is the stream depletion rate
        sd_avg - Numpy 1D array with stream depletion rate (L/d) based on continous pumping at the average of pumping rate Qpump
        Qavg - average of pumping Qpump (L/d)
    '''
    #Qpump = np.nan_to_num(Qpump)  #-make sure NaNs are replaced by zeros
    Qpump[np.isnan(Qpump)] = 0.
    #-Calculate Stream depletion factor
    SDF = sdf(L,S,T)
    t = np.arange(1,len(Qpump)+1,1)
    ###-Calculate sd for average pumping rate throughout the entire period t
    Qavg = np.nanmean(Qpump)
    y = np.sqrt(SDF/(4*t))
    y = erfc(y)
    sd_avg = y*Qavg
    ###-Calculate SD pumping going on and off and variable pumping rates
    dQ = np.zeros(len(t))
    sd_matrix = np.zeros([len(t), len(t)])
    for i in t:
        ix = np.argwhere(t==i)[0][0]
        if ix==0:
            dQ[ix] = Qpump[ix]
        else:
            dQ[ix] = Qpump[ix] - Qpump[ix-1]
             
        for j in t:
            if j>=i:
                jx = np.argwhere(t==j)[0][0]
                y = erfc(sqrt(SDF/(4*(j-i+1))))
                y = y * dQ[ix]
                sd_matrix[ix,jx] = y
    #-super position the individual curves
    sd_matrix = np.sum(sd_matrix, axis=0)
    
    return sd_matrix, sd_avg, Qavg

def plotSD(fname, Qpump, Qpump_sd, QpumpAvg=None, QpumpAvg_sd=None, xlabel_txt='', ylabel_txt='', title_txt=''):
    '''
    Plots the dynamic pumping and the associated stream depletion effect in one graph. If provided, then it also plots the average pumping rate with the associated
    stream depletion effect. Input:
        fname - absolute path to file name of figure to save
        Qpump - NumPy 1D array with dynamic pumping rates (L/d)
        Qpump_sd - NumPy 1D array with stream depletion rate (L/d) based on dynamic pumping rate Qpump
        QpumpAvg - Average pumping rate of Qpump (L/d) (Optional)
        QpumpAvg_sd - Numpy 1D array with stream depletion rate (L/d) based on continous pumping at the average of pumping rate Qpump (Optional)
        xlabel_txt - string to be plotted as x-axis label
        ylabel_txt - string to be plotted as y-axis label
        title_txt - string to be plotted as title
    '''
    fig,ax = plt.subplots(facecolor='#FFFFFF')
    t = np.arange(1,len(Qpump)+1,1)
    ax.plot(t, Qpump, label='Pumping rate')
    ax.plot(t, Qpump_sd, label='SD based on dynamic pumping rate')
    if QpumpAvg is not None and QpumpAvg_sd is not None:
        ax.plot(t,QpumpAvg_sd, label='SD based on average pumping rate')
        ax.hlines(QpumpAvg, t[0], t[-1], label='Average pumping rate')
    ax.set_xlabel(xlabel_txt)
    ax.set_ylabel(ylabel_txt)
    ax.grid(True)
    ax.set_ylim([0, np.nanmax(Qpump)+5])
    handles,labels = ax.get_legend_handles_labels()
    if QpumpAvg is not None and QpumpAvg_sd is not None:
        handles = [handles[0], handles[1], handles[3], handles[2]]
        labels = [labels[0], labels[1], labels[3], labels[2]]
    else:
        handles = [handles[0], handles[1]]
        labels = [labels[0], labels[1]]
    ax.legend(handles,labels,loc='upper right')
    plt.title(title_txt)
    fig.tight_layout()
    plt.savefig(fname, dpi=300)
    print('Plot is saved to %s' %fname)
