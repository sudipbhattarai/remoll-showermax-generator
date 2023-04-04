import math

output_file = "ring5"

### Define geometry parameters(dimensions based on ISU elog 576):
nModules = 1
nQuartz = 1
in2mm = 25.4
lightGuide_tilt = 2.5 # tilt angle of the light guide wrt quartz

## Quartz
length_quartz = 140.0
width_quartz = 80.0
thick_quartz = 15.0

zPos_Quartz = (length_quartz/2-1)*math.tan(lightGuide_tilt*math.pi/180) # 1 mm overlap of quartz and mirror box
print(zPos_Quartz)


## Mirror box bottom (lower part of the light guide)
length_mirror_box_bot = 90.0
x1_mirror_box_bot = 24.0
x2_mirror_box_bot = 84.131
y1_mirror_box_bot = 88.0
y2_mirror_box_bot = 88.0

xPos_mirror_box_bot_noTilt = length_quartz/2-1+length_mirror_box_bot/2  # 1 mm overlap of quartz and mirror box
zPos_mirror_box_bot_noTilt = 0.0
xPos_mirror_box_bot = xPos_mirror_box_bot_noTilt*math.cos(lightGuide_tilt*math.pi/180) - zPos_mirror_box_bot_noTilt*math.sin(lightGuide_tilt*math.pi/180) # rotate the mirror box by lightGuide_tilt
zPos_mirror_box_bot = xPos_mirror_box_bot_noTilt*math.sin(lightGuide_tilt*math.pi/180) + zPos_mirror_box_bot_noTilt*math.cos(lightGuide_tilt*math.pi/180)

## Mirror box top (upper part of the light guide)
length_mirror_box_top = 183.058
x1_mirror_box_top = x2_mirror_box_bot
x2_mirror_box_top = 71.88
y1_mirror_box_top = y2_mirror_box_bot
y2_mirror_box_top = 71.88

xPos_mirror_box_top_noTilt = length_quartz/2-1+length_mirror_box_bot+length_mirror_box_top/2  # 1 mm overlap of quartz and mirror box
zPos_mirror_box_top_noTilt = 0.0
xPos_mirror_box_top = xPos_mirror_box_top_noTilt*math.cos(lightGuide_tilt*math.pi/180) - zPos_mirror_box_top_noTilt*math.sin(lightGuide_tilt*math.pi/180) # rotate the mirror box by lightGuide_tilt
zPos_mirror_box_top = xPos_mirror_box_top_noTilt*math.sin(lightGuide_tilt*math.pi/180) + zPos_mirror_box_top_noTilt*math.cos(lightGuide_tilt*math.pi/180)

## mirror parameter
thick_wall_mirror = 0.5

## PMT region
radius_pmt = 1.5*in2mm # Radius of 1.5 inches (for 3 inches PMT)
length_pmt_cathode = 3e-6
length_pmt_window = 3.0

xPos_pmt_window_noTilt = length_quartz/2-1+length_mirror_box_bot+length_mirror_box_top+length_pmt_window/2  # 1 mm overlap of quartz and mirror box
zPos_pmt_window_noTilt = 0.0
xPos_pmt_window = xPos_pmt_window_noTilt*math.cos(lightGuide_tilt*math.pi/180) - zPos_pmt_window_noTilt*math.sin(lightGuide_tilt*math.pi/180) # rotate the mirror box by lightGuide_tilt
zPos_pmt_window = xPos_pmt_window_noTilt*math.sin(lightGuide_tilt*math.pi/180) + zPos_pmt_window_noTilt*math.cos(lightGuide_tilt*math.pi/180)

xPos_pmt_cathode_noTilt = length_quartz/2-1+length_mirror_box_bot+length_mirror_box_top+length_pmt_window+length_pmt_cathode/2  # 1 mm overlap of quartz and mirror box
zPos_pmt_cathode_noTilt = 0.0
xPos_pmt_cathode = xPos_pmt_cathode_noTilt*math.cos(lightGuide_tilt*math.pi/180) - zPos_pmt_cathode_noTilt*math.sin(lightGuide_tilt*math.pi/180) # rotate the mirror box by lightGuide_tilt
zPos_pmt_cathode = xPos_pmt_cathode_noTilt*math.sin(lightGuide_tilt*math.pi/180) + zPos_pmt_cathode_noTilt*math.cos(lightGuide_tilt*math.pi/180)


thick_mother=100.0

f=open(output_file+".gdml", "w+")

## GDML schema
out="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n"

out+="<!DOCTYPE gdml [\n"
out+="\t<!ENTITY matrices SYSTEM \"showerMaxMatrices.xml\">\n"
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

out+="<material formula=\"noFormula\" name=\"Air\" >\n"
out+="\t<property name=\"RINDEX\" ref=\"Air_RINDEX\"/>\n"
out+="\t<D value=\"0.00129\" />\n"
out+="\t<fraction n=\"0.3\" ref=\"Oxygen\" />\n"
out+="\t<fraction n=\"0.7\" ref=\"Nitrogen\" />\n"
out+="</material>\n"
out+="<material formula=\"SiO2\" name=\"Quartz\" >\n"
out+="\t<property name=\"RINDEX\" ref=\"Quartz_RINDEX\"/>\n"
out+="\t<property name=\"ABSLENGTH\" ref=\"Quartz_ABSLENGTH_DATA\"/>\n"
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

