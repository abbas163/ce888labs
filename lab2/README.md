In this Lab-2, First we have created a vehicles.py file in Pycharm, then we readed the vehicle.csv file to Create and save scatterplots and histograms for the current fleet and the proposed fleet (New_Fleet) as shown below:

![logo](./scaterplot.png?raw=true)

![logo](./current_fleet_histogram.png?raw=true)

![logo](./New_Fleet_Histogram.png?raw=true)


Then, We have used the bootstrap.py to create a function bootstrap on salaries.csv dataset for calculating bootstrap confidence  while using percentile function on Numpy i.e Mean, Lower and Upper as shown below

![logo](./bootstrap_confidence.png?raw=true)

After that, we have created the new file called bootstrap_vechicles.py to create a function bootstrap on vechicles.csv for comparison algorithm that requires the upper and lower bounds for the mean in order to say which fleet is better.i.e Current or New Fleet

Current Fleet:
(20.141535341365465, 19.353413654618475, 20.935843373493974)
New Fleet
(30.48787215189873, 29.151898734177216, 31.848101265822784)

As per the given result New Fleet data is much better then Current Fleet.