from is_leap_year import is_leap_year

origin_year = 1970

def day_to_year(days):
    year = origin_year

    while days > 365:
        if is_leap_year(year):
            # what about if leap year and days == 366
            if days > 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1

    return year

# # Changed this to upper case to satisfy pylint
# ORIGIN_YEAR = 1970

# def day_to_year(days):
#     year = ORIGIN_YEAR

#     while days > 0:
#         if is_leap_year(year):
#             days -= 366
#         else:
#             days -= 365
#         year += 1

#     return year - 1

