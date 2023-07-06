# AmateurDSNTracker

Track spacecraft without TLEs using the Horizons network. 

# Running

`python tracker.py -lat 55.44444 -lon 78.33333 -target -234`

This will track Stereo-A (object -234 in the database ) from a perspective of a ground station located at 55.44444,78.33333. It will output the az/el in real time after the 0x11 header. 
