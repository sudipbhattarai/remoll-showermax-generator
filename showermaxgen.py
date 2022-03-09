import csv
import sys
import os
import math

output_file = "showerMaxGen"

### Define geometry parameters(dimensions based on ISU elog 576):
radial_extent = 1020.0          #distance from beam center to tungsten-quartz bottom

## Quartz
length_quartz = 160.0
width_quartz = 265.0
thick_quartz = 6.0
quartz_rotate = ["pi/2", "-pi/2", "pi/2", "-pi/2"]

## Tungsten 
length_tungsten = length_quartz
width_tungsten = width_quartz
thick_tungsten = 8.0

# Spacer in TQ stack
thick_spacer = 0.870
thick_tolerance = 0.508

## Tungsten-quartz stack
length_stack_tungstenquartz = length_quartz
width_stack_tungstenquartz = width_quartz
thick_stack_tungstenquartz = 4*(thick_quartz+thick_tungsten)+ 8*thick_spacer + 2*thick_tolerance

## Mirror box bottom (lower part of the light guide)
length_mirror_box_bot = 67.462  
thick_mirror_box_bot = 85.868

## Mirror box top (upper part of the light guide)
length_mirror_box_top = 183.058
thick_mirror_box_top = 69.866

## PMT region
pmt_radius = 38.1 # Radius of 1.5 inches (for 3 inches PMT)
pmt_base_extent = 50
pmt_extent = 150
#pmt_cathode_extent = 3e-6
pmt_window_extent = 3.0
pmt_lpfilter_extent = 2.5       #long pass filter
pmt_atten_extent = 2.5          #attenuator
pmt_filter_extent = pmt_lpfilter_extent + pmt_atten_extent

## mirror parameter
thick_wall_mirror = 0.5

## Front and back plate of quartz-tungsten stack
length_front_back_plate = 181.698
width_front_back_plate = 313.800
thick_front_back_plate = 6.35 

# Webbed side support structure
length_web_plate = 432.190
width_web_plate = 15.875
thick_web_plate = 63.500

## Mirror box and PMT combined logical volume
length_logic_mirror_box = length_mirror_box_bot+length_mirror_box_top+pmt_filter_extent+pmt_window_extent+pmt_extent+pmt_base_extent

detector_tilt = 0

zstagger = 41   # distance between center of a SM module and the center of two SM rings(Value adjusted to fit support Larry's support structure)
print(23920-2*(thick_quartz+thick_tungsten)+zstagger)
print(23920-2*(thick_quartz+thick_tungsten)-zstagger)

thick_mother=2*thick_mirror_box_bot+2*zstagger+5

pos=radial_extent+length_quartz/2

f=open(output_file+".gdml", "w+")

## GDML schema
out="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
out+="<gdml"
out+="\n\txmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\""
out+="\n\txsi:noNamespaceSchemaLocation=\"http://service-spi.web.cern.ch/service-spi/app/releases/GDML/schema/gdml.xsd\">\n"

out+="\n\n<define>"
out+="\n</define>"

## Define materials
out+="\n\n<materials>\n"
out+="\t<material name=\"G4_Quartz\" state=\"solid\">\n"
out+="\t\t<MEE unit=\"eV\" value=\"139.2\"/>\n"
out+="\t\t<D value=\"2.2\" unit=\"g/cm3\"/>\n"
out+="\t\t<fraction n=\"0.467465468463971\" ref=\"G4_Si\"/>\n"
out+="\t\t<fraction n=\"0.532534531536029\" ref=\"G4_O\"/>\n"
out+="\t</material>\n"

out+="\t<material name=\"G4_Cathode\" state=\"solid\">\n"
#out+="\t\t<MEE unit=\"eV\" value=\"380.1876\"/>\n"
out+="\t\t<D value=\"0.8223\" unit=\"g/cm3\"/>\n"
out+="\t\t<fraction n=\"0.2349\" ref=\"G4_K\"/>\n"
out+="\t\t<fraction n=\"0.3993\" ref=\"G4_Cs\"/>\n"
out+="\t\t<fraction n=\"0.3658\" ref=\"G4_Sb\"/>\n"
out+="\t</material>\n"

out+="</materials>\n"

## Define solids
out+="\n\n<solids>\n"

out+="\t<tube name=\"solid_pmt_filter\" rmin=\"0\" rmax=\""+str(pmt_radius)+"\" z=\""+str(pmt_filter_extent)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_window\" rmin=\"0\" rmax=\""+str(pmt_radius)+"\" z=\""+str(pmt_window_extent)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

