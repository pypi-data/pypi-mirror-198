## IPC Calculator
## Description: Package to calculate how inflation affects the value of money, 
## taking into account the change from pesetas to euros if necessary.
## Author: @scuellaralmagro
## Date: March 2023

import time
from functools import reduce

# Constants

EXCHANGE_RATE = 166.386
IPC_TABLE = {'1962': 9.9,
             '1963': 5.5,
             '1964': 12.7,
             '1965': 9.4,
             '1966': 5.3,
             '1967': 6.6,
             '1968': 2.9,
             '1969': 3.4,
             '1970': 6.8,
             '1971': 9.6,
             '1972': 7.3,
             '1973': 14.2,
             '1974': 17.9,
             '1975': 14.1,
             '1976': 19.8,
             '1977': 26.4,
             '1978': 16.5,
             '1979': 15.6,
             '1980': 15.2,
             '1981': 14.4,
             '1982': 14.0,
             '1983': 12.2,
             '1984': 9.0,
             '1985': 8.2,
             '1986': 8.3,
             '1987': 4.6,
             '1988': 5.8,
             '1989': 6.9,
             '1990': 6.5,
             '1991': 5.5,
             '1992': 5.3,
             '1993': 4.9,
             '1994': 4.3,
             '1995': 4.3,
             '1996': 3.2,
             '1997': 2.0,
             '1998': 1.4,
             '1999': 2.9,
             '2000': 4.0,
             '2001': 2.7,
             '2002': 4.0,
             '2003': 2.6,
             '2004': 3.2,
             '2005': 3.7,
             '2006': 2.7,
             '2007': 4.2,
             '2008': 1.4,
             '2009': 0.8,
             '2010': 3.0,
             '2011': 2.4,
             '2012': 2.9,
             '2013': 0.3,
             '2014': -1.0,
             '2015': 0.0,
             '2016': 1.6,
             '2017': 1.1,
             '2018': 1.2,
             '2019': 0.8,
             '2020': -0.5,
             '2021': 6.5,
             '2022': 5.7}

# Functions

def convert_to_euros(amount_pts):
    """Converts a pesetas amount to euros"""
    return amount_pts / EXCHANGE_RATE

def convert_to_pesetas(amount_euros):
    """Converts an euros amount to pesetas"""
    return amount_euros * EXCHANGE_RATE

def inflation_adjustment(start_year: int, end_year: int, amount: float, start_currency: str) -> float:
    """
    Adjusts a given amount of money for inflation between two years and returns the result as a float
    in the currency of the end year with parity value.

    Args:
        start_year (int): The year in which the amount was earned or acquired.
        end_year (int): The year in which the amount should be adjusted for inflation.
        amount (float): The amount of money to be adjusted for inflation.
        start_currency (str): The currency of the amount, which must be either "pesetas", "euros", "peseta", "euro", "pts", or "€".

    Raises:
        ValueError: If the end year is greater than the current year, the start year is not found in the IPC table,
                    the end year is not found in the IPC table, the start currency is not supported, the start year is greater than the end year,
                    or the amount is negative.

    Returns:
        float: The adjusted amount of money as a float in the currency of the end year with parity value, rounded to two decimal places.
    """
    
    # Error handling
    if end_year > time.localtime().tm_year:
        raise ValueError(f"End year {end_year} is greater than current year {time.localtime().tm_year}.")
    if str(start_year) not in IPC_TABLE:
        raise ValueError(f"Start year {start_year} not found in IPC table")
    if str(end_year) not in IPC_TABLE:
        raise ValueError(f"End year {end_year} not found in IPC table")
    if start_currency not in ['pesetas', 'euros', 'peseta', 'euro', 'pts', '€']:
        raise ValueError(f"start_currency {start_currency} not supported")
    if start_year > end_year:
        raise ValueError(f"Start year {start_year} is greater than end year {end_year}.")
    if amount < 0:
        raise ValueError(f"Amount {amount} is negative")
    if amount == 0:
        return 0.0
    
    # Calculate accumulated inflation rate
    inflation_list = []
    for year in range(start_year, end_year):
        inflation_list.append(IPC_TABLE[str(year)] / 100 + 1)               # Find inflation rate for each year and add 1 to convert to factor
    overall_inflation_factor = reduce(lambda x, y: x * y, inflation_list)   # Multiply all factors to get overall inflation factor.
    overall_inflation_rate = (overall_inflation_factor - 1) * 100           # Subtract 1 to get inflation rate and convert to percentage

    # Calculate final amount
    final_amount = amount * overall_inflation_rate / 100 + amount

    # Converto to euros if necessary
    if start_currency in ['pesetas', 'peseta', 'pts'] and end_year > 2002:
        final_amount = convert_to_euros(final_amount)

    return round(final_amount, 2)