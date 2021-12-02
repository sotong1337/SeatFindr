import serial
from flask import Flask, request, render_template

class Table():
    def __init__(self, TableName):
        self._tableName = TableName
        self._display_clean = True
        self._clean = True
        self._presses = ""
        self._clear = "1121"

    def check_clean(self, buttonState, curr_task):
        #button pressed
        if buttonState == "1":
            print("here")
            self._display_clean = True

        if curr_task == "short_press":
            self._display_clean = self._clean
            self._presses += "1"
            
        elif curr_task == "long_press":
            self._display_clean = self._clean
            self._presses += "2"

        elif curr_task == "left_table":
            self._display_clean = False
            self._clean = False
            self._presses = ""

        if self._clear in self._presses:
            self._display_clean = True
            self._clean = True
            self._presses = ""
    
    def change_clean(self, new_status):
        self._display_clean = new_status
        self._clean = new_status

    def display_clean(self):
        if self._display_clean:
            return "Cleaned"
        return "Unclean"

Table1 = Table("Table1")
#Table2 = Table("Table2")
Table7 = Table("Table7")

#tables = [Table1, Table2]
#table_names = ["Table1", "Table2"]

tables = [Table1, Table7]
table_names = ["Table1", "Table7"]
        
app = Flask(__name__)
@app.route('/',  methods = ["GET", "POST"])
def home():
    global tables
    global table_names

    if request.method == "GET":
        try:
            ser = serial.Serial('COM3', 9600)
        
            arduino_output = ser.readline()         # read a byte string
            string_n = arduino_output.decode()  # decode byte string into Unicode  
            string = string_n.rstrip() # remove \n and \r

            lst = string.split(" ") #split output to specific elements
            table = tables[table_names.index(lst[0])]
            table.check_clean(lst[1], lst[2])
            print("string:")
            print(string)
            
            ser.close()

        except:
            pass

        t1 = Table1.display_clean()
        #t2 = Table2.display_clean()
        t7 = Table7.display_clean()

        #return render_template("index.html", t1 = t1, t2 = t2)
        return render_template("index.html", t1 = t1, t7 = t7)
    
    else:
        to_change = request.form.getlist("Tables")

        for i in to_change:
            table = tables[table_names.index(i)]
            table.change_clean(True)

        t1 = Table1.display_clean()
        #t2 = Table2.display_clean()
        t7 = Table7.display_clean()
        
        #return render_template("index.html", t1 = t1, t2 = t2)
        return render_template("index.html", t1 = t1, t7 = t7)

if __name__ == "__main__":
    app.run(debug = True)