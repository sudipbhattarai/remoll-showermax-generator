import math

### Define geometry parameters(dimensions based on ISU elog 576):
radial_extent = 1020.0          #distance from beam center to tungsten-quartz bottom on US ring
nQuartz = 4
nSMmodules = 1
in2mm = 25.4
output_file = "smBenchmark"+str(nQuartz)+"stackQsim"

## Quartz
length_quartz = 80.0
width_quartz = 40.0
thick_quartz = 6.0
quartz_rotate = ["pi/2", "-pi/2", "pi/2", "-pi/2"]

## Tungsten 
length_tungsten = length_quartz
width_tungsten = width_quartz
thick_tungsten = 8.0

## Spacer in TQ stack
thick_spacer = 0.3
thick_tolerance = 0.0

## Tungsten-quartz stack
length_stack_tungstenquartz = length_quartz
width_stack_tungstenquartz = width_quartz
thick_stack_tungstenquartz = 4*(thick_quartz+thick_tungsten)+ 8*thick_spacer + 2*thick_tolerance

# Mylar wrapping
thick_wrap_film = 0.075
length_wrap = length_quartz + 2*thick_wrap_film
width_wrap = width_quartz
thick_wrap = thick_quartz + 4*thick_wrap_film

## mirror parameter
thick_wall_mirror = 0.5

## PMT region
radius_pmt = 1.5*in2mm # Radius of 1.5 inches (for 3 inches PMT)
length_pmt_cathode = 3e-6
length_pmt_window = 3.0

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

out+="\t<box name=\"solid_wrap_1\" lunit=\"mm\" x=\""+str(length_wrap)+"\" y=\""+str(width_wrap)+"\" z=\""+str(thick_wrap)+"\"/>\n"
out+="\t<box name=\"solid_wrap_2\" lunit=\"mm\" x=\""+str(length_wrap+0.1)+"\" y=\""+str(width_wrap+1.0)+"\" z=\""+str(thick_wrap-2*thick_wrap_film)+"\"/>\n"

out+="\t<subtraction name=\"solid_wrap\">"
out+="\n\t\t<first ref=\"solid_wrap_1\"/>"
out+="\n\t\t<second ref=\"solid_wrap_2\"/>"
out+="\n\t\t<position name=\"pos_subtract_wrap_12\" x=\""+str(thick_wrap_film)+"\" y=\"0\" z=\"0\"/>"
out+="\n\t\t<rotation name=\"rot_subtract_wrap_12\" x=\"0\" y=\"0\" z=\"0\"/>"
out+="\n\t</subtraction>\n"
#-------------------

out+="\t<tube name=\"solid_pmt_window\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_window)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

out+="\t<tube name=\"solid_pmt_cathode\" rmin=\"0\" rmax=\""+str(radius_pmt)+"\" z=\""+str(length_pmt_cathode)+"\" deltaphi=\"2*pi\" startphi=\"0\" aunit=\"rad\" lunit=\"mm\"/>\n"

## Mother volume single detector
out+="\t<box name=\"solid_singledet\" lunit=\"mm\" x=\""+str(400)+"\" y=\""+str(150)+"\" z=\""+str(100)+"\"/>\n"

out+="\t<box name=\"solid_showerMaxMother\" lunit=\"mm\" x=\""+str(450)+"\" y=\""+str(200)+"\" z=\""+str(150)+"\"/>\n"

## Optical Surfaces
out+="\n\t<opticalsurface name=\"quartz_surface\" model=\"glisur\" finish=\"ground\" type=\"dielectric_dielectric\" value=\"0.98\" >\n"
out+="\t</opticalsurface>\n"

out+="\t<opticalsurface name=\"mylar_surface\" model=\"glisur\" finish=\"polished\" type=\"dielectric_metal\" value=\"1.0\" >\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"Mylar_REFLECTIVITY_30DEG\" />\n"
out+="\t</opticalsurface>\n"

out+="\t<opticalsurface name=\"Cathode_surface\" model=\"glisur\" finish=\"polished\" type=\"dielectric_metal\" value=\"1.0\">\n"
out+="\t\t<property name=\"REFLECTIVITY\" ref=\"CathodeSurf_REFLECTIVITY\" />\n"
out+="\t\t<property name=\"EFFICIENCY\" ref=\"Cathode_EFFICIENCY\" />\n"
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

                out+="\t<volume name=\"logic_wrap_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t<materialref ref=\"Aluminum_material\"/>"
                out+="\n\t\t<solidref ref=\"solid_wrap\"/>"
                #out+="\n\t\t<auxiliary auxtype=\"Color\" auxvalue=\"blue\"/>"
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
        out+="\n\t\t<physvol name=\"pmt_window_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_window_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_window_"+str(i)+"\" x=\""+str(length_quartz/2+10+length_pmt_window/2)+"\" \
                        y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
        out+="\n\t\t\t<rotation name=\"rot_logic_pmt_window_"+str(i)+"\" x=\"0\" y=\"-pi/2\" z=\"0\"/>"
        out+="\n\t\t</physvol>"

        out+="\n\t\t<physvol name=\"pmt_cathode_"+str(i)+"\">"
        out+="\n\t\t\t<volumeref ref=\"logic_pmt_cathode_"+str(i)+"\"/>"
        out+="\n\t\t\t<position name=\"pos_logic_pmt_cathode_"+str(i)+"\" x=\""+str(length_quartz/2+10+length_pmt_window+length_pmt_cathode/2)+"\" \
                        y=\""+str(0)+"\" z=\""+str(thick_tungsten/2)+"\"/>"
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

                out+="\n\t\t<physvol name=\"wrap_"+str(i)+"_"+str(j)+"\">"
                out+="\n\t\t\t<volumeref ref=\"logic_wrap_"+str(i)+"_"+str(j)+"\"/>"             
                out+="\n\t\t\t<position name=\"pos_logic_wrap_"+str(i)+"_"+str(j)+"\" x=\""+str(0)+"\" y=\""+str(0)+"\" z=\""+str(1.5*thick_quartz+2.0*thick_tungsten+4*thick_spacer+thick_tolerance-j*(thick_quartz+thick_tungsten)-(2*j+1)*thick_spacer)+"\"/>"
                out+="\n\t\t\t<rotation name=\"rot_logic_wrap_"+str(i)+"_"+str(j)+"\" x=\"0\" y=\"0\" z=\"0\"/>"        
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
for j in range(nQuartz):
        out+="\t\t<volumeref ref=\"logic_quartz_"+str(i)+"_"+str(j)+"\"/>\n"
out+="\t</skinsurface>\n"
for iMod in range(0,nSMmodules):
    for iWrap in range(0,nQuartz):
        out+="\t<skinsurface name=\"wrap_skin_surface_"+str(iMod)+"_"+str(iWrap)+"\" surfaceproperty=\"mylar_surface\" >\n"
        out+="\t\t<volumeref ref=\"logic_wrap_"+str(iMod)+"_"+str(iWrap)+"\"/>\n"
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

print("Succesfully written GDML file: "+output_file)
