########################################################################
# R.A.Borrelli
# @TheDoctorRAB 
# rev.25.September.2015
# v1.0
########################################################################
#
# v1.0: Basic calculations to compute weight fractions for MCNPX materials card 
#
########################################################################
#
# imports
#
import numpy
#
########################################################################
#
# constants
#
uranium238_mass=238.05078826
uranium235_mass=235.0439299
oxygen_mass=15.99491461956
thorium_mass=232.0380553
#
uranium_density=19.05  #g/cc
thorium_density=11.72  #g/cc
oxygen_density=0.00143 #g/cc
#
#######
#
# enrichment
#
uranium235_enrichment=0.05
uranium238_enrichment=1-uranium235_enrichment
#
#######
#
# weight
#
uranium_dioxide_mw=uranium235_enrichment*uranium235_mass+uranium238_enrichment*uranium238_mass+2*oxygen_mass
#
#######
#
# weight fractions
#
uranium235_fraction=(uranium235_enrichment*uranium235_mass)/uranium_dioxide_mw
uranium238_fraction=(uranium238_enrichment*uranium238_mass)/uranium_dioxide_mw
oxygen_fraction=(2*oxygen_mass)/uranium_dioxide_mw
#
#######
print uranium235_fraction,uranium238_fraction,oxygen_fraction
