#Use the following in your input and print statements
"Enter a file: "
"\nError in file name: {}. Please try again."
"State"
"Max Year"
"Max"
"Min Year"
"Min"
"\nCrop: {}"


#Use these constants to format your output table
HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}" #state, max year, max value, min year, min value in this order
DATA_FORMAT = "{:<20s}{:>10s}{:>6d}{:>10s}{:>6d}"   #state, max year, max value, min year, min value in this order


STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def open_file():
    '''You fill in the doc string'''
    while True:
        file_name = input("Enter a file: ")
        try:
            fp = open(file_name, 'r')
            return fp
        except FileNotFoundError:
            print(f"Error in file name: {file_name}. Please try again.")
        
def read_file(fp):
    '''You fill in the doc string'''
    STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
              'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
              'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
              'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
              'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
              'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
              'Wisconsin', 'Wyoming']

    data = {}
    for line in fp:
        state, crop, _, variety, year, _, value = [x.strip() for x in line.split(',')]
        if state in STATES and variety == "All GE varieties" and value.isdigit():
            if crop not in data:
                data[crop] = {}
            if state not in data[crop]:
                data[crop][state] = {}
            data[crop][state][year] = int(value)

    fp.close()
    return data


def main():
    print("如果需要辅导或者答案的话 + vx lzyxlzyx2022")

if __name__ == "__main__":
    main()
