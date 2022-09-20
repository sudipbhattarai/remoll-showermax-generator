import math

output_file = "showermaxQsim"

### Define geometry parameters(dimensions based on ISU elog 576):
radial_extent = 1020.0          #distance from beam center to tungsten-quartz bottom on US ring
nQuartz = 4
nSMmodules = 1
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
length_pmt_cathode = 3e-6
length_pmt_window = 3.0
length_pmt_filter = 5.0 #Combination of long pass filter and ND filter
length_pmt_region = length_pmt_filter + length_pmt_window + length_pmt_gut + length_pmt_base
length_pmt_housing = length_pmt_region + 2.0 + 3.0 # tolernace + lid
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

thick_mother=2*thick_mirror_box_bot+2*zstagger+5

pos=radial_extent+length_quartz/2

f=open(output_file+".gdml", "w+")

## GDML schema
out="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n"

out+="<!DOCTYPE gdml [\n"
out+="\t<!ENTITY matrices SYSTEM \"matrices.xml\">\n"
out+="]>\n\n"

out+="<gdml"
out+="\n\txmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\""
out+="\n\txsi:noNamespaceSchemaLocation=\"http://service-spi.web.cern.ch/service-spi/app/releases/GDML/schema/gdml.xsd\">\n"

out+="\n<define>"
out+="\n\t&matrices;"
out+="\n</define>"

## Define materials
out+="\n\n<materials>\n"

out+="<define>\n"
out+="\t<quantity type=\"density\" name=\"universe_mean_density\" value=\"1.e-25\" unit=\"g/cm3\" />\n"
out+="</define>\n"
out+="<element Z=\"8\" formula=\"O\" name=\"Oxygen\" >\n"
out+="\t<atom value=\"16\" />\n"
out+="</element>\n"
out+="<element Z=\"7\" formula=\"N\" name=\"Nitrogen\" >\n"
out+="\t<atom value=\"14.01\" />\n"
out+="</element>\n"
out+="<element Z=\"14\" formula=\"Si\" name=\"Silicon\" >\n"
out+="\t<atom value=\"28.085\" />\n"
out+="</element>\n"
out+="<element Z=\"13\" formula=\"Al\" name=\"Aluminum\" >\n"
out+="\t<atom value=\"26.982\" />\n"
out+="</element>\n"
out+="<element Z=\"51\" formula=\"Sb\" name=\"Antimony\" >\n"
out+="\t<atom value=\"121.760\" />\n"
out+="</element>\n"
out+="<element Z=\"55\" formula=\"Cs\" name=\"Caesium\" >\n"
out+="\t<atom value=\"132.90545\" />\n"
out+="</element>\n"
out+="<element Z=\"19\" formula=\"K\" name=\"Potassium\" >\n"
out+="\t<atom value=\"39.0983\" />\n"
out+="</element>\n"
out+="<element Z=\"74\" formula=\"W\" name=\"Tungsten\" >\n"
out+="\t<atom value=\"183.85\" />\n"
out+="</element>\n\n"

out+="<material formula=\"noFormula\" name=\"Air\" >\n"
out+="\t<property name=\"RINDEX\" ref=\"Air_RINDEX\"/>\n"
out+="\t<D value=\"0.00129\" />\n"
out+="\t<fraction n=\"0.3\" ref=\"Oxygen\" />\n"
out+="\t<fraction n=\"0.7\" ref=\"Nitrogen\" />\n"
out+="</material>\n"
out+="<material formula=\"SiO2\" name=\"Quartz\" >\n"
out+="\t<property name=\"RINDEX\" ref=\"Quartz_RINDEX\"/>\n"
out+="\t<property name=\"ABSLENGTH\" ref=\"Quartz_ABSLENGTH\"/>\n"
out+="\t<property name=\"REFLECTIVITY\" ref=\"Quartz_REFLECTIVITY\"/>\n"
out+="\t<D value=\"2.203\" />\n"
out+="\t<composite n=\"1\" ref=\"Silicon\" />\n"
out+="\t<composite n=\"2\" ref=\"Oxygen\" />\n"
out+="</material>\n"
out+="<material formula=\"K2CsSb\" name=\"Cathode\" >\n"
out+="\t<D value=\"3.46\" />\n"
out+="\t<composite n=\"2\" ref=\"Potassium\" />\n"
out+="\t<composite n=\"1\" ref=\"Caesium\" />\n"
out+="\t<composite n=\"1\" ref=\"Antimony\" />\n"
out+="\t</material>\n"
out+="<material formula=\"Al\" name=\"Aluminum_material\" >\n"
out+="\t<D value=\"2.6982\" />\n"
out+="\t<composite n=\"1\" ref=\"Aluminum\" />\n"
out+="</material>\n"
out+="<material formula=\"W\" name=\"Tungsten_material\" >\n"
out+="\t<D value=\"19.3\" />\n"
out+="\t<composite n=\"1\" ref=\"Tungsten\" />\n"
out+="</material>\n"

out+="</materials>\n"

## Define solids
out+="\n\n<solids>\n"

