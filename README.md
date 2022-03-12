# BikePath

This is a hobbie project that I'm using my DataCamp skills in python to ETL into a dataframe and perform analysis on.

Future State:
How cool would it be to see a map of melbourne and see a blink every time a bike went past a counter?
How many people are recorded at different areas and disappear from the next likely stop?  What are the possibilities for those people?  Stop at the shops?  Go an alterative or more dangerous/non-bike path route?

Code: Python
Start Date: Sep-21
Re-Start Date: Mar-22

Issues:
1. So... this data shows we have 7.63M rows of data. Some data is not consistent across all files.  So we might have incomplete files.  This is only one year too... Max speed doesn't look high enough at 15.92.  Average is 20.99 which is OK.   Speed looks OK - Average speed is 20.99213, but min is 2, Max is 15.92.  Why...  Need to split up months/dates
2. Need to zoom in on months to better see the data
3. Data needs cleaning up.  Some of the downloaded files aren't in zips or csvs.  They are missing an extension, which adds a layer of complexity.  Further, I can't add everything and then remove duplicates, because there might be genuine duplicate entries.

Control:
Version 0.1 - 12/03/22 - Added commentary around problems with data. 
