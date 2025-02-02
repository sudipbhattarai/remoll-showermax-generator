from cmath import pi
import math

output_file = "showerMaxDetectorSystem" # "showerMaxDetector for single det and showerMaxDetectorSystem for whole system"

### Define geometry parameters(dimensions based on ISU elog 576):
radial_extent = 1020.0          #distance from beam center to tungsten-quartz bottom on US ring
nQuartz = 4
nSMmodules = 1 if output_file == "showerMaxDetector" else 28
in2mm = 25.4

## Quartz
length_quartz = 160.0
width_quartz = 265.0
thick_quartz = 6.0
quartz_rotate = ["pi/2", "-pi/2", "pi/2", "-pi/2"]

## Tungsten 
length_tungsten = length_quartz
width_tungsten = width_quartz
thick_tungsten = 8.0

## Spacer in TQ stack
thick_spacer = 0.870
length_spacer = length_quartz
width_spacer = width_quartz
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

## mirror parameter
thick_wall_mirror = 0.5

## Front and back plate of quartz-tungsten stack
length_front_back_plate = 181.698
width_front_back_plate = 313.800
thick_front_back_plate = 6.35 
length_front_plate_hole = 3.20*in2mm
width_front_plate_hole = 8.40*in2mm

## Webbed side support structure
length_web_plate = 432.190
width_web_plate = 15.875
thick_web_plate = 63.500
radius_web_plate_hole_small = 31.75/2
radius_web_plate_hole_big = 25.53
thick_web_plate_leg = 6.350
length_web_plate_leg = 190.19
length_web_plate_egdeToHole = 38.175
length_web_plate_smallHoles_distance = 50.800
length_web_plate_holes_small_big = 53.975

## U-bracket (Referenced with lower bracket)
length_uBracket = 15.88
width_uBracket = 23.88
thick_uBracket = 50.80
width_uBracket_legSpace = 17.53
thick_uBracket_legSpace = 38.10

## Ledge
length_ledge = (length_front_back_plate-length_quartz)
width_ledge = 6.35
thick_ledge = thick_web_plate

## Outer radial top support
length_top_support = 6.350
width_top_support = 370.878
thick_top_support = 114.3
radius_top_support_hole = 42
width_top_support_corner_cut = 48.0       # edge cut is the rectangular cut in all 4 corners
thick_top_support_corner_cut = 20.0

## PMT region
radius_pmt = 1.5*in2mm # Radius of 1.5 inches (for 3 inches PMT)
length_pmt_base = 50
length_pmt_gut = 150
length_pmt_window = 3.0
length_pmt_filter = 5.0 #Combination of long pass filter and ND filter
length_pmt_region = length_pmt_filter + length_pmt_window + length_pmt_gut + length_pmt_base
length_pmt_housing = length_pmt_region + 2.0 + 3.0 # tolernace + lid
length_pmt_cathode = 3e-6
radius_inner_pmt_housing = radius_top_support_hole
radius_outer_pmt_housing =  radius_inner_pmt_housing + 3.0
radius_pmt_housing_lid = 48.0
length_pmt_housing_lid = 3.0
width_si_chip = 50
length_si_chip = 0.5

## Struts (the rods that attach SM modules to the ring support structure)
length_strut = 381.0
width_strut = 63.5
thick_strut = 36.83

## SM support ring
radius_inner_support_ring = 68*in2mm
radius_outer_support_ring = 78*in2mm
thick_support_ring= 1.75*in2mm  # It is 2 inches in the CAD 

detector_tilt = 0

zstagger = 41   # distance between center of a SM module and the center of two SM rings(Value adjusted to fit support Larry's support structure)
#print(23920-2*(thick_quartz+thick_tungsten)+zstagger)
#print(23920-2*(thick_quartz+thick_tungsten)-zstagger)

thick_mother=2*thick_mirror_box_bot+2*zstagger+5

pos=radial_extent+length_quartz/2

f=open(output_file+".gdml", "w+")

## GDML schema
out="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n"

out+="<!DOCTYPE gdml [\n"
out+="\t<!ENTITY matrices SYSTEM \"showerMaxMatrices.xml\">\n"
out+="\t<!ENTITY materials SYSTEM \"showerMaxMaterials.xml\">\n"
out+="]>\n\n"

out+="<gdml\n"
out+="\txmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
out+="\txsi:noNamespaceSchemaLocation=\"http://service-spi.web.cern.ch/service-spi/app/releases/GDML/schema/gdml.xsd\">\n\n"

out+="<define>\n"
out+="\t&matrices;\n"
out+="</define>\n\n"

