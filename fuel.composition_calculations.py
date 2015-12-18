########################################################################
# R.A.Borrelli
# @TheDoctorRAB 
# rev.16.December.2015
# v1.1
########################################################################
#
# v1.0: Basic calculations to compute weight fractions for MCNPX materials card 
# v1.1: Added thorium/uranium mixture density calculation
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
thorium232_mass=232.0380553
#
uranium_density=19.05  #g/cc
thorium_density=11.72  #g/cc
oxygen_density=0.00143 #g/cc
#
uranium_dioxide_density=10.97 #g/cc
thorium_dioxide_density=10.00 #g/cc
#
########################################################################
#
# fuel composition 
#
###
#
# enrichment
#
uranium235_enrichment=0.05
thorium232_enrichment=0.99
uranium238_enrichment=1-uranium235_enrichment-thorium232_enrichment
#
###
#
# weight
#
fuel_dioxide_mw=uranium235_enrichment*uranium235_mass+uranium238_enrichment*uranium238_mass+thorium232_enrichment*thorium232_mass+2*oxygen_mass
#
###
#
# weight fractions
#
uranium235_fraction=(uranium235_enrichment*uranium235_mass)/fuel_dioxide_mw
thorium232_fraction=(thorium232_enrichment*thorium232_mass)/fuel_dioxide_mw
uranium238_fraction=(uranium238_enrichment*uranium238_mass)/fuel_dioxide_mw
oxygen_fraction=(2*oxygen_mass)/fuel_dioxide_mw
#
###
#
# density
# Kutty et al., doi: 10.1007/978-1-4471-5589-8_2
# figure 4
#
fuel_density=((uranium235_enrichment+uranium238_enrichment)/(uranium_dioxide_density)+(thorium232_enrichment)/(thorium_dioxide_density))**(-1)
#
###
#
# output
#
fuel_oxide_output=open('fuel.oxide_th.99.out','w+')
fuel_oxide_output.write('uranium-thorium oxide mixture'+'\n\n'+'U235 enrichment'+'\t\t'+str.format('%.4f'%uranium235_enrichment)+'\n'+'Th232 enrichment'+'\t'+str.format('%.4f'%thorium232_enrichment)+'\n'+'U238 content'+'\t\t'+str.format('%.4f'%uranium238_enrichment)+'\n\n'+'U235 weight fraction'+'\t'+str.format('%.6f'%uranium235_fraction)+'\n'+'Th232 weight fraction'+'\t'+str.format('%.6f'%thorium232_fraction)+'\n'+'U238 weight fraction'+'\t'+str.format('%.6f')%uranium238_fraction+'\n'+'O weight fraction'+'\t'+str.format('%.6f'%oxygen_fraction)+'\n\n'+'fuel mixture density'+'\t'+str.format('%.2f'%fuel_density))
fuel_oxide_output.close()
#
########################################################################
#
# EOF
#
########################################################################
