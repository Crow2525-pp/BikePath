# BikePath

This is a hobbie project that I'm using my DataCamp skills in python to ETL into a dataframe and perform analysis on.

Future State:
How cool would it be to see a map of melbourne and see a blink every time a bike went past a counter?
How many people are recorded at different areas and disappear from the next likely stop?  What are the possibilities for those people?  Stop at the shops?  Go an alterative or more dangerous/non-bike path route?

Code: Python
Start Date: Sep-21
Re-Start Date: Mar-22

Issues:
1. So... this data shows we have 7.63M rows of data. Some data is not consistent across all files.  So we might have incomplete files.  This is only one year too... Max speed doesn't look high enough at 15.92, min looks OK at 2.  Average is 20.99 which is OK.  Why...  Need to split up months/dates to look closer.  Can't have max less than average.
2. Need to zoom in on months to better see the data
3. Data needs cleaning up.  Some of the downloaded files aren't in zips or csvs.  They are missing an extension, which adds a layer of complexity.  Further, I can't add everything and then remove duplicates, because there might be genuine duplicate entries.
4. The extract and removal tool needs work.  Because unzipping takes some time, the routine keeps finding files that are zipping in progress.  These files are then deleted after they're extracted.  Technically this doesn't matter, but it'll throw up some false positive erorrs.

Control:
Version 0.1 - 12/03/22 - Added commentary around problems with data. 
