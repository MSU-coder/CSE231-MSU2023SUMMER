
#Use the following strings in your prompts and print statements
"\nError. Please try again"
"Enter a file name: "
"\n\nGross Domestic Product"

#Use these contansts when displaying the results
HEADER_FORMAT = "{:<10s}{:>8s}{:>6s}{:>18s}"
DATA_FORMAT = "{:<10s}{:>8.1f}{:>6d}{:>18.2f}"

def open_file():
    ''' Docstring'''
    while True:
        file_name = input("Enter a file name: ")
        try:
            fp = open(file_name, "r")
            return fp
        except FileNotFoundError:
            print("Error. Please try again")
    
def find_min_percent(line):
    ''' Docstring'''

    min_value = float(line[76:76 + 12].strip())
    min_index = 0
    for i in range(47):
        start = 76 + i * 12
        end = start + 12
        value = float(line[start:end].strip())
        if value < min_value:
            min_value = value
            min_index = i
    return min_value, min_index

def find_max_percent(line):
    ''' Docstring'''

    max_value = float(line[76:76 + 12].strip())
    max_index = 0
    for i in range(47):
        start = 76 + i * 12
        end = start + 12
        value = float(line[start:end].strip())
        if value > max_value:
            max_value = value
            max_index = i
    return max_value, max_index

def find_gdp(line, index):
    ''' Docstring'''

    start = 76 + index * 12
    end = start + 12
    return float(line[start:end].strip()) / 1000


def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    ''' Docstring'''

    print("")
    print("Gross Domestic Product")
    print("{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max", "change", "year", "GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", min_val, min_year, min_val_gdp))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max", max_val, max_year, max_val_gdp))


def main():
    fp = open_file()
    lines = fp.readlines()
    line_9 = lines[9 - 1]
    line_44 = lines[44 - 1]
    start_year = 1969
    min_val, min_index = find_min_percent(line_9)
    min_year = start_year + min_index
    min_val_gdp = find_gdp(line_44, min_index)
    max_val, max_index = find_max_percent(line_9)
    max_year = start_year + max_index
    max_val_gdp = find_gdp(line_44, max_index)
    display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp)

if __name__ == "__main__":
    main()
