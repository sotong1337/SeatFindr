//#define Table1 2
//#define Table2 3
// note to self: grey table to 3, red to 2
//#define Chair7_4 A0
//#define Chair7_3 A1
//#define Chair7_2 A2
//#define Chair7_1 A3
//#define Table7 2

//#define Table4 3
//#define Table5 4
//#define Table6 5

#define Table2 A0
#define Chair2_1 A1
#define Chair2_2 A2

#define Table3 2
#define Chair3_1 3
#define Chair3_2 4

#define Table5 A3
#define Chair5_1 A4
#define Chair5_2 A5

#define Table9 5
#define Chair9_1 6
#define Chair9_2 7

#define Table10 8
#define Chair10_1 9
#define Chair10_2 10
#define Chair10_3 11

#define eatTime 10000 //300000
#define shortPress 500
#define resetTime 3000 //30000
String data = "";

class Table {
  private:
    String tableName;
    int pin;
    int buttonState = 0;
    int lastButtonState = 0;
    unsigned long long startPressed = 0;
    unsigned long long trueStartPressed = 0;
    unsigned long long endPressed = 0;
    unsigned long long holdTime = 0;
    unsigned long long trueHoldTime = 0;
    unsigned long long idleTime = 0;
    int required_pressure;
    bool cleaned = true;
    bool told = false;
    bool digital;
  public:
    Table(int pin, String tableName, bool digital, int required_pressure) {
      this->pin = pin;
      this->tableName = tableName;
      this->digital = digital;
      this->required_pressure = required_pressure;
      init();
    }
    
    void init() {
      pinMode(INPUT, INPUT_PULLUP);
      pinMode(INPUT, pin);
      updateState();
    }
    
    String updateState() {
      String output = "";
      if (digital) buttonState = digitalRead(pin);
      else {
        int sig = analogRead(pin);
        if (sig < required_pressure) buttonState = 1;
        else buttonState = 0;
      }
        
      if (buttonState != lastButtonState)output = process();

      else if (buttonState == 0 && not cleaned && not told) {
        if (millis() - endPressed >= resetTime) {
          output = tableName + " " + buttonState + " " + "left_table" + " " + cleaned + " ";
          told = true;
        };
      }
      lastButtonState = buttonState;
      return output;
    }

    String process() {
      String output = "";
      //when pressed
      if (buttonState == 1) {
        output = tableName + " " + buttonState + " " + "pressure_applied" + " " + cleaned + " ";
        trueStartPressed = millis();
        idleTime = trueStartPressed - endPressed;

        //person left and new person sat down (new press detected)
        if (idleTime >= resetTime) {
            //Serial.println(tableName + " " + buttonState + " " + "new_person" + " " + cleaned);
            //Serial.print("Idle Time: ");
            //Serial.println(idleTime / 1000);
            startPressed = trueStartPressed; 
        }
 
      // the button has been just released
      } else {
          endPressed = millis();
          
          trueHoldTime = endPressed - trueStartPressed;
          holdTime = endPressed - startPressed;
    
          if (trueHoldTime > 0 && trueHoldTime <= shortPress) {
              output = tableName + " " + buttonState + " " + "short_press" + " " + cleaned + " ";
              //Serial.print("TrueHold Time: ");
              //Serial.println(trueHoldTime / 1000);
          }
    
          else if (trueHoldTime > shortPress && trueHoldTime < eatTime) {
              output = tableName + " " + buttonState + " " + "long_press" + " " + cleaned + " ";
              //Serial.print("True Hold Time: ");
              //Serial.println(trueHoldTime / 1000);
          }
    
          if (holdTime >= eatTime) {
              cleaned = false;
              told = false;
              output = tableName + " " + buttonState + " " + "eating" + " " + cleaned + " ";
              //Serial.print("Hold Time: ");
              //Serial.println(holdTime / 1000);
          }
      }
      return output;
    }
    
    byte getState() {
      updateState();
      return buttonState;
    }
};

void setup() {
  Serial.begin(9600);
}

Table table2(Table2, "Table2", false, 480);
Table chair2_1(Chair2_1, "Chair2_1", false, 800);
Table chair2_2(Chair2_2, "Chair2_2", false, 750);

Table table3(Table3, "Table3", true, 0);
Table chair3_1(Chair3_1, "Chair3_1", true, 0);
Table chair3_2(Chair3_2, "Chair3_2", true, 0);

Table table5(Table5, "Table5", false, 800);
Table chair5_1(Chair5_1, "Chair5_1", false, 950);
Table chair5_2(Chair5_2, "Chair5_2", false, 0);

Table table9(Table9, "Table9", true, 0);
Table chair9_1(Chair9_1, "Chair9_1", true, 0);
Table chair9_2(Chair9_2, "Chair9_2", true, 0);

Table table10(Table10, "Table10", true, 0);
Table chair10_1(Chair10_1, "Chair10_1", true, 0);
Table chair10_2(Chair10_2, "Chair10_2", true, 0);
Table chair10_3(Chair10_3, "Chair10_3", true, 0);

void loop() {
  //data += chair7_1.updateState();
  //data += chair7_2.updateState();
  //data += chair7_3.updateState();
  //data += chair7_4.updateState();
  // //table2.updateState();
  //data += table7.updateState();
  //data += table6.updateState();
  //data += table5.updateState();
  //data += table4.updateState();
  
  data += table2.updateState();
  data += chair2_1.updateState();
  data += chair2_2.updateState();

  data += table3.updateState();
  data += chair3_1.updateState();
  data += chair3_2.updateState();

  data += table5.updateState();
  data += chair5_1.updateState();
  //data += chair5_2.updateState();

  data += table9.updateState();
  data += chair9_1.updateState();
  data += chair9_2.updateState();

  data += table10.updateState();
  data += chair10_1.updateState();
  data += chair10_2.updateState();
  data += chair10_3.updateState();
  if (data != "") {
    Serial.println(data);
    
  }
  
  data = "";
}
