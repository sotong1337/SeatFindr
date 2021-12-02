# Clear-table
 For a tkkyia project

# Problem Analysis
 Now that tray return is mandatory, many of the cleaners are stationed at the tray return point. <br>
 When this happens, they are unaware of which tables are uncleaned as they are no longer clearing the tables. <br>
 Sometimes, the tables look clean, but still have germs on it. <br>
 Yet, if cleaners were to go around to clean the tbales, we experienced that the tray return point piles up with uncleaned dishes really quickly. <br>
 Thus, this project aims to create a system that is able to inform the cleaners which table are not yet cleaned. <br>

# Methodology
 A table is unclean after someone dines at that table. <br>
 We are able to know if someone is at the table if there is a pressure detected. <br>
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
 - Software with a layout of the coffee shop/ hawker center/ etc, <br>
 - that can detect when a person is finished eating, change the table status accordingly, <br>
 - and allow cleaners to inform it which tables are cleaned, and change the table status accordingly. <br>
 - With: <br>
   - Arduino (Leonardo) <br>
   - Pressure sensors (buttons) <br>
   - Wires, Resistors (10k ohms), a Breadboard <br>
   - And a computer <br>
 - as the hardware, <br>
 - using: <br>
   - Python flask <br>
   - and Arduino IDE <br>
 - as the software. <br>
 <br>
 Special thanks to my mum who works at a Ya Kun and came up with this problem <3