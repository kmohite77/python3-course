# Script to generate a CSV of workspace details based on user inputs
# Prompting user for location & floor details
print("\nEnter location and floor details below:")
Country = input("Country Name: ")
State = input("State Name: ")
City = input("City Name: ")
Floor = int(input("Floor Number (e.g., 1, 2, 3): "))
TotalDesk_rows = int(input("Total number of rows of desks: "))
firstDesk_label = input("Label of the first desk in row (e.g., A, B, C): ")
lastDesk_label = input("Label of the last desk in row (e.g., A, B, C): ")
# Generate the filename based on location and floor information
filename = "desksList-{}-{}-{}-{}.csv".format(Country, State, City, Floor)
# Ensure that desk labels are entered in the correct alphabetical order
while lastDesk_label < firstDesk_label:
  print("Error: First desk label should be alphabetically before or equal to the last desk label.")
  firstDesk_label = input("Please enter the correct label of the first desk in row: ")
  lastDesk_label = input("Please enter the correct label of the last desk in row: ")
# Open the CSV file for writing desk data
with open(filename, "w") as csv_file_var:
  # Write the header row to the CSV file
  csv_file_var.write("Workspace ID,Workspace Name,Workspace Type,Capacity,Calendar Type,Calendar Service,Calendar Resource,Country/Region,State,City,Floor,Assets\n")
  # Generate desk names based on user inputs and write them to the CSV
  for desk_num in range(1, TotalDesk_rows + 1):
    # Loop through each desk label in the row
    for desk_char in range(ord(firstDesk_label), ord(lastDesk_label) + 1):
      # Construct the desk name (e.g., 01.001A)
      deskName_string = '0' + str(Floor) + "." + "{:03}".format(desk_num) + chr(desk_char)
      # Create the final CSV line for this desk
      final_deskName_string = (
        "" + "," + deskName_string + "," + "Desk" + "," + "0" + "," +
        "Zoom" + "," + "Zoom Calendar Service" + "," + deskName_string + "," +
        Country + "," + State + "," + City + "," + str(Floor) + ","
      )
      # Write the desk data to the CSV file
      csv_file_var.write(final_deskName_string + "\n")
# Confirmation message
print(f"Desk details have been successfully saved to {filename}.")
