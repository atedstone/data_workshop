"""
Run post-processing on electrical conductivity sensor calibrations.

Execute script once for each multiplexer (i.e. once per site).

Andrew Tedstone, February 2020

"""

import pandas as pd
import datetime as dt
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# This script is designed to work with several different locations or sites of data.
# Specify the one we are working with.
location = 5

# Load datalogger data for the location we are interested in
data_pts = pd.read_csv('EC%scal_4x.dat' %location, 
	 skiprows=[0,2,3], header=0, parse_dates=True, index_col='TIMESTAMP')
# Keep only the datalogger columns that contain EC data
data_pts = data_pts.filter(like='EC(')

# Read the calibration points from the relevant sheet in the excel file
cal_pts = pd.read_excel('ec_calibration.xlsx', 
	sheet_name='fs%s' %location, names=['TIMESTAMP', 'ec_microsiemens'], header=None, 
	index_col='TIMESTAMP', parse_dates=True)

# The millivolts calibration data were recorded by the logger once every 10 seconds for a
# minute. For each EC microsiemens calibration point we want to calculate the average of
# the data stored over that minute.
store = {}
for ix, row in cal_pts.iterrows():
	# Get a small dataframe of just the data for the minute
	use_data = data_pts[ix:ix+dt.timedelta(seconds=50)]
	# Calculate the average mV value for each sensor and save to store
	store[row.ec_microsiemens] = use_data.mean(axis=0)

# Now convert the dictionary to a data frame so that we can work with it more easily.
df = pd.DataFrame.from_dict(store, orient='index')

# Highest points are suspect, drop them
df = df[df.index < 390]


## We want to calculate the coefficients of linear regression between sensor milliVolts
# and what the actual EC for that milliVolt value is. We need to do this for each
# sensor (there are 16 in this example), so iteritems() allows us to treat one column at
# a time.
store = {}
for sensor_name, data in df.iteritems():

	# Do ordinary least squares regression using statsmodels
	X = data
	y = data.index
	X = sm.add_constant(X)
	fit = sm.OLS(y, X).fit()
	print(fit.summary())

	# Start plotting a figure. Add the mv vs EC values as Xs first.
	plt.figure()
	plt.plot(data, data.index.values, marker='x', linestyle='none')

	# Format the figure
	plt.ylim(0, 500)
	plt.ylabel('EC (microsiemens)')
	plt.xlim(0,1)
	plt.xlabel('mV')

	# Get the m and c parameters of y = m * x + c
	m = fit.params[1]
	c = fit.params[0]

	# Calculate the 'interpolated' values of the linear function
	xx = np.arange(0.3, 1, 0.1)
	yy = m * xx + c
	# Plot them
	plt.plot(xx, yy, '--')

	plt.title('FS%s_%s $m=%.2f~c=%.2f$' %(site, sensor_name, m, c))
	plt.savefig('calibration_FS%s_%s.png' %(site, sensor_name))

	store[sensor_name] = dict(m=m, c=c, r2=fit.rsquared)


df_cal = pd.DataFrame.from_dict(store, orient='index')
df_cal.to_csv('calibration_coefficients_FS%s.csv' %site)

