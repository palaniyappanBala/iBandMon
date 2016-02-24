#/usr/bin/python2

#  Copyright (c) 2016-2017 Palaniyappan Bala 
#
#
#  Author : Palaniyappan Bala
#
#

import yaml, time, datetime

try:
	import linux_metrics as lm
except:
	print "linux_metrics, package not found"
	print "pip install linux_metrics"
	return

class Config():
	def parse(self):
		try:
		  f = open('bandwidth.yaml', 'r')
		except IOError as e:
		  print "I/O error bandwidth.yaml"

		self.config = yaml.load(f)
		f.close()
		if (not str(self.config["interval"]).isdigit()):
			print "Interval must be a digit"
			return
		return self.config

if __name__ == '__main__':
	yml=Config().parse()
	tx=rx=0
	while True:
		tx,rx=lm.net_stat.rx_tx_bits(yml["interface"])
		time.sleep(yml["interval"])
		tx1,rx1=lm.net_stat.rx_tx_bits(yml["interface"])
	        dt=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print (("%19s TX : %10d bytes, RX : %10d bytes")%(dt, tx1-tx, rx1-rx))



