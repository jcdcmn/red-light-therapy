# Red Light Therapy

Python code to calculate an optimum dose for red light therapy.

In a full-body red light therapy pod from www.NovoThor, one lies in the pod and receives 16mW/cm2 for 8 minutes, for a total of 8 joules per square centimetre of skin.

To get the same effect from off-the-shelf grow lights, purchase some panels with the same wavelength as the NovoThor, which is 650nm and 810nm. Arrange four panels on the wall in a 2x2 grid. Using a light meter such as the TES-1333, find the right distance where the light intensity reads "160" on the meter. The meter is in W/m2, so this represents 16mW/cm2 of light intensity, same as the NovoThor.

There are 360 degrees in a circle. Stand facing the panel, then rotate 45 degrees every 60 seconds. After 480 seconds, every square centimetre of skin will have received a fraction of the dose that an 8-minute session in the NovoThor would deliver.

But what is that fraction? Use the attached Python code to get a rough estimate.

The output of the program is as follows:

  Total seconds at each 45 degree angle: 60
  Total number of 45 degree angles in 360 degreese: 8
  Total seconds to rotate 360 degrees: 480
  Total minutes to rotate 360 degrees: 8.0
  What does our TES-1333 light meter read in W/m2? 260
  Total joules/centimetre2 this: 3.7661731573020285
  Total minutes NovoThor: 12.0
  Total joules/centimetre2 NovoThor: 11.99952
  Percent of NovoThor: 31.38603175212032