#out+="\t<tube name=\"solid_pmt_cathode\" rmin=\"0\" rmax=\""+str(pmt_radius)+"\" z=\""+str(pmt_cathode_extent)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt\" rmin=\"0\" rmax=\""+str(pmt_radius)+"\" z=\""+str(pmt_extent)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_base\" rmin=\"0\" rmax=\""+str(pmt_radius)+"\" z=\""+str(pmt_base_extent)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<box name=\"solid_mirror_box_tungstenquartz_1\" lunit=\"mm\" x=\""+str(length_stack_tungstenquartz)+"\" y=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\" z=\""+str(thick_stack_tungstenquartz+2*thick_wall_mirror)+"\"/>\n"

out+="\t<box name=\"solid_mirror_box_tungstenquartz_2\" lunit=\"mm\" x=\""+str(length_stack_tungstenquartz+1)+"\" y=\""+str(width_stack_tungstenquartz)+"\" z=\""+str(thick_stack_tungstenquartz)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_tungstenquartz\">"
out+="\n\t\t<first ref=\"solid_mirror_box_tungstenquartz_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_tungstenquartz_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_tungstenquartz_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_tungstenquartz_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<trd name=\"solid_mirror_box_bot_1\" lunit=\"mm\" x1=\""+str(thick_stack_tungstenquartz-thick_tungsten+2*thick_wall_mirror)+"\"  x2=\""+str(thick_mirror_box_bot+2*thick_wall_mirror)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\"  y2=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_bot)+"\"/>\n"

