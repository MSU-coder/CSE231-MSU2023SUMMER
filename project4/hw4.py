import matplotlib.pyplot as plt

def open_file():
   while True:
       year = input("Enter a year where 1990 <= year <= 2023: ")
       if year.isdigit() and 1990 <= int(year) <= 2023:
           try:
               filename = f'year{year}.txt'
               fp = open(filename, 'r')
               return fp, int(year)
           except FileNotFoundError:
               print(f"Error in file name: '{filename}' Please try again.")
       else:
           print("Error in year. Please try again.")


def read_file(fp):
    data_list = []
    next(fp)
    next(fp)
    for line in fp:
        split_line = line.split()
        range_bottom = float(split_line[0].replace(',', ''))
        if split_line[2] == 'over':
            range_top = float('inf')
        else:
            range_top = float(split_line[2].replace(',', ''))
        cumulative_percentage = float(split_line[5])
        income = float(split_line[7].replace(',', ''))
        aggregate_amount = float(split_line[6].replace(',', ''))
        number_of_people = int(split_line[3].replace(',', ''))
        data_list.append((range_bottom, range_top, cumulative_percentage, income, aggregate_amount, number_of_people))
    return data_list


def find_average(data_list):
    total_income = sum([data[4] for data in data_list])
    total_people = sum([data[5] for data in data_list])
    return total_income / total_people

def find_median(data_list):
    for data in data_list:
        if data[2] >= 50:
            return data[3]

def get_range(data_list, percent):
    for data in data_list:
        if data[2] >= percent:
            return ((data[0], data[1]), data[2], data[3])

def get_percent(data_list, income):
    for data in data_list:
        if data[0] <= income <= data[1]:
            return ((data[0], data[1]), data[2])

def do_plot(x_vals, y_vals, year):
    plt.plot(x_vals[:40], y_vals[:40])
    plt.xlabel("Income")
    plt.ylabel("Cumulative Percentage")
    plt.title(f"Cumulative Percent for Income in {year}")
    plt.show()

def main():
   fp, year = open_file()
   data_list = read_file(fp)

   avg = find_average(data_list)
   med = find_median(data_list)

   print("Year   Mean            Median")
   print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year, avg, med))

   plot_choice = input("Do you want to plot values (yes/no)? ")
   if plot_choice.lower() == "yes":
       x_vals = [data[0] for data in data_list]
       y_vals = [data[2] for data in data_list]
       do_plot(x_vals, y_vals, year)

   while True:
       choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
       if not choice:
           break
       elif choice.lower() == "r":
           percent = float(input("Enter a percent: "))
           if 0 <= percent <= 100:
               result = get_range(data_list, percent)
               print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(result[1], result[2]))
           else:
               print("Error in percent. Please try again")
       elif choice.lower() == "p":
           income = float(input("Enter an income: "))
           if income >= 0:
               result = get_percent(data_list, income)
               print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(income, result[1]))
           else:
               print("Error: income must be positive")
       else:
           print("Error in selection.")


if __name__ == "__main__":
    main()