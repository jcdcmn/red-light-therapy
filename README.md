# Red Light Therapy

Python code to calculate an optimum dose for red light therapy.

This script compares the dose from a full body light pod from www.NovoThor.com, to a setup of off-the-shelf grow lights at the same light intensity and frequency. 

## Discussion on Reddit

https://www.reddit.com/r/Nootropics/comments/avulcd/budget_led_light_therapy_infared_red_blue_uv_etc/
https://www.reddit.com/r/Biohackers/comments/a1vdl7/best_full_body_redlight/

## Instructions

In a full-body red light therapy pod from www.NovoThor.com, one lies in the pod and receives 16mW/cm2 or 1 joule per minute. After 10 minutes, this is 10 joules per square centimetre of skin.

To get the same effect from off-the-shelf grow lights, purchase some panels with the same wavelength as the NovoThor, which is 650nm and 810nm. Arrange four panels on the wall in a 2x2 grid. Using a light meter such as the TES-1333, find the right distance where the light intensity reads "160" on the meter. The meter is in W/m2, so this represents 16mW/cm2 of light intensity, same as the NovoThor.

There are 360 degrees in a circle. Stand facing the panel, then rotate 45 degrees every 60 seconds. After 480 seconds, every square centimetre of skin will have received a fraction of the dose that an 10-minute session in the NovoThor would deliver.

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

It turns out that if the light intensity on the skin is the same as the NovoThor, at between 15 and 20mW/cm2, then 60 seconds at each 45 degree angle is equivalent to 20% of a standard 10-minute NovoThor session.

# Original Reddit Post

## Title: Build your own red light therapy rig

Source: I beat chronic pain using a full body red light therapy rig. I do have a science degree which helped with the physics side of the build. This tries to summarize 12 months of experience.

### Check 1: Light intensity

If any manufacturer says "we are better", just ignore them and ask them two questions:

1. Light intensity in W/m2 at 100cm.
2. Light intensity in W/m2 at 100cm and 30cm off to the side.

To verify light intensity, ask for a photo of them holding a light meter at a certain distance.

There are two main types of lens available: 90 degree and 60 degree.

* A 60 degree lens will give *more* even light coverage, so the intensity on the arms will be similar to that in the center of the chest.
* A 90 degree lens will give *less* even light coverage, because the light from each LED spreads out so much that a lot of it will miss you.

For this reason, ask for a 60 degree lens.

### Check 2: Understand difference between W/m2 and mW/cm2

One is 10x the other:

- To convert mW/cm2 to W/m2, multiply by 10.
- To convert W/m2 to mW/cm2, divide by 10.

A light meter such as the TES-1333 measures in W/m2. Divide their values by 10 to get mW/cm2.

### Check 3: Can you get 160W/m2 light intensity on your skin?

The NovoThor from www.NovoThor.com is the gold standard for fully body light pods. They are $120,000. Other light panels are much better value (a tiny fraction of the cost). NovoThor pods deliver an average of 16mW/cm2 over the entire body. This is what you should be aiming for. In other words, stand the right distance away so your light meter reads 160W/m2. If you want full body, then turn 45 degrees every few minutes. You can go up to 30mW/cm if you reduce the time.

### Check 4: Light: 50% red and 50% infrared?

Do the specs say that the light panel is producing red (650nm) and infrared (810nm)? If in doubt, look at the specs for the NovoThor and try to match them.

### Check 5: Buy a light meter

A light meter is essential. I have the TES-1333. Any light meter will do, as long as it is sensitive to 650nm (red) and 810nm (infrared) light. Some manufacturers have been known to mix up their mW/cm2 and W/m2, so their specs are wrong. There is no shortcut: you have to measure.

### Check 6: Where do I source the panels?

First off, don't let any manufacturer convince you that their photons are superior to other manufacturer's photons. A photon is a photon: as long as there is sufficient light intensity at the right wavelength for the right time, then all is good in the world.

If you order from any manufacturer in the US or UK, it's a no-brainer: you pay, they deliver. But what about China? The open secret is that US resellers source panels in China, and if not, the parts come from there. Most of them are made in the same factory as grow lights for plants.

