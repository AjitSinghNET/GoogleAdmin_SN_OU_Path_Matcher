## The Script
A script that reads a list of serial numbers from an input file, searches for each serial number in a directory or data source, and outputs the corresponding Organizational Unit (OU) path for each serial number.

## Setup
1. Export the Google Admin Devices File and place it in the `Input` Folder. Update the `main.py` file with the input file name.
2. In the `input.csv`, add the data that needs to be updated with the its corresponding OU Path. Ensure that all data is in the correct column.
3. Execute the script using the command `py ./src/main.py` or however, you have setup your python environment depending on your Operating System (OS).
4. When the script executes, it should provide an updated csv file with the OU Path attached.
5. Before running the script again with another set of Input Data, delete the existing `output.csv` file.

For more support, contact me on email Ajit.Singh@.... or Teams.
