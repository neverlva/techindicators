# techindicators
Python functions to calculate technical indicators from stock price data using Numpy.

## Purpose

These Python functions calculate various technical indicators from price time series data of stocks or other securities. The price data must be supplied as Numpy arrays and the functions rely on Numpy for calculations.  The code was written for those who would rather use Numpy matrices and arrays rather than Pandas dataframes for calculations.

## List of functions

### sma

The sma function is the [simple moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages).  Two parameters are required: a Numpy array of prices, and the number of time periods for averaging.  The function returns the simple moving average as a numpy array.  Note that the length of the moving average will be shorter than the price series by N-1, where N is the period for averaging.

### ema

The ema function is the [exponential moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages).  Two parameters are required: a Numpy array of prices, and the number of time periods for averaging.  The function returns the simple moving average as a numpy array.  Note that the length of the moving average will be shorter than the price series by N-1, where N is the period for averaging.

### kama

The kama function is the [Kaufman adaptive moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average).  Four parameters are required: a Numpy array of prices, the number of periods for the efficiency ratio calculation, the number of periods for the fastest exponential moving average constant, and the number of periods for the slowest exponential moving average constant.  The time periods are adjustable, but Kaufman origibnally suggested time periods of 10, 2, and 30 for the efficiency ration, fastest EMA, and slowest EMA, respectively.  The kama function returns the average as a Numpy array whose length is shorter than the price array by N-1, where N is the number of periods used for the effciency ratio.

### atr

The atr function is [average true range](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_true_range_atr)  The function requires four parameters: an array of high prices, an array of low prices, and array of closing prices, and a time period for averaging.  The time period is adjustable, but 14 is typically used.  The average true range is returned as an array shorter than the price array by N-1, where N is the time period used for averaging.
