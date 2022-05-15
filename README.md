# Clear-table
 For a tkkyia project <br>

# Problem Analysis
 Hawker centers are cool, with Singapore's hawker culture being a part of UNESCO cultural Intangible cultural heritage. <br>
 Cheap and tasty food, as well as a place for interaction are all part of its appeal. <br>
 However, during peak hours, seats are almost impossible to find, much less clean seats. <br>
 Futhermore, now that tray return is mandatory, many of the cleaners are stationed at the tray return point. <br>
 When this happens, they are unaware of which tables are uncleaned as they are no longer clearing the tables. <br>
 Sometimes, the tables look clean, but still have germs on it. <br>
 Yet, if cleaners were to go around to clean the tbales, the tray return point piles up with uncleaned dishes really quickly. <br>
 <img src = "img0.png">
 Thus, this project aims to create a system that is able to inform the patrons and cleaners which tables are occupied or are not yet cleaned. <br>

# Methodology
 How many people are at a seat <br>
 We know a chair is occupiued if there is pressure on the chair. <br>
 Thus, each chair will have a pressure sensor. <br>
 But that only tells us how many chairs are being sat on. <br>
 How do we know how many chairs are occupied for a single table? <br>
 By making the parent class (table) store a list its chairs, <br>
 and sending the data of which specific chair is being sat on. <br>
 What if someone is just putting something on it? i.e. Can we choose not to detect if someone is choping? <br>
 This is an option left for the hawker centers to decide. (because I personally think choping is fine) <br>
 This is why we use pressure sensors. <br>
 By using two pieces of low resistance metal, <br>
 When more weight is put on it, <br>
 The metals get in contact more and there will be less resistance. <br>
 Thus, we can can set a threshold for a minimum pressure to set off the sensor. <br>
 <br>
 Whether a table is clean: <br>
 A table is unclean after someone dines at that table. <br>
 We are able to know if someone is eating at the table if there is a pressure detected. <br>
 Thus, pressure sensors will be used on each table. <br>
 How do we know that the person is dining there and not just accidentally touched the table or is resting for a while? <br>
 Thus a "eating time" is defined. <br>
 If the pressure is detected for longer than 10 mins, we can be certain that the person is dining. <br>
 But what if the person lifts up his bowl to drink his soup? <br>
 Thus, a debounce time of 30s is added. <br>
 However, in our experience of dining, there is almost always a pressure on the table, so this is just for precaution. <br>
 <br>
 Another thing to consider is when a person immdiately sits down after another one is finished dining e.g. during peak period. <br>
 Do we need to consider this case? <br>
 Well, no. <br>
 In real life cases, usually a cleaner would not go to clear the table (even before the mandate) <br>
 <br>
 Now that we have defined when to change the table status to unclean, how do we know when to change the table status to clean? <br>
 There are two conditions when this happens: <br>
 1. When there is a person dining on the table. <br>
 - We know this occurs when there is a pressure on the table. <br>
 - Thus, if a pressure is detected, the table status would be changed to clean. <br>
 - Once the pressure is released, the table status would revert back to its previous status. <br>
 2. When a cleaner cleans the table. <br>
 - There is no reliable way to know when the table is cleaned. <br>
 - Thus, we need the cleaner to inform the program that the table is cleaned. <br>
 - This is done so in 2 ways: <br>
 2.1 Applying pressure on the table in a certain order e.g. short press, short press, long press, short press <br>
 - However, just in case the cleaner forgot to do that, <br>
 2.2 The cleaner may also directly select on the program the tables which are cleaned and submit the form. <br>

# Final Product
 The final product is a: <br>
 - Web app and mobile application with a layout of the coffee shop/ hawker center/ etc, <br>
 - that can detect how many people are at that table and <br>
 - when a person is finished eating, changing the table's status accordingly, <br>
 - and allow cleaners to inform it (the system) which tables are cleaned, and change the table status accordingly. <br>
 - With: <br>
   - Arduino (Uno) <br>
   - Pressure sensors (buttons & home-made pressure senors) <br>
   - HC-05 <br>
   - Wires, Resistors (10k ohms), a Breadboard <br>
 - as the hardware, <br>
 - using: <br>
   - Python flask <br>
   - Arduino IDE <br>
   - and Flutter (Dart) <br>
 - as the software. <br>
 <br>

# Notes:
 This only contain codes for the web app part. <br>
 Codes for the mobile app found here: https://github.com/LeeJingPeng/SeatFindr <br>
 Both uses the same logic <br>
 app2.py and table2.ino are the final ver, Although time values used are only for demo. <br>

# To do:
 Make circuit diagram for arduino