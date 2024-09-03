#location & floor details Entered by user
print("\nEnter details below:")
Country = input("Country Name :")
State = input("State Name :")
City = input("City Name :")
Floor = int(input("Floor Number (ex-1,2,3):"))
TotalDesk_rows = int(input("Total rows of desks :"))
firstDesk_label = input("Label of first desk in row (ex-A,B,C):")
lastDesk_label = input("Label of last desk in row (ex-A,B,C):")

filename = "desksList-{}-{}-{}-{}.csv".format(Country,State,City,Floor)


if(lastDesk_label<firstDesk_label):
    print("Labels are not in correct order. First label should be lower than last label. Please enter again")
    firstDesk_label = input("Label of first desk in row (ex-A,B,C):")
    lastDesk_label = input("Label of last desk in row (ex-A,B,C):")

#csv_file_var_w = open ("desksList.csv", "w")
csv_file_var = open (filename,"w")
csv_file_var.write("Workspace ID" + "," + "Workspace Name" + "," + "Workspace Type" + "," + "Capacity" + "," + "Calendar Type" + "," + "Calendar Service" + "," + "Calendar Resource" + "," + "Country/Region" + "," + "State" + "," + "City" + "," + "Floor" + "," + "Assets"+"\n")

## Create desk names and write to file above

for desk_num in range (1,TotalDesk_rows+1):
    #print(desk_num)    
    for desk_char in range(ord(firstDesk_label),ord(lastDesk_label)+1) :       
        deskName_string = '0'+ str(Floor) +"."+ "{:03}".format(desk_num)+chr(desk_char)

        ##  writing to csv file format : Workspace ID , Workspace Name, Worksapce Type, Capacity, Calendar Type, Cakendar Servc=ice, Calendar Resource, Country/Region, State, City, Floor, Assets
        final_deskName_string = "" + ","+ deskName_string + "," + "Desk" + "," + "0"+ "," + "Zoom" + "," + "Zoom Calendar Service" + "," + deskName_string + "," + Country + "," + State + "," + City + "," + str(Floor) + "," + ""
        #print(final_deskName_string)
        
        csv_file_var.write(final_deskName_string+"\n")

csv_file_var.close()

#csv_file_var = open(csv_file_var,"r")
#print(csv_file_var.read()) 




