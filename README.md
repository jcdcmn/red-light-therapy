# Red Light Therapy

Python code to calculate an optimum dose for red light therapy.

This script compares the dose from a full body light pod from www.NovoThor.com, to a setup of off-the-shelf grow lights at the same light intensity and frequency. 

## Discussion on Reddit

https://www.reddit.com/r/Nootropics/comments/avulcd/budget_led_light_therapy_infared_red_blue_uv_etc/
https://www.reddit.com/r/Biohackers/comments/a1vdl7/best_full_body_redlight/

## Instructions

In a full-body red light therapy pod from www.NovoThor.com, one lies in the pod and receives 16mW/cm2 or 1 joule per minute. After 10 minutes, this is 10 joules per square centimetre of skin.

To get the same effect from off-the-shelf grow lights, purchase some panels with the same wavelength as the NovoThor, which is 650nm and 810nm. Arrange four panels on the wall in a 2x2 grid. Using a light meter such as the TES-1333, find the right distance where the light intensity reads "160" on the meter. The meter is in W/m2, so this represents 16mW/cm2 of light intensity, same as the NovoThor.

There are 360 degrees in a circle. Stand facing the panel, then rotate 45 degrees every 60 seconds. After 480 seconds, every square centimetre of skin will have received a fraction of the dose that an 12-minute session in the NovoThor would deliver.

But what is that fraction? Use the attached Python code to get a better estimate.

The output of the program is as follows:

```
Photobiomodulation (Red Light Therapy) Dose Calculator
  - Instructions: https://github.com/sharpe5/red-light-therapy/
User set variables:
  - What does our TES-1333 light meter read in W/m2? 160
    - Note: stand closer or further away to adjust this value. Should measure between 150 and 200 W/m2.
  - Total seconds spent standing at each 45 degree angle: 60
    - Note: typically, a good dose is achieved by spending between 60 and 150 seconds at each 45 degree angle.
Calculated (NovoThor):
  - Total minutes in NovoThor: 10
  - Light intensity in NovoThor [mW/cm2]: 16.666
  - Total joules/centimetre2 NovoThor: 10.0
Calculated (off-the-shelf red light therapy panels):
  - Total number of 45 degree angles in 360 degrees: 8
  - Total seconds to rotate 360 degrees: 480
  - Total minutes to rotate 360 degrees: 8.0
  - Total joules/centimetre2 this: 2.3176450198781713
Calculated (final value):
  - Percent dose compared to one full-body NovoThor session of 10 minutes @ 16.666 mW/cm2: 23.2%
```

## Warnings

Read said Reddit posts for warnings on:
- Exposure to eyes.
- Exposure to testicles.
- Overdosing.

## Summary

It turns out that if the light intensity on the skin is the same as the NovoThor, at between 15 and 20mW/cm2, then 60 seconds at each 45 degree angle is equivalent to 20% of a standard 12-minute NovoThor session.

## Pull Requests

Spotted a way to improve this estimation? Pull requests welcome.
