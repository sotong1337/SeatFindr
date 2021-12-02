//#define Table1 2
//#define Table2 3
// note to self: grey table to 3, red to 2
#define Table1 3
#define Table7 2

#define eatTime 10000 //300000
#define shortPress 500
#define resetTime 3000 //30000

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
    bool cleaned = true;
    bool told = false;
  public:
    Table(int pin, String tableName) {
      this->pin = pin;
      this->tableName = tableName;
      init();
    }
    void init() {
      pinMode(pin, INPUT);
      updateState();
    }
    
    void updateState() {
      buttonState = digitalRead(pin);
      
      if (buttonState != lastButtonState) {
        process();
      }

      else if (buttonState == LOW && not cleaned && not told) {
        if (millis() - endPressed >= resetTime) {
          Serial.println(tableName + " " + buttonState + " " + "left_table" + " " + cleaned);
          told = true;
        };
      }
      lastButtonState = buttonState;
    }

    void process() {
      //when pressed
      if (buttonState == HIGH) {
        Serial.println(tableName + " " + buttonState + " " + "pressure_appiled" + " " + cleaned);
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
    
          if (trueHoldTime > 100 && trueHoldTime <= shortPress) {
              Serial.println(tableName + " " + buttonState + " " + "short_press" + " " + cleaned);
              //Serial.print("TrueHold Time: ");
              //Serial.println(trueHoldTime / 1000);
          }
    
          else if (trueHoldTime > shortPress && trueHoldTime < eatTime) {
              Serial.println(tableName + " " + buttonState + " " + "long_press" + " " + cleaned);
              //Serial.print("True Hold Time: ");
              //Serial.println(trueHoldTime / 1000);
          }
    
          if (holdTime >= eatTime) {
              cleaned = false;
              told = false;
              Serial.println(tableName + " " + buttonState + " " + "eating" + " " + cleaned);
              //Serial.print("Hold Time: ");
              //Serial.println(holdTime / 1000);
          }
      }
    }
    
    byte getState() {
      updateState();
      return buttonState;
    }
};

Table table1(Table1, "Table1");
//Table table2(Table2, "Table2");
Table table7(Table7, "Table7");

void setup() {}

void loop() {
  table1.updateState();
  //table2.updateState();
  table7.updateState();
}
