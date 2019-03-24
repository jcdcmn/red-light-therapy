# Dose calculator for red light therapy (i.e. photobiomodulation).
# Compares dose from off-the-shell red light therapy panels to dose from a full body light pod from www.NovoThor.com.
# https://github.com/sharpe5/red-light-therapy/

import os
import math
import argparse
import sys

parser = argparse.ArgumentParser(description='Dose calculator for red light therapy.')
parser.add_argument('watts', metavar='WATTS', type=int, default=160, nargs='?', help='Watts Per Squared Meter')
parser.add_argument('seconds', metavar='SECONDS', type=int, default=60, nargs='?', help='Seconds Per 45 Degree Round')
args = parser.parse_args()

print("Photobiomodulation (Red Light Therapy) Dose Calculator")
print("  - Help screen: %s -h" % sys.argv[0])
print("  - Instructions: https://github.com/sharpe5/red-light-therapy/")
print("")
print("User set variables:")

this_watts_per_meter = args.watts
# Note: This is 10x the value in mW/cm2 (milliwatts to watts is 1000, and 10000 square centimetres in a in metre.
print("  - What does our TES-1333 light meter read in W/m2? " + str(this_watts_per_meter))
print("    - Note: stand closer or further away to adjust this value. Should measure between 150 and 200 W/m2.")

# How many seconds we spend at each 45 degree angle. This is the *only* variable we have to manually change.
this_total_seconds_per_eighth = args.seconds
print("  - Total seconds spent standing at each 45 degree angle: " + str(this_total_seconds_per_eighth))
print("    - Note: typically, a good dose is achieved by spending between 60 and 150 seconds at each 45 degree angle.")

print("")
print("Calculated (NovoThor):")

# What we would get from a full body light pod from www.NovoThor.com in N minutes.
novothor_time_minutes = 10
print("  - Total minutes in NovoThor: " + str(novothor_time_minutes))
novothor_time_seconds = 60 * novothor_time_minutes
novothor_millijoules_per_centimetre = 16.666
print("  - Light intensity in NovoThor [mW/cm2]: " + str(novothor_millijoules_per_centimetre))
print("    - Note: W/m2 is ten times the value in mW/cm2, as there is 10000 square centimeters in a metre, and 1000 milliwatts in a watt.")
novothor_total_joules_per_square_centimetre = novothor_time_seconds * novothor_millijoules_per_centimetre / 1000.0
print("  - Total joules/centimetre2 NovoThor: " + str(round(novothor_total_joules_per_square_centimetre,1)))

print("")
print("Calculated (off-the-shelf red light therapy panels):")

print("  - Light intensity as measured by TES-1333 light meter [W/m2]: " + str(this_watts_per_meter))
print("    - Note: W/m2 is ten times the value in mW/cm2, as there is 10000 square centimeters in a metre, and 1000 milliwatts in a watt.")

this_total_seconds = this_total_seconds_per_eighth * 8
print("  - Total number of 45 degree angles in 360 degrees: 8")

print("  - Total seconds to rotate 360 degrees: " + str(this_total_seconds))
print("  - Total minutes to rotate 360 degrees: " + str(this_total_seconds / 60))

this_milliwatts_per_centimeter = this_watts_per_meter / 10
# each square centimetre of skin gets three exposures: facing panel, previous (45 degrees less), next (45 degrees more)
# first position, facing straight at the panel
this_total_joules_position_1 = this_total_seconds_per_eighth * this_milliwatts_per_centimeter / 1000.0
# next position, rotated 45 more degrees facing the panel
this_total_joules_position_2 = this_total_joules_position_1 * math.cos(math.radians(45))
# previous position, rotated 45 less degrees facing the panel
this_total_joules_position_3 = this_total_joules_position_1 * math.cos(math.radians(45))
this_total_joules_this = this_total_joules_position_1 + this_total_joules_position_2 + this_total_joules_position_3

print("  - Total joules/centimetre2 this: " + str(round(this_total_joules_this,2)))


print("")
print("Calculated (final value):")
percent_our_setup_of_novothor = this_total_joules_this / novothor_total_joules_per_square_centimetre * 100
print("  - Percent dose compared to one full-body NovoThor session of " + str(novothor_time_minutes) + " minutes @ "
      + str(novothor_millijoules_per_centimetre) + " mW/cm2: " + str(round(percent_our_setup_of_novothor, 1)) + "%")