## Define materials
out+="&materials;\n\n"

## Define solids
out+="<solids>\n"

out+="\t<xtru name=\"solid_quartz\" lunit=\"mm\">\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2+thick_quartz)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<section zOrder=\"1\" zPosition=\""+str(-width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t\t<section zOrder=\"2\" zPosition=\""+str(width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t</xtru>\n"

out+="\t<box name=\"solid_tungsten\" lunit=\"mm\" x=\""+str(length_tungsten)+"\" y=\""+str(width_tungsten)+"\" z=\""+str(thick_tungsten)+"\"/>\n"

out+="\t<box name=\"solid_spacer\" lunit=\"mm\" x=\""+str(length_spacer)+"\" y=\""+str(width_spacer)+"\" z=\""+str(thick_spacer-0.02)+"\"/>\n"  # Made 0.02 less thick than actual gap

# Suitcase box, where the TQ stack rests
out+="\t<box name=\"solid_suitcase_tungstenquartz_1\" lunit=\"mm\" x=\""+str(length_stack_tungstenquartz+thick_wall_mirror)+"\" y=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\" z=\""+str(thick_stack_tungstenquartz+2*thick_wall_mirror)+"\"/>\n"
out+="\t<box name=\"solid_suitcase_tungstenquartz_2\" lunit=\"mm\" x=\""+str(length_stack_tungstenquartz+1.0)+"\" y=\""+str(width_stack_tungstenquartz)+"\" z=\""+str(thick_stack_tungstenquartz)+"\"/>\n"

out+="\t<subtraction name=\"solid_suitcase_tungstenquartz\">"
out+="\n\t\t<first ref=\"solid_suitcase_tungstenquartz_1\"/>"
out+="\n\t\t<second ref=\"solid_suitcase_tungstenquartz_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_suitcase_tungstenquartz_12\" x=\""+str(0.5)+"\" y=\"0\" z=\"0\"/>"
out+="\n\t\t<rotation name=\"rot_subtract_suitcase_tungstenquartz_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# Front-back aluminum plate
out+="\t<box name=\"solid_front_back_plate\" lunit=\"mm\" x=\""+str(length_front_back_plate)+"\" y=\""+str(width_front_back_plate)+"\" z=\""+str(thick_front_back_plate)+"\"/>\n"
out+="\t<box name=\"solid_front_plate_hole\" lunit=\"mm\" x=\""+str(length_front_plate_hole)+"\" y=\""+str(width_front_plate_hole)+"\" z=\""+str(thick_front_back_plate+1.0)+"\"/>\n"

out+="\t<subtraction name=\"solid_front_plate\">"
out+="\n\t\t<first ref=\"solid_front_back_plate\"/>"
out+="\n\t\t<second ref=\"solid_front_plate_hole\"/>"
out+="\n\t\t<position name=\"pos_subtract_front_plate\" x=\"0\" y=\""+str(0)+"\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_front_plate\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# U-bracket(Reference volume is bottom left)
out+="\t<box name=\"solid_uBracket_1\" lunit=\"mm\" x=\""+str(length_uBracket)+"\" y=\""+str(width_uBracket)+"\" z=\""+str(thick_uBracket)+"\"/>\n"
out+="\t<box name=\"solid_uBracket_legSpace\" lunit=\"mm\" x=\""+str(length_uBracket+1.0)+"\" y=\""+str(width_uBracket_legSpace+0.2)+"\" z=\""+str(thick_uBracket_legSpace)+"\"/>\n"

out+="\t<subtraction name=\"solid_uBracket_2\">"
out+="\n\t\t<first ref=\"solid_uBracket_1\"/>"
out+="\n\t\t<second ref=\"solid_uBracket_legSpace\"/>"
out+="\n\t\t<position name=\"pos_subtract_uBracket\" x=\"0\" y=\""+str(-(width_uBracket-width_uBracket_legSpace)/2)+"\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_uBracket\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#------------------

# Ledge
out+="\t<box name=\"solid_ledge\" lunit=\"mm\" x=\""+str(length_ledge)+"\" y=\""+str(width_ledge)+"\" z=\""+str(thick_ledge)+"\"/>\n"
#out+="\t<box name=\"solid_ledge_2\" lunit=\"mm\" x=\""+str(10)+"\" y=\""+str(15)+"\" z=\""+str(thick_ledge-2*thick_web_plate_leg)+"\"/>\n"

#out+="\t<union name=\"solid_ledge\">"
#out+="\n\t\t<first ref=\"solid_ledge_1\"/>"
#out+="\n\t\t<second ref=\"solid_ledge_2\"/>"
#out+="\n\t\t\t<position name=\"pos_union_ledge\" x=\""+str(length_ledge/2-5)+"\" y=\""+str(-width_ledge/2-7.5)+"\" z=\""+str(0)+"\"/>"
#out+="\n\t\t\t<rotation name=\"rot_union_ledge\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
#out+="\n\t</union>\n"
#------------------

# Mirror box bottom(lower part of the light guide)
out+="\t<trd name=\"solid_mirror_box_bot_1\" lunit=\"mm\" x1=\""+str(thick_stack_tungstenquartz-thick_tungsten+2*thick_wall_mirror)+"\"  x2=\""+str(thick_mirror_box_bot+2*thick_wall_mirror)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\"  y2=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_bot)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_bot_2\" lunit=\"mm\" x1=\""+str(thick_stack_tungstenquartz-thick_tungsten)+"\"  x2=\""+str(thick_mirror_box_bot)+"\" y1=\""+str(width_stack_tungstenquartz)+"\"  y2=\""+str(width_stack_tungstenquartz)+"\" z=\""+str(length_mirror_box_bot+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_bot\">"
out+="\n\t\t<first ref=\"solid_mirror_box_bot_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_bot_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# Mirror box top(upper part of the light guide)
out+="\t<trd name=\"solid_mirror_box_top_1\" lunit=\"mm\" x1=\""+str(thick_mirror_box_bot+2*thick_wall_mirror)+"\"  x2=\""+str(thick_mirror_box_top+2*thick_wall_mirror)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror)+"\"  y2=\""+str(thick_mirror_box_top+2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_top)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_top_2\" lunit=\"mm\" x1=\""+str(thick_mirror_box_bot)+"\"  x2=\""+str(thick_mirror_box_top)+"\" y1=\""+str(width_stack_tungstenquartz)+"\"  y2=\""+str(thick_mirror_box_top)+"\" z=\""+str(length_mirror_box_top+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_top\">"
out+="\n\t\t<first ref=\"solid_mirror_box_top_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_top_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# Web Plate (side support)
out+="\t<box name=\"solid_web_plate_1\" lunit=\"mm\" x=\""+str(length_web_plate)+"\" y=\""+str(width_web_plate)+"\" z=\""+str(thick_web_plate)+"\"/>\n"
out+="\t<cone name=\"solid_web_plate_hole_small\" rmin1=\""+str(0)+"\"  rmax1=\""+str(radius_web_plate_hole_small)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(radius_web_plate_hole_small)+"\"  z=\""+str(width_web_plate+1.0)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"
out+="\t<cone name=\"solid_web_plate_hole_big\" rmin1=\""+str(0)+"\"  rmax1=\""+str(radius_web_plate_hole_big)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(radius_web_plate_hole_big)+"\"  z=\""+str(width_web_plate+1.0)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"
out+="\t<box name=\"solid_web_plate_leg_gap\" lunit=\"mm\" x=\""+str(length_web_plate_leg+0.2)+"\" y=\""+str(width_web_plate+1.0)+"\" z=\""+str(2*radius_web_plate_hole_big)+"\"/>\n"

for i in range(0,4):
        out+="\t<subtraction name=\"solid_web_plate_"+str(i+2)+"\">"
        out+="\n\t\t<first ref=\"solid_web_plate_"+str(i+1)+"\"/>"
        out+="\n\t\t<second ref=\"solid_web_plate_hole_small\"/>"
        out+="\n\t\t<position name=\"pos_subtract_web_plate_hole_small\" x=\""+str(length_web_plate/2-length_web_plate_egdeToHole-i*length_web_plate_smallHoles_distance)+"\" y=\"0\" z=\"0\"/>" 
        out+="\n\t\t<rotation name=\"rot_subtract_web_plate_hole_small\" x=\"pi/2\" y=\"0\" z=\"0\"/>"
        out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_web_plate_6\">"
out+="\n\t\t<first ref=\"solid_web_plate_5\"/>"
out+="\n\t\t<second ref=\"solid_web_plate_hole_big\"/>"
out+="\n\t\t<position name=\"pos_subtract_web_plate_hole_big\" x=\""+str(length_web_plate/2-length_web_plate_egdeToHole-3*length_web_plate_smallHoles_distance-length_web_plate_holes_small_big)+"\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_web_plate_hole_big\" x=\"pi/2\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_web_plate_7\">"
out+="\n\t\t<first ref=\"solid_web_plate_6\"/>"
out+="\n\t\t<second ref=\"solid_web_plate_leg_gap\"/>"
out+="\n\t\t<position name=\"pos_subtract_web_plate_leg\" x=\""+str(-(length_web_plate-length_web_plate_leg)/2)+"\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_web_plate_leg\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# Outer radial top support
out+="\t<box name=\"solid_top_support_1\" lunit=\"mm\" x=\""+str(length_top_support)+"\" y=\""+str(width_top_support)+"\" z=\""+str(thick_top_support)+"\"/>\n"
out+="\t<cone name=\"solid_top_support_hole\" rmin1=\""+str(0)+"\"  rmax1=\""+str(radius_top_support_hole)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(radius_top_support_hole)+"\"  z=\""+str(length_top_support+1.0)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"
out+="\t<box name=\"solid_top_support_corner_cut\" lunit=\"mm\" x=\""+str(length_top_support+1.0)+"\" y=\""+str(width_top_support_corner_cut)+"\" z=\""+str(thick_top_support_corner_cut)+"\"/>\n"

out+="\t<subtraction name=\"solid_top_support_2\">"
out+="\n\t\t<first ref=\"solid_top_support_1\"/>"
out+="\n\t\t<second ref=\"solid_top_support_hole\"/>"
out+="\n\t\t<position name=\"pos_subtract_top_support\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_top_support\" x=\"0\" y=\"pi/2\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_top_support_3\">"
out+="\n\t\t<first ref=\"solid_top_support_2\"/>"
out+="\n\t\t<second ref=\"solid_top_support_corner_cut\"/>"
out+="\n\t\t<position name=\"pos_subtract_top_support\" x=\"0\" y=\""+str((width_top_support-width_top_support_corner_cut+0.4)/2)+"\" z=\""+str((thick_top_support-thick_top_support_corner_cut+0.4)/2)+"\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_top_support\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_top_support_4\">"
out+="\n\t\t<first ref=\"solid_top_support_3\"/>"
out+="\n\t\t<second ref=\"solid_top_support_corner_cut\"/>"
out+="\n\t\t<position name=\"pos_subtract_top_support\" x=\"0\" y=\""+str(-(width_top_support-width_top_support_corner_cut+0.4)/2)+"\" z=\""+str((thick_top_support-thick_top_support_corner_cut+0.4)/2)+"\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_top_support\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_top_support_5\">"
out+="\n\t\t<first ref=\"solid_top_support_4\"/>"
out+="\n\t\t<second ref=\"solid_top_support_corner_cut\"/>"
out+="\n\t\t<position name=\"pos_subtract_top_support\" x=\"0\" y=\""+str(-(width_top_support-width_top_support_corner_cut+0.4)/2)+"\" z=\""+str(-(thick_top_support-thick_top_support_corner_cut+0.4)/2)+"\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_top_support\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"

out+="\t<subtraction name=\"solid_top_support_6\">"
out+="\n\t\t<first ref=\"solid_top_support_5\"/>"
out+="\n\t\t<second ref=\"solid_top_support_corner_cut\"/>"
out+="\n\t\t<position name=\"pos_subtract_top_support\" x=\"0\" y=\""+str((width_top_support-width_top_support_corner_cut+0.4)/2)+"\" z=\""+str(-(thick_top_support-thick_top_support_corner_cut+0.4)/2)+"\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_top_support\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

out+="\t<tube name=\"solid_pmt_filter\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_filter)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_window\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_window)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_cathode\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_cathode)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_gut)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_base\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_base)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<box name=\"solid_si_chip\" lunit=\"mm\" x=\""+str(length_si_chip)+"\" y=\""+str(width_si_chip)+"\" z=\""+str(width_si_chip)+"\"/>\n"

out+="\t<cone name=\"solid_pmt_housing\" rmin1=\""+str(radius_inner_pmt_housing)+"\"  rmax1=\""+str(radius_outer_pmt_housing)+"\" rmin2=\""+str(radius_inner_pmt_housing)+"\" rmax2=\""+str(radius_outer_pmt_housing)+"\"  z=\""+str(length_pmt_housing)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"

out+="\t<cone name=\"solid_pmt_housing_lid\" rmin1=\""+str(0)+"\"  rmax1=\""+str(radius_pmt_housing_lid)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(radius_pmt_housing_lid)+"\"  z=\""+str(length_pmt_housing_lid)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"

out+="\t<box name=\"solid_strut\" lunit=\"mm\" x=\""+str(length_strut)+"\" y=\""+str(width_strut)+"\" z=\""+str(thick_strut)+"\"/>\n"

# Mother volume single detector
out+="\t<box name=\"solid_stack_region\" lunit=\"mm\" x=\""+str(length_front_back_plate)+"\" y=\""+str(width_front_back_plate+1.0)+"\" z=\""+str(thick_stack_tungstenquartz+2*thick_wall_mirror+2*thick_front_back_plate+1.0)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_bot_region\" lunit=\"mm\" x1=\""+str(thick_stack_tungstenquartz-thick_tungsten+2*thick_wall_mirror+1.0)+"\"  x2=\""+str(thick_mirror_box_bot+2*thick_wall_mirror+1.0)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror+1.0)+"\"  y2=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror+1.0)+"\" z=\""+str(length_mirror_box_bot+1.0)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_top_region\" lunit=\"mm\" x1=\""+str(thick_mirror_box_bot+2*thick_wall_mirror+1.0)+"\"  x2=\""+str(thick_mirror_box_top+2*thick_wall_mirror+1.0)+"\" y1=\""+str(width_stack_tungstenquartz+2*thick_wall_mirror+1.0)+"\"  y2=\""+str(thick_mirror_box_top+2*thick_wall_mirror+1.0)+"\" z=\""+str(length_mirror_box_top+1.0)+"\"/>\n"

out+="\t<union name=\"solid_singledet_1\">"
out+="\n\t\t<first ref=\"solid_stack_region\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_bot_region\"/>"
out+="\n\t\t\t<position name=\"pos_mirror_box_bot\" x=\""+str((length_front_back_plate+length_mirror_box_bot)/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_mirror_box_bot\" x=\""+str(0)+"\" y=\"pi/2\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<union name=\"solid_singledet_2\">"
out+="\n\t\t<first ref=\"solid_singledet_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_top_region\"/>"
out+="\n\t\t\t<position name=\"pos_mirror_box_top\" x=\""+str(length_front_back_plate/2+length_mirror_box_bot+length_mirror_box_top/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_mirror_box_top\" x=\""+str(0)+"\" y=\"pi/2\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<union name=\"solid_singledet_3\">"
out+="\n\t\t<first ref=\"solid_singledet_2\"/>"
out+="\n\t\t<second ref=\"solid_top_support_6\"/>"
out+="\n\t\t\t<position name=\"pos_top_support\" x=\""+str(length_front_back_plate/2+length_mirror_box_bot+length_mirror_box_top+length_top_support/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_top_support\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<cone name=\"solid_pmt_region\" rmin1=\""+str(0)+"\"  rmax1=\""+str(radius_outer_pmt_housing+5.0)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(radius_outer_pmt_housing+5.0)+"\"  z=\""+str(length_pmt_housing+5.0)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n"

out+="\t<union name=\"solid_singledet_4\">"
out+="\n\t\t<first ref=\"solid_singledet_3\"/>"
out+="\n\t\t<second ref=\"solid_pmt_region\"/>"
out+="\n\t\t\t<position name=\"pos_pmt_region\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_housing/2 + 2.5)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_pmt_region\" x=\""+str(0)+"\" y=\"pi/2\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<box name=\"solid_webplate_region\" lunit=\"mm\" x=\""+str(length_web_plate)+"\" y=\""+str(width_front_back_plate)+"\" z=\""+str(thick_web_plate)+"\"/>\n"

out+="\t<union name=\"solid_singledet_5\">"
out+="\n\t\t<first ref=\"solid_singledet_4\"/>"
out+="\n\t\t<second ref=\"solid_webplate_region\"/>"
out+="\n\t\t\t<position name=\"pos_webplate_region\" x=\""+str((length_web_plate)/2)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_webplate_region\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
out+="\n\t</union>\n"

out+="\t<box name=\"solid_strut_region\" lunit=\"mm\" x=\""+str(length_strut)+"\" y=\""+str(width_top_support)+"\" z=\""+str(thick_strut)+"\"/>\n"

out+="\t<union name=\"solid_singledet_6\">"
out+="\n\t\t<first ref=\"solid_singledet_5\"/>"
out+="\n\t\t<second ref=\"solid_strut_region\"/>"
out+="\n\t\t\t<position name=\"pos_strut_region\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_strut/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
out+="\n\t\t\t<rotation name=\"rot_strut_region\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
out+="\n\t</union>\n"
#----------------

out+="\t<cone name=\"solid_support_ring\" rmin1=\""+str(radius_inner_support_ring)+"\"  rmax1=\""+str(radius_outer_support_ring)+"\" rmin2=\""+str(radius_inner_support_ring)+"\" rmax2=\""+str(radius_outer_support_ring)+"\"  z=\""+str(thick_support_ring)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n" #Make sure this mother volume doesn't interfere with coils

if nSMmodules==28:
        out+="\t<cone name=\"solid_showerMaxMother\" rmin1=\""+str(730)+"\"  rmax1=\""+str(2100)+"\" rmin2=\""+str(730)+"\" rmax2=\""+str(2100)+"\"  z=\""+str(thick_mother)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n\n" #Make sure this mother volume doesn't interfere with coils
else:
        out+="\t<cone name=\"solid_showerMaxMother\" rmin1=\""+str(0)+"\"  rmax1=\""+str(1000)+"\" rmin2=\""+str(0)+"\" rmax2=\""+str(1000)+"\"  z=\""+str(thick_mother)+"\" startphi=\"0\" deltaphi=\"360\" aunit=\"deg\" lunit=\"mm\"/>\n\n"

## Optical Surfaces
out+="\t<opticalsurface name=\"quartz_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_dielectric\" value=\"0.98\" >\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"Quartz_REFLECTIVITY\" />\n"
out+="\t</opticalsurface>\n"
out+="\t<opticalsurface name=\"Al_mirror_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_metal\" value=\"0.98\" >\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"MiroSilver_REFLECTIVITY_30DEG\" />\n"
out+="\t</opticalsurface>\n"
out+="\t<opticalsurface name=\"Cathode_surface\" model=\"glisur\" finish=\"polished\" type=\"dielectric_metal\" value=\"1.0\">\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"CathodeSurf_REFLECTIVITY\" />\n"
out+="\t\t<property name=\"EFFICIENCY\" ref=\"Cathode_EFFICIENCY\" />\n"
out+="\t</opticalsurface>\n"

out+="</solids>\n"

## Define logical volumes using above solids
out+="\n\n<structure>\n"

out+="\t<volume name=\"logic_support_ring\">"
out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
out+="\n\t\t<solidref ref=\"solid_support_ring\"/>"
out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
out+="\n\t</volume>\n"

for i in range(0,nSMmodules):
        for j in range(0,nQuartz):
                out+="\t<volume name=\"logic_quartz_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Quartz\"/>"
                out+="\n\t\t<solidref ref=\"solid_quartz\"/>"
                out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
                out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxQuartz\" />"
                out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+str(2*(4-j))+"\"/>"
                out+="\n\t</volume>\n"
      
                out+="\t<volume name=\"logic_tungsten_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Tungsten_material\"/>"
                out+="\n\t\t<solidref ref=\"solid_tungsten\"/>"
                if (j == 3):
                        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxTungsten\" />"
                        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+str(2*(4-j)-1)+"\"/>"
                out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"red\"/>"
                out+="\n\t</volume>\n"
                
        for j in range(2*nQuartz):        
                out+="\t<volume name=\"logic_spacer_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Nylon\"/>"
                out+="\n\t\t<solidref ref=\"solid_spacer\"/>"
                out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"black\"/>"
                out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxSpacer\" />"
                out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+str(20+j)+"\"/>"
                out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_suitcase_tungstenquartz_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_suitcase_tungstenquartz\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_front_back_plate_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_front_back_plate\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"orange\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_front_plate_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_front_plate\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"orange\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_web_plate_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_web_plate_7\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_uBracket_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_uBracket_2\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_ledge_left_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Nylon\"/>"
        out+="\n\t\t<solidref ref=\"solid_ledge\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"ledgeLeft\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"28"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"brown\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_ledge_right_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Nylon\"/>"
        out+="\n\t\t<solidref ref=\"solid_ledge\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"ledgeRight\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"29"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"brown\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_bot\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_top\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_filter_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_filter\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTFilter\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"10"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"magenta\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_window_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_window\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTwindow\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"11"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Cathode\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_cathode\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTcathode\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetType\" auxvalue=\"opticalphoton\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"16"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Galactic\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMT\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"12"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"yellow\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_si_chip_1_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Si\"/>"
        out+="\n\t\t<solidref ref=\"solid_si_chip\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"pmtBaseSiChip\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"14"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"black\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_si_chip_2_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Si\"/>"
        out+="\n\t\t<solidref ref=\"solid_si_chip\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"pmtBaseSiChip\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"15"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"black\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_base_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"G4_Galactic\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_base\"/>"
        out+="\n\t\t<physvol name=\"pmt_si_chip_1_"+str(i)+"\">"        # Add Silicon chips inside the base
        out+="\n\t\t\t<volumeref ref=\"logic_si_chip_1_"+str(i)+"\"/>"     
        out+="\n\t\t\t<position name=\"pos_logic_si_chip_1_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(-length_pmt_base/6)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_si_chip_1_"+str(i)+"\" x=\""+str(0)+"\" y=\"pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"
        out+="\n\t\t<physvol name=\"pmt_si_chip_2_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_si_chip_2_"+str(i)+"\"/>"     
        out+="\n\t\t\t<position name=\"pos_logic_si_chip_2_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(length_pmt_base/6)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_si_chip_2_"+str(i)+"\" x=\""+str(0)+"\" y=\"pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"showerMaxPMTbase\" />"
        out+="\n\t\t<auxiliary auxtype=\"DetNo\" auxvalue=\""+"7"+str(i).zfill(2)+"13"+"\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"red\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.5\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_top_support_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_top_support_6\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_housing_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_housing\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.5\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_housing_lid_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_housing_lid\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_strut_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_strut\"/>"
        out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"grey\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_singledet_"+str(i).zfill(2)+"\">"
        out+="\n\t\t<materialref ref=\"Air\"/>"
        out+="\n\t\t<solidref ref=\"solid_singledet_6\"/>"

        # After defining logical volumes for each SM modules, now define physical volumes
        out+="\n\t\t<physvol name=\"suitcase_tungstenquartz_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_suitcase_tungstenquartz_"+str(i)+"\"/>"     
        out+="\n\t\t\t<position name=\"pos_logic_suitcase_tungstenquartz_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_suitcase_tungstenquartz_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_bot_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(length_front_back_plate/2+length_mirror_box_bot/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_top_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_top_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_top_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"top_support_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_top_support_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_top_support_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_top_support_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        #out+="\n\t\t<physvol name=\"pmt_filter_"+str(i)+"\">"
        #out+="\n\t\t\t<volumeref ref=\"logic_pmt_filter_"+str(i)+"\"/>"
        #out+="\n\t\t\t<position name=\"pos_logic_pmt_filter_"+str(i)+"\" x= \""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support/2)+"\" y=\"0\" z=\""+str(thick_tungsten/2)+"\"/>"
        #out+="\n\t\t\t<rotation name=\"rot_logic_pmt_filter_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        #out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_window_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_window_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_window/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_cathode_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_window+length_pmt_cathode/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_window+length_pmt_cathode+length_pmt_gut/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_base_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_base_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_base_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_window+length_pmt_cathode+length_pmt_gut+length_pmt_base/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_base_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_housing_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_housing_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_housing_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_housing/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_housing_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_housing_lid_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_housing_lid_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_housing_lid_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_housing+length_pmt_housing_lid/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_housing_lid_"+str(i)+"\" x=\""+str(0)+"\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"strut_right_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_strut_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_strut_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_strut/2)+"\" y=\""+str((width_top_support-width_strut)/2)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_strut_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"strut_left_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_strut_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_strut_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_strut/2)+"\" y=\""+str(-(width_top_support-width_strut)/2)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_strut_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"front_plate_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_front_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_front_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(-(thick_stack_tungstenquartz+2*thick_wall_mirror+thick_front_back_plate)/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_front_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"back_plate_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_front_back_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_back_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str((thick_stack_tungstenquartz+2*thick_wall_mirror+thick_front_back_plate)/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_back_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"web_plate_right_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_web_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_web_plate_"+str(i)+"\" x=\""+str((length_web_plate-length_front_back_plate)/2)+"\" y=\""+str((width_front_back_plate-width_web_plate)/2)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_web_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"web_plate_left_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_web_plate_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_web_plate_"+str(i)+"\" x=\""+str((length_web_plate-length_front_back_plate)/2)+"\" y=\""+str(-(width_front_back_plate-width_web_plate)/2)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_web_plate_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"ledge_right_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_ledge_right_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_ledge_right_"+str(i)+"\" x=\""+str((length_quartz)/2)+"\" y=\""+str((width_quartz+width_ledge)/2+thick_wall_mirror+0.2)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_ledge_right_"+str(i)+"\" x=\""+str(pi)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"ledge_left_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_ledge_left_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_ledge_left_"+str(i)+"\" x=\""+str((length_quartz)/2)+"\" y=\""+str(-(width_quartz+width_ledge)/2-thick_wall_mirror-0.2)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_ledge_left_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"uBracket_bottom_left_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_uBracket_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_uBracket_bottom_left_"+str(i)+"\" x=\""+str(-(length_quartz-length_uBracket)/2)+"\" y=\""+str(-(width_front_back_plate-width_uBracket)/2-thick_wall_mirror)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_uBracket_bottom_left_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"uBracket_bottom_right_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_uBracket_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_uBracket_bottom_right_"+str(i)+"\" x=\""+str(-(length_quartz-length_uBracket)/2)+"\" y=\""+str((width_front_back_plate-width_uBracket)/2+thick_wall_mirror)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_uBracket_bottom_right_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"pi\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"uBracket_top_left_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_uBracket_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_uBracket_top_left_"+str(i)+"\" x=\""+str((length_quartz-width_uBracket)/2)+"\" y=\""+str(-(width_front_back_plate-length_uBracket)/2-thick_wall_mirror)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_uBracket_top_left_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"pi/2\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"uBracket_top_right_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_uBracket_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_uBracket_top_right_"+str(i)+"\" x=\""+str((length_quartz-width_uBracket)/2)+"\" y=\""+str((width_front_back_plate-length_uBracket)/2+thick_wall_mirror)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_uBracket_top_right_"+str(i)+"\" x=\""+str(0)+"\" y=\"0\" z=\"pi/2\"/>"
        out+="\n\t\t</physvol>"

        for j in range(0,nQuartz):
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

        #for j in range(0,2*nQuartz):
                #out+="\n\t\t<physvol name=\"spacer_"+str(i)+"_"+str(j)+"\">"
                #out+="\n\t\t\t<volumeref ref=\"logic_spacer_"+str(i)+"_"+str(j)+"\"/>"             
                #out+="\n\t\t\t<position name=\"pos_logic_spacer_"+str(i)+"_"+str(j)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(2.0*thick_quartz+2.0*thick_tungsten+4*thick_spacer+0.074-((j+1)//2)*thick_quartz-(j//2)*thick_tungsten-j*thick_spacer)+"\"/>"
                #out+="\n\t\t\t<rotation name=\"rot_logic_spacer_"+str(i)+"_"+str(j)+"\" x=\"0\" y=\"0\" z=\"0\"/>"        
                #out+="\n\t\t</physvol>"

        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
        out+="\n\t</volume>\n"
            
out+="\t<volume name=\"showerMaxMother\">"
out+="\n\t\t<materialref ref=\"Air\"/>"
out+="\n\t\t<solidref ref=\"solid_showerMaxMother\"/>"

# Place all 28 modules in the showerMaxMother volume
for i in range(0,nSMmodules):
        if (nSMmodules==28):
                if (i%2==0):    
                        zpos=-zstagger
                        rpos=pos
                if (i%2==1):
                        zpos=zstagger
                        rpos=pos + 4
                theta=math.pi+2*i*math.pi/28
                xpos=rpos*(math.cos(theta))
                ypos=rpos*(math.sin(theta)) 
        else:
                theta=0
                xpos=0
                ypos=0
                zpos=0

        out+="\n\t\t<physvol name=\"singledet_"+str(i).zfill(2)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_singledet_"+str(i).zfill(2)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_singledet_"+str(i)+"\" x=\""+str(xpos)+"\" y=\""+str(ypos)+"\" z=\""+str(zpos)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_singledet_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(-theta)+"\"/>"
        out+="\n\t\t</physvol>"

if nSMmodules == 28:
        out+="\n\t\t<physvol name=\"support_ring\">"
        out+="\n\t\t\t<volumeref ref=\"logic_support_ring\"/>"
        out+="\n\t\t\t<position name=\"pos_support_ring)\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_support_ring\" x=\""+str(0)+"\" y=\"0\" z=\""+str(0)+"\"/>"
        out+="\n\t\t</physvol>"

out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
out+="\n\t</volume>\n\n"

# Specify surfaces for optical properties
out+="\t<skinsurface name=\"quartz_skin_surface\" surfaceproperty=\"quartz_surface\" >\n"
for i in range(0,nSMmodules):
    out+="\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>\n"
    out+="\t\t<volumeref ref=\"logic_pmt_filter_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"

out+="\t<skinsurface name=\"suitcase_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
for i in range(0,nSMmodules):
    out+="\t\t<volumeref ref=\"logic_suitcase_tungstenquartz_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"

out+="\t<skinsurface name=\"mirror_box_top_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
for i in range(0,nSMmodules):
    out+="\t\t<volumeref ref=\"logic_mirror_box_top_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"

out+="\t<skinsurface name=\"mirror_box_bottom_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
for i in range(0,nSMmodules):
    out+="\t\t<volumeref ref=\"logic_mirror_box_bot_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"

out+="\t<skinsurface name=\"cathode_surface\" surfaceproperty=\"Cathode_surface\" >\n"
for i in range(0,nSMmodules):
    out+="\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"

out+="\n</structure>\n"

out+="<setup name=\"showerMaxWorld\" version=\"1.0\">"
out+="\n\t<world ref=\"showerMaxMother\"/>"
out+="\n</setup>\n"

out+="</gdml>\n"

f.write(out)

print("Succesfully written to GDML file.")