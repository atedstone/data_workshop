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

site = 5

data_pts = pd.read_csv('EC%scal_4x.dat' %site, 
	 skiprows=[0,2,3], header=0, parse_dates=True, index_col='TIMESTAMP')
data_pts = data_pts.filter(like='EC(')

cal_pts = pd.read_excel('ec_calibration.xlsx', 
	sheet_name='fs%s' %site, names=['TIMESTAMP', 'ec_microsiemens'], header=None, 
	index_col='TIMESTAMP', parse_dates=True)

store = {}
for ix, row in cal_pts.iterrows():
	use_data = data_pts[ix:ix+dt.timedelta(seconds=50)]
	store[row.ec_microsiemens] = use_data.mean(axis=0)
	#print(use_data.describe())

df = pd.DataFrame.from_dict(store, orient='index')

# Highest points are suspect, drop them
df = df[df.index < 390]

store = {}
for sensor_name, data in df.iteritems():
	X = data
	y = data.index
	X = sm.add_constant(X)
	fit = sm.OLS(y, X).fit()
	print(fit.summary())

	plt.figure()
	plt.plot(data, data.index.values, marker='x', linestyle='none')
	plt.ylim(0, 500)
	plt.ylabel('EC (microsiemens)')
	plt.xlim(0,1)
	plt.xlabel('mV')

	m = fit.params[1]
	c = fit.params[0]

	xx = np.arange(0.3, 1, 0.1)
	yy = m * xx + c
	plt.plot(xx, yy, '--')

	plt.title('FS%s_%s $m=%.2f~c=%.2f$' %(site, sensor_name, m, c))
	plt.savefig('calibration_FS%s_%s.png' %(site, sensor_name))

	store[sensor_name] = dict(m=m, c=c, r2=fit.rsquared)


df_cal = pd.DataFrame.from_dict(store, orient='index')
df_cal.to_csv('calibration_coefficients_FS%s.csv' %site)

