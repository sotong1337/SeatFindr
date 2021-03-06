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

# Table7 = Table("Table7", 4)
# Chair7_1 = Chair("Chair7_1", Table7)
# Chair7_2 = Chair("Chair7_2", Table7)
# Chair7_3 = Chair("Chair7_3", Table7)
# Chair7_4 = Chair("Chair7_4", Table7)

# tables = [Chair7_1, Chair7_2, Chair7_3, Chair7_4, Table7]
# table_names = ["Chair7_1", "Chair7_2", "Chair7_3", "Chair7_4", "Table7"]

Table1 = Table("Table1", 3)
Chair1_1 = Chair("Chair1_1", Table1)
Chair1_2 = Chair("Chair1_2", Table1)
Chair1_3 = Chair("Chair1_3", Table1)

Table2 = Table("Table2", 2)
Chair2_1 = Chair("Chair2_1", Table2)
Chair2_2 = Chair("Chair2_2", Table2)

Table3 = Table("Table3", 2)
Chair3_1 = Chair("Chair3_1", Table3)
Chair3_2 = Chair("Chair3_2", Table3)

Table4 = Table("Table4", 3)
Chair4_1 = Chair("Chair4_1", Table4)
Chair4_2 = Chair("Chair4_2", Table4)
Chair4_3 = Chair("Chair4_3", Table4)

Table5 = Table("Table5", 2)
Chair5_1 = Chair("Chair5_1", Table5)
Chair5_2 = Chair("Chair5_2", Table5)

Table6 = Table("Table6", 2)
Chair6_1 = Chair("Chair6_1", Table6)
Chair6_2 = Chair("Chair6_2", Table6)

Table7 = Table("Table7", 3)
Chair7_1 = Chair("Chair7_1", Table7)
Chair7_2 = Chair("Chair7_2", Table7)
Chair7_3 = Chair("Chair7_3", Table7)

Table8 = Table("Table8", 2)
Chair8_1 = Chair("Chair8_1", Table8)
Chair8_2 = Chair("Chair8_2", Table8)

Table9 = Table("Table9", 2)
Chair9_1 = Chair("Chair9_1", Table9)
Chair9_2 = Chair("Chair9_2", Table9)

Table10 = Table("Table10", 3)
Chair10_1 = Chair("Chair10_1", Table10)
Chair10_2 = Chair("Chair10_2", Table10)
Chair10_3 = Chair("Chair10_3", Table10)

tables = [Table1, Chair1_1, Chair1_2, Chair1_3,\
Table2, Chair2_1, Chair2_2, \
Table3, Chair3_1, Chair3_2, \
Table4, Chair4_1, Chair4_2, Chair4_3, \
Table5, Chair5_1, Chair5_2, \
Table6, Chair6_1, Chair6_2, \
Table7, Chair7_1, Chair7_2, Chair7_3, \
Table8, Chair8_1, Chair8_2, \
Table9, Chair9_1, Chair9_2, \
Table10, Chair10_1, Chair10_2, Chair10_3]

table_names = ["Table1", "Chair1_1", "Chair1_2", "Chair1_3",\
"Table2", "Chair2_1", "Chair2_2", \
"Table3", "Chair3_1", "Chair3_2", \
"Table4", "Chair4_1", "Chair4_2", "Chair4_3", \
"Table5", "Chair5_1", "Chair5_2", \
"Table6", "Chair6_1", "Chair6_2", \
"Table7", "Chair7_1", "Chair7_2", "Chair7_3", \
"Table8", "Chair8_1", "Chair8_2", \
"Table9", "Chair9_1", "Chair9_2", \
"Table10", "Chair10_1", "Chair10_2", "Chair10_3"]

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
        
        #t1_status, c1_status, max_chairs1 = Table1.display_status()
        t2_status, c2_status, max_chairs2 = Table2.display_status()
        t3_status, c3_status, max_chairs3 = Table3.display_status()
        #t4_status, c4_status, max_chairs4 = Table4.display_status()
        t5_status, c5_status, max_chairs5 = Table5.display_status()
        #t6_status, c6_status, max_chairs6 = Table6.display_status()
        #t7_status, c7_status, max_chairs7 = Table7.display_status()
        #t8_status, c8_status, max_chairs8 = Table8.display_status()
        t9_status, c9_status, max_chairs9 = Table9.display_status()
        t10_status, c10_status, max_chairs10 = Table10.display_status()

        return render_template("index2.html", t3_status = t3_status, c3_status = c3_status, max_chairs3 = max_chairs3, \
            t2_status = t2_status, c2_status = c2_status, max_chairs2 = max_chairs2, \
            t5_status = t5_status, c5_status = c5_status, max_chairs5 = max_chairs5, \
            t9_status = t9_status, c9_status = c9_status, max_chairs9 = max_chairs9, \
            t10_status = t10_status, c10_status = c10_status, max_chairs10 = max_chairs10)
    
    else:
        to_change = request.form.getlist("Tables")

        for i in to_change:
            table = tables[table_names.index(i)]
            table.change_clean(True)

        t2_status, c2_status, max_chairs2 = Table2.display_status()
        t3_status, c3_status, max_chairs3 = Table3.display_status()
        t5_status, c5_status, max_chairs5 = Table5.display_status()
        t9_status, c9_status, max_chairs9 = Table9.display_status()
        t10_status, c10_status, max_chairs10 = Table10.display_status()

        return render_template("index2.html", t3_status = t3_status, c3_status = c3_status, max_chairs3 = max_chairs3, \
            t2_status = t2_status, c2_status = c2_status, max_chairs2 = max_chairs2, \
            t5_status = t5_status, c5_status = c5_status, max_chairs5 = max_chairs5, \
            t9_status = t9_status, c9_status = c9_status, max_chairs9 = max_chairs9, \
            t10_status = t10_status, c10_status = c10_status, max_chairs10 = max_chairs10)

if __name__ == "__main__":
    app.run(debug = True)