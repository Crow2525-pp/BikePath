# BikePath

This is a hobbie project that I'm using my DataCamp skills in python to ETL a VicRoads bike dataset into a Pandas dataframe and perform analysis on.  

Here is the Tableau Public draft: [Melbourne Bike Path Dashboard 2024 Data - Unfinished](https://public.tableau.com/app/profile/philip.patterson4951/viz/MelbourneBikePathDashboard2024Data-Unfinished/Dashboard1?publish=yes)

Future State:  
How cool would it be to see a map of melbourne and see a blink every time a bike went past a counter?
How many people are recorded at different areas and disappear from the next likely stop?  What are the possibilities for those people?  Stop at the shops?  Go an alterative or more dangerous/non-bike path route?

Code: Python  
Start Date: Sep-21  
Re-Start Date: Mar-22  
Re-Visit Date: Feb-24

Issues:  
1. So... this data shows we have 7.63M rows of data. Some data is not consistent across all files.  So we might have incomplete files.  This is only one year too... Max speed doesn't look high enough at 15.92, min looks OK at 2.  Average is 20.99 which is OK.  Why...  Need to split up months/dates to look closer.  Can't have max less than average.
2. Need to zoom in on months to better see the data
3. Data needs cleaning up.  Some of the downloaded files aren't in zips or csvs.  They are missing an extension, which adds a layer of complexity.  Further, I can't add everything and then remove duplicates, because there might be genuine duplicate entries.  When renaming these files, i'll need to add some try/except error catching to allow them to overwrite the existing file
4. The extract and removal tool needs work.  Because unzipping takes some time, the routine keeps finding files that are zipping in progress.  These files are then deleted after they're extracted.  Technically this doesn't matter, but it'll throw up some false positive erorrs.


Control:  
Version 0.1  
- 12/03/22 - Added commentary around problems with data.  
- 02/05/22 - Amended the directories where items are stored.  Zip folder for zips; extract folder for extracted zips;  I also added the 2022 url.  Also the extraction is working better now into they're own folders.  Next is cleaning up corrupt file extensions (e.g. filename.csv.123123 rather than filename.csv)
- 25/02/24 - Added Tableau Public viz to move away from pandas.  Setup Poetry Env and started proper sync to Github.
