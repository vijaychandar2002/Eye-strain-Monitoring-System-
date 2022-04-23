# **iCare**
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Inspiration
In this corona period, with almost everything online we can't avoid long screen exposure but due to this we experience unhealthy eye conditions like watering of eyes, difficulty in focusing etc. To overcome this problem we developed a project that will monitor your limit and monitor your exposure.

## What problems do looking at computer screens cause?
People who look at computers frequently, (in particular those that look at a computer for more than three hours a day), may experience symptoms such as:
- Eye discomfort
- Headaches
- Itchy eyes
- Dry or watering eyes
- Burning sensations
- Changes in color perception
- Blurred vision
- Difficulty focusing

## What it does
This applications is programmed to :
- Monitor our blink duration. In case, of under and over blinking, it sends alert message and adjusts the brightness of screen. 
- Adjust the screen brightness and warm light strength according to blink rate of user.
- Adjust the font size according to our distance from screen to avoid strain on eyes.
- Send alerts to refocus after 20 mins as prescribed by doctors. 
- It also alerts the user if he exceeds a allowed proximity between monitor and user. (40 cm as prescribed by the doctors) 
- Automatically activate the night mode according to time zone.

 
## How we built it
We are using **computer vision** using opencv2 to find human faces in front of the computer and then monitoring their activity using **AI-Image detection** model. If the model finds that the user is stressing his eyes in any way, the model alerts the user and if the user is still forcing his eyes then the model reduces the screen brightness and takes necessary steps using **Windows service apis**. Further, the the program is converted into a **windows startup service** i.e. this program starts whenever the user boots his/her PC.

## Study sources
- http://www.nhs.uk/livewell/eyehealth/pages/eyesafety.aspx
- http://www.princeton.edu/uhs/healthy-living/hot-topics/ergonomics/
- http://www.une.edu.au/hrs/handbook/04/4.12.pdf
- http://staffcentral.brighton.ac.uk/.../doc002851.pdf
- http://www.wellness.uci.edu/toolkit/march/screenstrain.pdf
- http://www.nhs.uk/conditions/dry-eye-syndrome/Pages/Introduction.aspx
- http://publichealth.lacounty.gov/.../WorkStationSetUp_Jan2012.pdf
- http://news.bbc.co.uk/1/hi/health/7967381.stm
- www.ndt-ed.org/.../contrastsensitivity.htm
- http://news.bbc.co.uk/1/hi/england/bristol/4753833.stm


### How to run?
- Install the required python packages
```py 
pip install -r requirements.txt
```
- run the file 
```py 
python main.py
```
- if your pc has multiple camera's you can switch them by changing the index of Video Capture
```py
cap = cv2.VideoCapture(index)
# changed the index here (default set to =0)
```
