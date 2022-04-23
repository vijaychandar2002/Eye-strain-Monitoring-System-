## Inspiration
We can't avoid long screen exposure in this corona period because almost everything is online, but as a result, we experience unhealthy eye conditions such as watering eyes, difficulty focusing, and so on. To address this issue, we created a project that will track your exposure and limit.

## What problems do looking at computer screens cause?
People who frequently look at computers (especially those who look at a computer for more than three hours per day) may experience symptoms such as:
- Eye ailment
- Migraines
- Scratchy eyes
- Watery or dry eyes
- Sensations of burning
- Color perception changes - Blurred vision
- Difficulty concentrating

## What it does
This application is set up to: - Monitor the duration of our blinks. In the event of under or over blinking, it sends an alert message and adjusts the screen brightness.
- Adjust the screen brightness and warm light strength based on the user's blink rate.
- To avoid eye strain, adjust the font size based on our distance from the screen.
- As doctors prescribe, send alerts to refocus after 20 minutes.
- It also warns the user if he comes within a certain distance of the monitor. (as prescribed by the doctors, 40 cm)
- Activate the night mode automatically based on the time zone.
 
## How we built it
We're using **computer vision** with opencv2 to find human faces in front of the computer and then tracking their movements with the **AI-Image detection** model. If the model detects that the user is stressing his eyes in any way, it alerts the user, and if the user continues to force his eyes, the model reduces the screen brightness and takes the necessary steps using **Windows service apis**. Furthermore, the programme is converted into a **Windows startup service**, which means that it runs whenever the user boots his or her computer.

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
