def next_15_leap_years(year):
    year_list = []
    for y in range(year, year + 100):
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            year_list.append(y)
            if len(year_list) == 15:
                return year_list


y_list = next_15_leap_years(2020)
for ye in y_list:
    print(ye)
