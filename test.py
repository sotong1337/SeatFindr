import serial
from flask import Flask, request, render_template

class Table():
    def __init__(self, TableName, chairs_left):
        self._tableName = TableName
        self._chairs_left = chairs_left
        self._max_chairs = chairs_left
        self._display_clean = True
        self._clean = True
        self._presses = ""
        self._clear = "1121"

    def check_status(self, buttonState, curr_task):
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

    def change_chairs(self, add):
        if add:
            if (self._chairs_left < self._max_chairs):
                self._chairs_left += 1
        else:
            if (self._chairs_left > 0):
                self._chairs_left -= 1

    def display_status(self):
        #also returns seats
        if self._display_clean:
            return ("Cleaned", self._chairs_left, self._max_chairs)
        return ("Unclean", self._chairs_left, self._max_chairs)

class Chair(Table):
    def __init__(self, ChairName, ParentTable):
        self._chairName = ChairName
        self._parentTable = ParentTable
        self._occupied = False

    def check_status(self, buttonState, curr_task):
        if curr_task != "left_table":
            if buttonState == "1" and self._occupied == False:
                self._occupied = True
                self._parentTable.change_chairs(False)
            elif buttonState == "0" and self._occupied == True:
                if self._occupied == True:
                    self._occupied = False
                    self._parentTable.change_chairs(True)
    
    #only used for checking purposes
    def display_status(self):
        if (self._occupied == True):
            return "Occupied"
        else:
            return "Available"

Table7 = Table("Table7", 4)
Chair7_1 = Chair("Chair7_1", Table7)
Chair7_2 = Chair("Chair7_2", Table7)
Chair7_3 = Chair("Chair7_3", Table7)
Chair7_4 = Chair("Chair7_4", Table7)

tables = [Chair7_1, Chair7_2, Chair7_3, Chair7_4, Table7]
table_names = ["Chair7_1", "Chair7_2", "Chair7_3", "Chair7_4", "Table7"]
ser = 1

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    global ser
    ser = serial.Serial('COM9', 9600)

@app.route('/',  methods = ["GET", "POST"])
def home():

    global ser
    global tables
    global table_names

    if request.method == "GET":
        try:
        
            # ser_out= ser.readline()
            # arduino_output=[]
            # while ser_out != "":
            #     arduino_output.append(ser_out)
            # string_n=""
            # for i in arduino_output:
            #     string_n += i.decode()
            arduino_output = ser.readline()
            string_n = arduino_output.decode()
            string = string_n.rstrip()

            lst = string.split(" ") #split output to specific elements
            # tables stores the class object
            # table_names stor their names
            # lst is the arduino output. lst[0] contains name of table
            for i in range(0, len(lst)):
                try:
                    table = tables[table_names.index(lst[i])]
                    table.check_status(lst[i + 1], lst[i + 2])
                    print("string: ", end = "")
                    print(string)
                except:
                    pass
            #table = tables[table_names.index(lst[0])]
            #table.check_status(lst[1], lst[2])
            print("string: ", end = "")
            print(string)

        except:
            pass

        t7_status, c7_status, max_chairs = Table7.display_status()

        return render_template("index2.html", t7_status = t7_status, c7_status = c7_status, max_chairs = max_chairs)
    
    else:
        to_change = request.form.getlist("Tables")

        for i in to_change:
            table = tables[table_names.index(i)]
            table.change_clean(True)

        t7_status, c7_status, max_chairs = Table7.display_status()
        
        
        return render_template("index2.html", t7_status = t7_status, c7_status = c7_status, max_chairs = max_chairs)

if __name__ == "__main__":
    app.run(debug = True)