In general, few hesitate when buying from eBay.com. Alibaba.com has the same consumer protections as eBay. If you complain, you get a credit card refund, just like eBay.

I sourced my light rig from Alibaba, and it was just like eBay: I paid, goods arrived 4 weeks later. The only problem with Alibaba.com is that the goods take a while to arrive (3 to 4 weeks to the UK, for example), and it's more work: you have to set up a sale by talking directly to the manufacturer.

I have not heard any bad things about SunGrow, Oneo, Platinum450, PlatinumLED, NovoThor, Joovv, etc. If you hear of any other manufacturers that deliver reliably (or not!) please let me know and I'll update this post.

### Check 7: How many panels?

The panels I purchased are 90x20cm. If you are prepared to spend 60 to 80 minutes for one full body session, then you can use one panel. If you just did your torso, then it would be a 20 to 40 minute session to get some sort of reasonable dose. I purchased 4 panels, so one session takes 20 minutes, and standing 1 metre away  gives me 75% of the dose of the NovoThor (from www.NovoThor.com).

The panels hang on my wall from heavy duty custom hooks, in a 2x2 grid which is 2 metres tall and 40cm wide. They come with wires to attach them to the mounting hooks.

### Check 8: How long do I spend in front of the panel?

So you've got a brand new full body light rig, and it's hanging on the wall like a giant picture.

In general, you want the same light dose as NovoThor. And that means 16mW/cm2 for 8 minutes on each square centimetre of skin. This works out to 1 Joule/cm2 per minute, or 8 Joules per square centimetre of skin after 8 minutes. 

Personally, I spend a total of 16 minutes in front of the full body 2x2 grid of light panels. I stand the right distance away to get 16mW/cm2 on the skin. I rotate 45 degrees every 2 minutes. If you do the math, that gives a good portion of the dose compared to NovoThor.

I actually have a Python script which does all the calculations, see https://github.com/sharpe5/red-light-therapy. Given the total time standing in front of my panel at a certain distance at a certain light intensity as measured by my light meter, what percentage of the dosage of a full body 8 minute NovoThor session am I getting, in joules / cm2? Let me know if you want me to post it. It does have a few cosines in it to account for dosage received at each angle while rotating.

### Check 9: Safety (Testicles and eyes)

Any dose between 2 Joules / cm2 and 12 Joules / cm2 is optimal. Any dose higher than that is probably too much, and any dose lower than that will have little effect. If in doubt, go by the dosages published by www.NovoThor.com. Photobiomodulation with LED lights is one of the safest medical treatments available, there is almost nothing that can go wrong. 

Eyes: Try not to look directly at the light. LED light is *not* coherent (like a laser), so it won't hurt eyes. But nobody looks directly at the panel (you'll give yourself a headache, it's way too bright). Personally, I either close my eyes, or wear high quality eyewear that blocks light produced by the panel. The eyewear is designed for laser light, but it does just as well for LED light. If you hold a TES-1333 light meter behind any eyewear, it should read about 5 to 10 W/m2 (i.e. 95% block). 

**WARNING: if you hold any eyewear in front of a light meter such as the TES-1333, and the light level is not dramatically reduced (to less than 10% of original), DO NOT use that eyewear. Instead, just close your eyes.**

The reason? Infrared light is invisible, and cheap eyewear could let this through. And even if you use eyewear, just close your eyes most of the time.

Testicles: avoid infrared light (810nm) on one's testicles. They are more sensitive. Personally, until there is more scientific consensus, I use an opaque codpiece (for lack of a better word).

### Check 10: The science behind it

3,000 studies on photobiomodulation, 200 randomized controlled trials, used by the Olympic Teams, big league sports and people with chronic health conditions. It's all on PubMed.

### Update

Please don't get the impression that red light therapy can cover up poor lifestyle choices. No amount of red light therapy will help you feel healthy (and happy) if the basics are holding you back:

- Avoid a poor diet
- Exercise
- Avoid the worst pollutants


### Another post

I did another post here a while ago:
https://www.reddit.com/r/Biohackers/comments/a1vdl7/best_full_body_redlight/

# Pull Requests

Spotted a way to improve this estimation? Pull requests welcome.
