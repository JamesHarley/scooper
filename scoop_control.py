#scoop_control
#import scoop
from datetime import datetime

print("********************************************************************************")
print("Started: "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("********************************************************************************")
import scoop_remote
import scoop_gigs
import scoop_json_gig
import scoop_json_remote
 
print("################################################################################")
print("Finished: "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("################################################################################")