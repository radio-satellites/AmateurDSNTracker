from astroquery.jplhorizons import Horizons
import argparse
import datetime

time = datetime.datetime.utcnow()

argparser = argparse.ArgumentParser()

argparser.add_argument("--latitude", "-lat", action="store")
argparser.add_argument("--longitude", "-lon", action="store")
argparser.add_argument("--timeproxy", "-len", action="store")
argparser.add_argument("--target", "-t", action="store")

args = argparser.parse_args()

longitude = -54.444232
latitude = 46.444232
target = str(-234)

pred_length = 9 #hours

if args.latitude:
    try:
        latitude = float(args.latitude)
    except:
        print("Latitude '"+args.latitude+"' is invalid!")
        exit()

if args.longitude:
    try:
        longitude = float(args.longitude)
    except:
        print("Latitude '"+args.longitude+"' is invalid!")
        exit()

if args.target:
    try:
        target = str(args.target)
    except:
        print("Latitude '"+args.target+"' is invalid!")
        exit()
    
if args.timeproxy:
    try:
        pred_length = int(args.timeproxy)
    except:
        print("Invalid time proxy '"+args.timeproxy+"'!")
        exit()

print("HORIZONS QUERY")
print("BY VE3SVF!")

print("\n\n\n")

print("Using observer "+str(latitude)+","+str(longitude)+" for object ID "+str(target))
        
observer = {'lon': longitude,
                     'lat': latitude,
                     'elevation': 0.093}

print("Create query...")

obj = Horizons(id=target, location=observer,
               epochs={'start':str(time+datetime.timedelta(minutes=1)), 'stop':str(time+ datetime.timedelta(hours=pred_length)),
                       'step':'1m'})

print("Send query...")
eph = obj.ephemerides()

print("Done query!")

times = eph["datetime_str"]

az = eph["AZ"]

el = eph["EL"]

for i in range(len(times)):
    times[i] == datetime.datetime.strptime(str(times[i]), '%Y-%b-%d %H:%M:%S.%f')

print("AZ EL DATA (live)")
print("[DEBUG] FIRST PREDICTION AT TIME " + str(times[0]))
print("TARGET NAME: "+str(eph['targetname'][0]))
print("0x11") #Start data header

counter = 0
total_data = len(times)


while True:
    current_time = datetime.datetime.strptime(str(times[counter]), '%Y-%b-%d %H:%M:%S.%f')
    if datetime.datetime.utcnow().hour == current_time.hour and datetime.datetime.utcnow().minute == current_time.minute:
        print(str(az[counter])+","+str(el[counter]))
        counter = counter + 1
    if counter == total_data:
        print("FINISHED!")
        exit()
        