# Mirror box bottom(lower part of the light guide)
out+="\t<trd name=\"solid_mirror_box_bot_1\" lunit=\"mm\" x1=\""+str(x1_mirror_box_bot)+"\"  x2=\""+str(x2_mirror_box_bot)+"\" y1=\""+str(y1_mirror_box_bot)+"\"  y2=\""+str(y2_mirror_box_bot)+"\" z=\""+str(length_mirror_box_bot)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_bot_2\" lunit=\"mm\" x1=\""+str(x1_mirror_box_bot-2*thick_wall_mirror)+"\"  x2=\""+str(x2_mirror_box_bot-2*thick_wall_mirror)+"\" y1=\""+str(y1_mirror_box_bot-2*thick_wall_mirror)+"\"  y2=\""+str(y2_mirror_box_bot-2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_bot+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_bot\">"
out+="\n\t\t<first ref=\"solid_mirror_box_bot_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_bot_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_bot_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

# Mirror box top(upper part of the light guide)
out+="\t<trd name=\"solid_mirror_box_top_1\" lunit=\"mm\" x1=\""+str(x1_mirror_box_top)+"\"  x2=\""+str(x2_mirror_box_top)+"\" y1=\""+str(y1_mirror_box_top)+"\"  y2=\""+str(y2_mirror_box_top)+"\" z=\""+str(length_mirror_box_top)+"\"/>\n"
out+="\t<trd name=\"solid_mirror_box_top_2\" lunit=\"mm\" x1=\""+str(x1_mirror_box_top-2*thick_wall_mirror)+"\"  x2=\""+str(x2_mirror_box_top-2*thick_wall_mirror)+"\" y1=\""+str(y1_mirror_box_top-2*thick_wall_mirror)+"\"  y2=\""+str(y2_mirror_box_top-2*thick_wall_mirror)+"\" z=\""+str(length_mirror_box_top+1)+"\"/>\n"

out+="\t<subtraction name=\"solid_mirror_box_top\">"
out+="\n\t\t<first ref=\"solid_mirror_box_top_1\"/>"
out+="\n\t\t<second ref=\"solid_mirror_box_top_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>" 
out+="\n\t\t<rotation name=\"rot_subtract_mirror_box_top_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

out+="\t<tube name=\"solid_pmt_window\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_window)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_cathode\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_cathode)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

## Mother volume single detector
out+="\t<box name=\"solid_singledet\" lunit=\"mm\" x=\""+str(800)+"\" y=\""+str(300)+"\" z=\""+str(200)+"\"/>\n"

out+="\t<box name=\"solid_ring5Mother\" lunit=\"mm\" x=\""+str(900)+"\" y=\""+str(350)+"\" z=\""+str(250)+"\"/>\n"

## Optical Surfaces
out+="\n\t<opticalsurface name=\"quartz_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_dielectric\" value=\"0.98\" >\n"
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

for i in range(0,nModules):
        for j in range(0,nQuartz):
                out+="\t<volume name=\"logic_quartz_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Quartz\"/>"
                out+="\n\t\t<solidref ref=\"solid_quartz\"/>"
                #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
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
        out+="\n\t\t<physvol name=\"mirror_box_bot_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_bot_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(xPos_mirror_box_bot)+"\" y=\""+str(0)+"\" z=\""+str(zPos_mirror_box_bot)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_bot_"+str(i)+"\" x=\""+str(0)+"\" y=\"-90+2.5"+"\" z=\"0\" unit=\"deg\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"mirror_box_top_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_mirror_box_top_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_mirror_box_top_"+str(i)+"\" x=\""+str(xPos_mirror_box_top)+"\" y=\""+str(0)+"\" z=\""+str(zPos_mirror_box_top)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_mirror_box_top_"+str(i)+"\" x=\""+str(0)+"\" y=\"-90+2.5\" z=\"0\" unit=\"deg\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_window_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_window_"+str(i)+"\" x=\""+str(xPos_pmt_window)+"\" y=\""+str(0)+"\" z=\""+str(zPos_pmt_window)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-90+2.5\" z=\"0\" unit=\"deg\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_cathode_"+str(i)+"\" x=\""+str(xPos_pmt_cathode)+"\" y=\""+str(0)+"\" z=\""+str(zPos_pmt_cathode)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_cathode_"+str(i)+"\" x=\"0\" y=\"-90+2.5\" z=\"0\" unit=\"deg\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"quartz_"+str(i)+"_"+str(j)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_quartz_"+str(i)+"_"+str(j)+"\"/>"             
        out+="\n\t\t\t<position name=\"pos_logic_quartz_"+str(i)+"_"+str(j)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(zPos_Quartz)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_quartz_"+str(i)+"_"+str(j)+"\" x=\"-pi/2\" y=\"0\" z=\"0\"/>"        
        out+="\n\t\t</physvol>"

        out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
        out+="\n\t</volume>\n"
            
out+="\t<volume name=\"ring5Mother\">"
out+="\n\t\t<materialref ref=\"Air\"/>"
out+="\n\t\t<solidref ref=\"solid_ring5Mother\"/>"

# Place all modules in the ring5Mother volume
for i in range(0,nModules):
        out+="\n\t\t<physvol name=\"singledet_"+str(i).zfill(2)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_singledet_"+str(i).zfill(2)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_singledet_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_singledet_"+str(i)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(0)+"\"/>"
        out+="\n\t\t</physvol>"

out+="\n\t\t<auxiliary auxtype=\"Alpha\" auxvalue=\"0.0\"/>"
out+="\n\t</volume>\n\n"

# Specify surfaces
out+="\t<skinsurface name=\"quartz_skin_surface\" surfaceproperty=\"quartz_surface\" >\n"
for j in range(nQuartz):
        out+="\t\t<volumeref ref=\"logic_quartz_"+str(i)+"_"+str(j)+"\"/>\n"
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

out+="<setup name=\"ring5World\" version=\"1.0\">"
out+="\n\t<world ref=\"ring5Mother\"/>"
out+="\n</setup>\n"

out+="</gdml>\n"

f.write(out)

print("Succesfully written to GDML file.")