out+="\t<trd name=\"solid_mirror_box_bot_2\" lunit=\"mm\" x1=\""+str(thick_stack_tungstenquartz-thick_tungsten)+"\"  x2=\""+str(thick_mirror_box_bot)+"\" y1=\""+str(width_stack_tungstenquartz)+"\"  y2=\""+str(width_stack_tungstenquartz)+"\" z=\""+str(length_mirror_box_bot+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_bot\">"
out+="\n\t\t<first ref=\"solid_mirror_box_bot_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_bot_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<trd name=\"solid_mirror_box_top_1\" lunit=\"mm\" x1=\""+str(thick_mirror_box_bot+2*thick_wall_mirror)+"\"  x2=\""+str(thick_mirror_box_top+2*thick_wall_mirror)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\"  y2=\""+str(thick_mirror_box_top+2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_top)+"\"/>\n"

out+="\t<trd name=\"solid_mirror_box_top_2\" lunit=\"mm\" x1=\""+str(thick_mirror_box_bot)+"\"  x2=\""+str(thick_mirror_box_top)+"\" y1=\""+str(width_stack_tungstenquartz)+"\"  y2=\""+str(thick_mirror_box_top)+"\" z=\""+str(length_mirror_box_top+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_top\">"
out+="\n\t\t<first ref=\"solid_mirror_box_top_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_top_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<xtru name=\"solid_quartz\" lunit=\"mm\">\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2+thick_quartz)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<section zOrder=\"1\" zPosition=\""+str(-width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t\t<section zOrder=\"2\" zPosition=\""+str(width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t</xtru>\n"

out+="\t<box name=\"solid_tungsten\" lunit=\"mm\" x=\""+str(length_tungsten)+"\" y=\""+str(width_tungsten)+"\" z=\""+str(thick_tungsten)+"\"/>\n"

#-----------------------#
out+="\t<box name=\"solid_logic_mirror_box_3\" lunit=\"mm\" x=\""+str(length_front_back_plate)+"\" y=\""+str(width_front_back_plate)+"\" z=\""+str(thick_stack_tungstenquartz+2*thick_wall_mirror+2*thick_front_back_plate)+"\"/>\n"

out+="\t<union name=\"solid_logic_mirror_box_tungstenquartz_frontplate_backplate\">"
out+="\n\t\t<first ref=\"solid_mirror_box_tungstenquartz_1\"/>"
out+="\n\t\t<second ref=\"solid_logic_mirror_box_3\"/>"
out+="\n\t\t<position name=\"pos_logic_mirror_box_tungstenquartz_frontplate_backplate\" z=\""+str(0)+"\" y=\""+str(0)+"\" x=\""+str(-(length_front_back_plate-length_quartz)/2.0)+"\"/>"
out+="\n\t\t<rotation name=\"rot_logic_mirror_box_tungstenquartz_frontplate_backplate\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</union>\n"
#-----------------------#

out+="\t<box name=\"solid_logic_mirror_box_4\" lunit=\"mm\" z=\""+str(length_logic_mirror_box-length_mirror_box_bot)+"\" y=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\" x=\""+str(thick_mirror_box_bot+2*thick_wall_mirror)+"\"/>\n"
out+="\t<union name=\"solid_logic_mirror_box\">"
out+="\n\t\t<first ref=\"solid_mirror_box_bot_1\"/>"
out+="\n\t\t<second ref=\"solid_logic_mirror_box_4\"/>"
out+="\n\t\t<position name=\"pos_logic_mirror_box\" z=\""+str(length_logic_mirror_box/2.0)+"\" y=\""+str(0)+"\" x=\"0\"/>"
out+="\n\t\t<rotation name=\"rot_logic_mirror_box\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<box name=\"solid_front_back_plate\" lunit=\"mm\" x=\""+str(length_front_back_plate)+"\" y=\""+str(width_front_back_plate)+"\" z=\""+str(thick_front_back_plate)+"\"/>\n"

out+="\t<union name=\"solid_logic_mirror_box_union\">"
out+="\n\t\t<first ref=\"solid_logic_mirror_box_tungstenquartz_frontplate_backplate\"/>"
out+="\n\t\t<second ref=\"solid_logic_mirror_box\"/>"
out+="\n\t\t<position name=\"pos_logic_mirror_box_union\" x=\""+str(length_quartz/2.0+length_mirror_box_bot/2.0)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2.0)+"\"/>"
out+="\n\t\t<rotation name=\"rot_logic_mirror_box_union\" x=\"0\" y=\"pi/2\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<box name=\"solid_web_plate\" lunit=\"mm\" x=\""+str(length_web_plate)+"\" y=\""+str(width_web_plate)+"\" z=\""+str(thick_web_plate)+"\"/>\n"

out+="\t<cone name=\"solid_showerMaxMother\" rmin1=\""+str(730)+"\"  rmax1=\""+str(1900)+"\" rmin2=\""+str(730)+"\" rmax2=\""+str(1900)+"\"  z=\""+str(thick_mother)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n" #Make sure this mother volume doesn't interfere with coils

out+="</solids>\n"

## Define logical volumes using above solids
out+="\n\n<structure>\n"

for i in range(0,28):
        out+="\t<volume name=\"logic_mirror_box_tungstenquartz_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Al\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_tungstenquartz\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Al\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_bot\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Al\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_top\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_filter_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_filter\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTFilter\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"10"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"magenta\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_window_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_window\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTwindow\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"11"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
        out+="\n\t</volume>\n"

        #out+="\t<volume name=\"logic_pmt_cathode_"+str(i)+"\">"
        #out+="\n\t\t<materialref ref=\"G4_Cathode\"/>"
        #out+="\n\t\t<solidref ref=\"solid_pmt_cathode\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"purple\"/>"
        #out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Galactic\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMT\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"12"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"yellow\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_base_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Galactic\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_base\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTbase\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"13"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"red\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_front_back_plate_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Al\"/>"
        out+="\n\t\t<solidref ref=\"solid_front_back_plate\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"orange\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_web_plate_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Al\"/>"
        out+="\n\t\t<solidref ref=\"solid_web_plate\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        for j in range(0,4):
                out+="\t<volume name=\"logic_quartz_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"G4_Quartz\"/>"
                out+="\n\t\t<solidref ref=\"solid_quartz\"/>"
                out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
                out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxQuartz\" />"
                out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+str(2*(4-j))+"\"/>"
                out+="\n\t</volume>\n"
      
                out+="\t<volume name=\"logic_tungsten_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"G4_W\"/>"
                out+="\n\t\t<solidref ref=\"solid_tungsten\"/>"
                if (j == 3):
                        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxTungsten\" />"
                        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+str(2*(4-j)-1)+"\"/>"
                out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"red\"/>"
                out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_singledet_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_AIR\"/>"
        out+="\n\t\t<solidref ref=\"solid_logic_mirror_box_union\"/>"

        # After defining logical volumes for each SM modules, now define physical volumes
        out+="\n\t\t<physvol name=\"mirror_box_tungstenquartz_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_tungstenquartz_"+str(i)+"\"/>"     
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_tungstenquartz_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_tungstenquartz_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_bot_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_top_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_top_"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_top_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_filter_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_filter_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_filter"+str(i)+"\" x= \""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top+pmt_filter_extent/2)+"\" y=\"0\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_filter"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_window_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_window_"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top+pmt_filter_extent+pmt_window_extent/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        #out+="\n\t\t<physvol name=\"pmt_cathode_"+str(i)+"\">"
        #out+="\n\t\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>"
        #out+="\n\t\t\t<position name=\"pos_logic_pmt_cathode_"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top+pmt_window_extent+pmt_cathode_extent/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        #out+="\n\t\t\t<rotation name=\"rot_logic_pmt_cathode_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        #out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top+pmt_filter_extent+pmt_window_extent+pmt_extent/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_base_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_base_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_base"+str(i)+"\" x=\""+str(length_quartz/2+length_mirror_box_bot+length_mirror_box_top+pmt_filter_extent+pmt_window_extent+pmt_extent+pmt_base_extent/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_base_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"front_plate_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_front_back_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_front_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(-(thick_stack_tungstenquartz+2*thick_wall_mirror+thick_front_back_plate)/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_front_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"back_plate_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_front_back_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_back_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str((thick_stack_tungstenquartz+2*thick_wall_mirror+thick_front_back_plate)/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_back_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"web_plate_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_web_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_web_plate_"+str(i)+"\" x=\""+str((length_web_plate-length_front_back_plate)/2)+"\" y=\""+str((width_front_back_plate-width_web_plate)/2)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_web_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        for j in range(0,4):
                out+="\n\t\t<physvol name=\"quartz_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t\t<volumeref ref=\"logic_quartz_"+str(i)+"_"+str(j)+"\"/>"             
                out+="\n\t\t\t<position name=\"pos_logic_quartz_"+str(i)+"_"+str(j)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(1.5*thick_quartz+2.0*thick_tungsten+4*thick_spacer+thick_tolerance-j*(thick_quartz+thick_tungsten)-(2*j+1)*thick_spacer)+"\"/>"
                out+="\n\t\t\t<rotation name=\"rot_logic_quartz_"+str(i)+"_"+str(j)+"\" x=\""+quartz_rotate[j]+"\" y=\"0\" z=\"0\"/>"        
                out+="\n\t\t</physvol>"

                out+="\n\t\t<physvol name=\"tungsten_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t\t<volumeref ref=\"logic_tungsten_"+str(i)+"_"+str(j)+"\"/>"
                out+="\n\t\t\t<position name=\"pos_logic_tungsten_"+str(i)+"_"+str(j)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(1.5*thick_tungsten+1.0*thick_quartz+4*thick_spacer+thick_tolerance-j*(thick_quartz+thick_tungsten)-2*(j+1)*thick_spacer)+"\"/>"
                out+="\n\t\t\t<rotation name=\"rot_logic_tungsten_"+str(i)+"_"+str(j)+"\" x=\"0\" y=\"0\" z=\"0\"/>"
                out+="\n\t\t</physvol>"

        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
        out+="\n\t</volume>\n"
            
out+="\t<volume name=\"showerMaxMother\">"
out+="\n\t\t<materialref ref=\"G4_AIR\"/>"
out+="\n\t\t<solidref ref=\"solid_showerMaxMother\"/>"

# Place all 28 modules in the showerMaxMother volume
for i in range(0,28):
        if (i%2==0):    
                zpos=-zstagger
                rpos=pos
        if (i%2==1):
                zpos=zstagger
                rpos=pos + 4
        theta=math.pi+2*i*math.pi/28
        xpos=rpos*(math.cos(theta))
        ypos=rpos*(math.sin(theta)) 
        out+="\n\t\t<physvol name=\"singledet_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_singledet_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_singledet_"+str(i)+"\" x=\""+str(xpos)+"\" y=\""+str(ypos)+"\" z=\""+str(zpos)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_singledet_"+str(i)+"\" x=\""+str(math.asin(-math.sin(theta)*math.sin(detector_tilt)))+"\" y=\""+str(math.asin(math.cos(theta)*math.sin(detector_tilt)))+"\" z=\""+str(-theta)+"\"/>"
        out+="\n\t\t</physvol>"

out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
out+="\n\t</volume>"

out+="\n</structure>\n"

out+="<setup name=\"showerMaxWorld\" version=\"1.0\">"
out+="\n\t<world ref=\"showerMaxMother\"/>"
out+="\n</setup>\n"

out+="</gdml>\n"

f.write(out)