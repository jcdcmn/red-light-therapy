# Red Light Therapy

Python code to calculate an optimum dose for red light therapy.

In a full-body red light therapy pod from www.NovoThor.com, one lies in the pod and receives 16mW/cm2 for 8 minutes, for a total of 8 joules per square centimetre of skin.

To get the same effect from off-the-shelf grow lights, purchase some panels with the same wavelength as the NovoThor, which is 650nm and 810nm. Arrange four panels on the wall in a 2x2 grid. Using a light meter such as the TES-1333, find the right distance where the light intensity reads "160" on the meter. The meter is in W/m2, so this represents 16mW/cm2 of light intensity, same as the NovoThor.

There are 360 degrees in a circle. Stand facing the panel, then rotate 45 degrees every 60 seconds. After 480 seconds, every square centimetre of skin will have received a fraction of the dose that an 8-minute session in the NovoThor would deliver.

But what is that fraction? Use the attached Python code to get a better estimate.

It turns out that if the light intensity on the skin is the same as the NovoThor, at between 15 and 20mW/cm2, then 60 seconds at each 45 degree angle is equivalent to 20% of a standard 12-minute NovoThor session.

The output of the program is as follows:

```c
Red Light Therapy Dose Calculator
  - See: https://github.com/sharpe5/red-light-therapy/
User set variables:
  - What does our TES-1333 light meter read in W/m2? 160
  - Total seconds at each 45 degree angle: 60
Calculated (intermediate):
  - Total number of 45 degree angles in 360 degreese: 8
  - Total seconds to rotate 360 degrees: 480
  - Total minutes to rotate 360 degrees: 8.0
  - Total joules/centimetre2 this: 2.3176450198781713
  - Total minutes in NovoThor: 0.2
  - Light intensity in NovoThor [mW/cm2]: 16.666
  - Total joules/centimetre2 NovoThor: 11.99952
Calculated (final value):
  - Percent dose compared to one full-body NovoThor session of 12 minutes @ 16.666 mW/cm2: 19.3%
```
