ETL Project Guide

Hypothesis/Topic: Our group predicted that there would be a strong, negative correlation between COVID-19 case numbers, traffic, and air pollution in Ohio. We broke this data down on a county level within the state of Ohio.

SUMMARY

Traffic Data:

Data to be Extracted:  The number of car trips by county in 2019 and 2020.

Data Source: https://data.bts.gov/Research-and-Statistics/Trips-by-Distance/w96p-f2qv/data
Extraction (Transformation): Filters were applied on the website of the data source to show only the state of Ohio (to be broken down by county). Filters were also applied to show trips from 04/02/2019 to 07/07/2020. The data was then downloaded as a CSV and this was read into Pandas. From there, a dataframe was created. Two null columns, “unnamed 15,” and “unnamed 16,” were dropped from the dataset.

Load: A PostgresSQL database was created, and an engine connecting to this database was created in Pandas. The Dataframe was then loaded into a PostgresSQL table named “trips.”


COVID Data:

Data to be Extracted: Covid-19 data points for Ohio (on county level)

Data Source: Ohio Government website
https://www.coronavirus.ohio.gov

Extraction: The initial data was provided in Tableau on the Ohio Government website. We also performed scraping to extra particular “dashboard” data from the ohio.gov homepage. Pandas was used to scrape the dashboard.

Transformation: Once the data was pulled from the COVID-19 dashboard, it was transformed in Pandas into a table format.

Load: The table was then loaded into PgAdmin along with the other data collected as part of a relational database.

Population Data:

Data to be Extracted:  Population for each Ohio County

Data Source:  Wikipedia info page for Ohio Counties:
https://en.wikipedia.org/wiki/List_of_counties_in_Ohio

Extraction:  Since the data was provided in a table on the Wikipedia website, Pandas was used to extract the table.  After cleaning the table (described below), the table was saved as a CSV file for upload into the relational database.

Transformation (Cleaning):  The table extracted had several additional columns that were not needed so they were deleted (county seat, establishment date, origin, etc.)  Only the following rows were kept:  County Name, County Code, and Population.  County Code was originally named FIPS Code but it was changed to match other data sources.  The County Name field had ‘County’ after each county name and that was also removed to match other data sources.

Load:  The table was loaded into PgAdmin along with the other data collected as part of the relational database.

Air Quality Data:

Data to be Extracted: Air quality data in Ohio:
https://www.epa.gov/outdoor-air-quality-data/download-daily-data

Transformation: After downloading CSV files from AQI, were merged and then divided into a site table and a measurement table. Each CSV contained only one measurement (Pb, CO, NO2, Ozone, etc) along with excessive site info (site name, site id, site region, longitude, etc) and needed to be organized efficiently. Glob was used to gather the CSV names and then a For Loop was implemented to import the names and concatenate them together. After merging all the CSVs, tables were built by dropping certain columns for each table. After dataframes were created, SQLite database was initiated. A series of functions were then used. These would a) create a table in the SQLite file and then b) add the corresponding Pandas dataframe. After the functions were defined and run, this produced 7 tables. One of these tables contained information related to the site (site id, location, name, longitude-latitude, etc) and 6 tables for the various pollutants measured.

Load: The table was then loaded into PgAdmin along with the other data collected as part of a relational database.


These are the data sources that we worked with. Additionally, we have an ERD to help provide a visual aid that outlines our line of thinking.
