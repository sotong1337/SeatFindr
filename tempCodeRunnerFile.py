app = Flask(__name__)
# @app.route('/',  methods = ["GET", "POST"])
# def home():

#     global tables
#     global table_names

#     if request.method == "GET":
#         try:
#             ser = serial.Serial('COM9', 9600)
        
#             # ser_out= ser.readline()
#             # arduino_output=[]
#             # while ser_out != "":
#             #     arduino_output.append(ser_out)
#             # string_n=""
#             # for i in arduino_output:
#             #     string_n += i.decode()
#             arduino_output = ser.readline()
#             string_n = arduino_output.decode()
#             string = string_n.rstrip()

#             lst = string.split(" ") #split output to specific elements
#             # tables stores the class object
#             # table_names stor their names
#             # lst is the arduino output. lst[0] contains name of table
#             for i in range(0, len(lst)):
#                 try:
#                     table = tables[table_names.index(lst[i])]
#                     table.check_status(lst[i + 1], lst[i + 2])
#                     print("string: ", end = "")
#                     print(string)
#                 except:
#                     pass
#             #table = tables[table_names.index(lst[0])]
#             #table.check_status(lst[1], lst[2])
#             print("string: ", end = "")
#             print(string)

#             ser.close()

#         except:
#             pass

#         t7_status, c7_status, max_chairs = Table7.display_status()

#         return render_template("index2.html", t7_status = t7_status, c7_status = c7_status, max_chairs = max_chairs)
    
#     else:
#         to_change = request.form.getlist("Tables")

#         for i in to_change:
#             table = tables[table_names.index(i)]
#             table.change_clean(True)

#         t7_status, c7_status, max_chairs = Table7.display_status()
        
        
#         return render_template("index2.html", t7_status = t7_status, c7_status = c7_status, max_chairs = max_chairs)

# if __name__ == "__main__":
#     app.run(debug = True)