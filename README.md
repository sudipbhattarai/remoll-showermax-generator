# remoll-showermax-generator
Generator for producing gdml file for remoll showermax detectors.


Modify parameters and execute:
```python
python showermaxgen.py
````

By default, the position is set to
```
pos=radial_extent+length_quartz/2
```
So, the detector active area ranges from 1020 to 1180 mm for upstream ring(open and close sector) and 1024 to 1184 for downstream ring (trans sectors) . Make sure that this range is in the shadow of the main detector ring 5 (920-1060 mm) at 22 m. 

To introduce detector tilt, change the detector_tilt variable. By default, it is set to 0. In the picture below, it's set to -math.pi/6 or -30 degrees. For shallow angles, the existing stagger and mother volume extent might be fine. Check for overlaps if you are going to large angles as shown and increase the mother volume extent (len_mother) and zstagger variables.
```
detector_tilt = -math.pi/6
```

![showermaxPeak](https://user-images.githubusercontent.com/7409132/124005187-66f00c00-d99e-11eb-8b68-e994946d7a48.JPG)

