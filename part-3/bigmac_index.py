#!/usr/bin/env python3
# Youssef Chahine
# CPSC 223p-03
# 2020-10-27
# ykchahine@csu.fullerton.edu
#
"""A program that prints a series of plots that
   uses data from each country's CSV files relating to the BIG MAC INDEX"""
import sys
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def series_plots():
    """Gets a series of plots that makes a bar for each country
       based on how many hours it takes to purchase
       4 Big Macs in terms of U.S dollars for a minumum wage worker"""
    temp_list = simple_plot()
    my_list = temp_list[0]
    country = temp_list[2]
    min_wage = temp_list[3]
    dollar_year = []
    wage_per_hr = []
    total_earned_hrly = []
    wage_index = 0
    for country_name in country:
        index = 0
        count = 0
        for date in my_list[country_name][0]:
            if date.year == 2017:
                count += 1
            elif date.year != 2017 and count == 2:
                dollar_year.append(my_list[country_name][3][index - 2])
                count = 0
            index += 1
    for i in dollar_year:
        value = i*4
        wage_per_hr.append(int(value // min_wage[wage_index]))
        wage_index += 1
    total_index = 0
    for wage in wage_per_hr:
        total_earned_hrly.append(wage*min_wage[total_index])
        total_index += 1
    fig, axis = plt.subplots(figsize=(7, 7), constrained_layout=True)
    y_pos = np.arange(len(country))
    plt.bar(y_pos, wage_per_hr, align='center', alpha=0.5, color='r')
    plt.xticks(y_pos, country)
    for i, _v_ in enumerate(wage_per_hr):
        plt.text(y_pos[i]-0.1, _v_+0.1, str(_v_), fontsize=19)
    plt.ylabel('Hours Worked', fontsize=16)
    plt.suptitle('Hours Worked for 4 Big Macs', fontsize=24)
    fig.savefig("hours_worked_to_feed_a_family.png")
    plt.close()


def scatter_plot():
    """A scatter plot that labels each country's GDP adjusted values"""
    temp_list = simple_plot()
    scatter_list = temp_list[0]
    zero = temp_list[1]
    fig, axis = plt.subplots(figsize=(8, 10), constrained_layout=True)
    plt.suptitle('Hours Worked for 4 Big Macs', fontsize=24)
    axis.scatter(scatter_list["CAN"][6], scatter_list["CAN"][0], color='blue',
                 label='CAN_dollar_adj_valuation')
    axis.scatter(scatter_list["NZL"][6], scatter_list["NZL"][0],
                 color='yellow', label='NZL_dollar_adj_valuation')
    axis.scatter(scatter_list["MEX"][6], scatter_list["MEX"][0], color='green',
                 label='MEX_dollar_adj_valuation')
    axis.scatter(scatter_list["DEU"][6], scatter_list["DEU"][0], color='red',
                 label='DEU_dollar_adj_valuation')
    axis.scatter(scatter_list["JPN"][6], scatter_list["JPN"][0],
                 color='fuchsia', label='JPN_dollar_adj_valuation')
    axis.plot(zero, scatter_list["USA"][0], color='black',
              label='US Dollar', dashes=[4, 3])
    axis.set(xlabel="Percentages", ylabel="Dates")
    axis.legend(loc=4)
    fig.savefig("big_mac_index_scatter.png")
    plt.close()


def simple_plot():
    """A function that takes in the JSON file
      and plots the lines using the datetime and matplotlib module"""
    first = 0
    country = []
    min_wage = []
    with open(sys.argv[1]) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if first != 0:
                country.append(row[0])
                min_wage.append(float(row[1]))
            else:
                first += 1
    my_list = {"CAN": [], "USA": [],
               "NZL":  [], "JPN": [], "DEU": [], "CHN": []}
    for country_name in country:
        dates_list = []
        local_price = []
        dollar_ex = []
        dollar_price = []
        dollar_ex = []
        dollar_ppp = []
        dollar_valuation = []
        dollar_adj_valuation = []
        zero = []
        first = 0
        file = "ECONOMIST-BIGMAC_{}.csv".format(country_name)
        with open(file) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if first != 0:
                    dates_list.append(row[0])
                    local_price.append(float(row[1]))
                    dollar_ex.append(float(row[2]))
                    dollar_price.append(float(row[3]))
                    dollar_ppp.append(float(row[4]))
                    dollar_valuation.append(float(row[5]))
                    if row[6] != '':
                        dollar_adj_valuation.append(float(row[6]))
                    else:
                        dollar_adj_valuation.append(float("0"))
                    zero.append(0)
                else:
                    first += 1

        dates_list = [datetime.strptime(_d_, "%Y-%m-%d") for _d_ in dates_list]
        my_list[country_name] = [dates_list, local_price, dollar_ex,
                                 dollar_price, dollar_ppp, dollar_valuation,
                                 dollar_adj_valuation]
    fig, axis = plt.subplots(figsize=(8, 10), constrained_layout=True)
    axis.set(title="Big Mac Index Valuation")
    axis.plot(my_list["CAN"][0], my_list["CAN"][6], color='blue',
              label='CAN_dollar_adj_valuation')
    axis.plot(my_list["CAN"][0], my_list["CAN"][5], color='skyblue',
              dashes=[4, 3], label='CAN_dollar_valuation')
    axis.plot(my_list["NZL"][0], my_list["NZL"][6], color='yellow',
              label='NZL_dollar_adj_valuation')
    axis.plot(my_list["NZL"][0], my_list["NZL"][5], color='yellow',
              dashes=[4, 3], label='NZL_dollar_valuation')
    axis.plot(my_list["MEX"][0], my_list["MEX"][6], color='green',
              label='MEX_dollar_adj_valuation')
    axis.plot(my_list["MEX"][0], my_list["MEX"][5], color='limegreen',
              dashes=[4, 3], label='MEX_dollar_valuation')
    axis.plot(my_list["DEU"][0], my_list["DEU"][6], color='red',
              label='DEU_dollar_adj_valuation')
    axis.plot(my_list["DEU"][0], my_list["DEU"][5], color='lightcoral',
              dashes=[4, 3], label='DEU_dollar_valuation')
    axis.plot(my_list["JPN"][0], my_list["JPN"][6], color='fuchsia',
              label='JPN_dollar_adj_valuation')
    axis.plot(my_list["JPN"][0], my_list["JPN"][5], color='magenta',
              dashes=[4, 3], label='JPN_dollar_valuation')
    axis.plot(my_list["USA"][0], zero, color='black', label='US Data')
    axis.set(xlabel="Dates", ylabel="Percentages")
    axis.legend(loc=2)
    fig.savefig("bigmac_index.png")
    plt.close()
    return (my_list, zero, country, min_wage)


def main():
    """Calls each plot"""
    print("Writing plot to big_mac_index_valuation.png")
    simple_plot()
    print("Writing plot to big_mac_index_scatter.png")
    scatter_plot()
    print("Writing plots to hours_worked_to_feed_a_family.png")
    series_plots()


if __name__ == "__main__":
    main()
