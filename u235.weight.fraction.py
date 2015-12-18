########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.17.December.2015
########################################################################
# 
# Uranium 235 as a function of thorium content 
#
########################################################################
#
#
#
########################################################################
#
# imports
#
import numpy
import scipy.stats
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
from win32api import GetSystemMetrics
#
########################################################################
#
#
#
#######
#
# diagnostics
#
matplotlib.rcParams.update({'font.size': 18}) #set global plot font
width=GetSystemMetrics (0)
height=GetSystemMetrics (1)
#
#######
#
# input data
#
plotdata=numpy.loadtxt('u235.weight.fraction.inp')
#
#######
#
# plot
#
fig,left_axis=plot.subplots()
title='U235 weight fraction in (ThU)O2 mixed oxide fuel'
xtitle='Thorium content'
ytitle='U235 weight fraction'
line_color='black'
#
plot.title(title)
left_axis.set_xlabel(xtitle)
left_axis.set_ylabel(ytitle)
#
xmin=0
xmax=0.95
ymin=0.043
ymax=0.045
#
xmajortick=0.05
xminortick=0.025
ymajortick=0.0010
yminortick=0.0005
#
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
#
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
#
left_axis.grid(which='major',axis='both',linewidth='1.1')
#
left_axis.plot(plotdata[:,0],plotdata[:,1],color=line_color)
#
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
plot.show()
#
########################################################################
#
# EOF
#
########################################################################