out+="\t<xtru name=\"solid_quartz\" lunit=\"mm\">\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(-length_quartz/2)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2+thick_quartz)+"\" y=\""+str(-thick_quartz/2)+"\"/>\n"
out+="\t\t<twoDimVertex x=\""+str(length_quartz/2)+"\" y=\""+str(thick_quartz/2)+"\"/>\n"
out+="\t\t<section zOrder=\"1\" zPosition=\""+str(-width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t\t<section zOrder=\"2\" zPosition=\""+str(width_quartz/2)+"\" xOffset=\"0\" yOffset=\"0\" scalingFactor=\"1\"/>\n"
out+="\t</xtru>\n"

out+="\t<box name=\"solid_tungsten\" lunit=\"mm\" x=\""+str(length_tungsten)+"\" y=\""+str(width_tungsten)+"\" z=\""+str(thick_tungsten)+"\"/>\n"

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

out+="\t<tube name=\"solid_pmt_filter\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_filter)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_window\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_window)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_cathode\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_cathode)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

## Mother volume single detector
out+="\t<box name=\"solid_singledet\" lunit=\"mm\" x=\""+str(800)+"\" y=\""+str(300)+"\" z=\""+str(200)+"\"/>\n"

out+="\t<box name=\"solid_showerMaxMother\" lunit=\"mm\" x=\""+str(900)+"\" y=\""+str(350)+"\" z=\""+str(250)+"\"/>\n"

## Optical Surfaces
out+="\n\t<opticalsurface name=\"quartz_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_dielectric\" value=\"0.98\" >\n"
out+="\t</opticalsurface>\n"
out+="\t<opticalsurface name=\"Al_mirror_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_metal\" value=\"0.98\" >\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"Aluminium_Surf_Reflectivity\" />\n"
out+="\t</opticalsurface>\n"
out+="\t<opticalsurface name=\"Cathode_surface\" model=\"glisur\" finish=\"polished\" type=\"dielectric_metal\" value=\"1.0\">\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"Cathode_Surf_Reflectivity\" />\n"
out+="\t\t<property name=\"EFFICIENCY\" ref=\"Cathode_Surf_Efficiency\" />\n"
out+="\t</opticalsurface>\n"

out+="</solids>\n"

## Define logical volumes using above solids
out+="\n\n<structure>\n"

for i in range(0,nSMmodules):
        for j in range(0,nQuartz):
                out+="\t<volume name=\"logic_quartz_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Quartz\"/>"
                out+="\n\t\t<solidref ref=\"solid_quartz\"/>"
                #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
                out+="\n\t</volume>\n"
      
                out+="\t<volume name=\"logic_tungsten_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Tungsten_material\"/>"
                out+="\n\t\t<solidref ref=\"solid_tungsten\"/>"
                #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"red\"/>"
                out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_suitcase_tungstenquartz_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_suitcase_tungstenquartz\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_bot\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
        out+="\n\t\t<solidref ref=\"solid_mirror_box_top\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"green\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_filter_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_filter\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"magenta\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_window_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Quartz\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_window\"/>"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t<materialref ref=\"Cathode\"/>"
        out+="\n\t\t<solidref ref=\"solid_pmt_cathode\"/>"
        out+="\n\t\t<auxiliary auxtype=\"SensDet\" auxvalue=\"PhotoCathode\" />"
        #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
        out+="\n\t</volume>\n"

        out+="\t<volume name=\"logic_singledet_"+str(i).zfill(2)+"\">"

        out+="\n\t\t<materialref ref=\"Air\"/>"
        out+="\n\t\t<solidref ref=\"solid_singledet\"/>"

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

        out+="\n\t\t<physvol name=\"pmt_filter_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_filter_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_filter_"+str(i)+"\" x= \""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_filter/2)+"\" y=\"0\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_filter_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_window_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_window_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_filter+length_pmt_window/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_cathode_"+str(i)+"\" x=\""+str(length_quartz/2+length_ledge/2+length_mirror_box_bot+length_mirror_box_top+length_top_support+length_pmt_filter+length_pmt_window+length_pmt_cathode/2)+"\" y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_cathode_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
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

        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
        out+="\n\t</volume>\n"
            
out+="\t<volume name=\"showerMaxMother\">"
out+="\n\t\t<materialref ref=\"Air\"/>"
out+="\n\t\t<solidref ref=\"solid_showerMaxMother\"/>"

# Place all modules in the showerMaxMother volume
for i in range(0,nSMmodules):
        out+="\n\t\t<physvol name=\"singledet_"+str(i).zfill(2)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_singledet_"+str(i).zfill(2)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_singledet_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_singledet_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t</physvol>"

out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
out+="\n\t</volume>\n\n"

# Specify surfaces
out+="\t<skinsurface name=\"quartz_skin_surface\" surfaceproperty=\"quartz_surface\" >\n"
for j in range(4):
        out+="\t\t<volumeref ref=\"logic_quartz_"+str(i)+"_"+str(j)+"\"/>\n"
out+="\t</skinsurface>\n"
out+="\t<skinsurface name=\"suitcase_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
out+="\t\t<volumeref ref=\"logic_suitcase_tungstenquartz_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"
out+="\t<skinsurface name=\"mirror_box_top_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
out+="\t\t<volumeref ref=\"logic_mirror_box_top_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"
out+="\t<skinsurface name=\"mirror_box_bottom_skin_surface\" surfaceproperty=\"Al_mirror_surface\" >\n"
out+="\t\t<volumeref ref=\"logic_mirror_box_bot_"+str(i)+"\"/>\n"
out+="\t</skinsurface>\n"
out+="\t<bordersurface name=\"cathode_window_border_surface\" surfaceproperty=\"Cathode_surface\" >\n"
out+="\t<physvolref ref=\"pmt_window_"+str(i)+"\"/>\n"
out+="\t<physvolref ref=\"pmt_cathode_"+str(i)+"\"/>\n"
out+="\t</bordersurface>\n"

out+="\n</structure>\n"

out+="<setup name=\"showerMaxWorld\" version=\"1.0\">"
out+="\n\t<world ref=\"showerMaxMother\"/>"
out+="\n</setup>\n"

out+="</gdml>\n"

f.write(out)

print("Succesfully written to GDML file.")
