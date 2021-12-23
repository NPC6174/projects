#
# Example file for parsing and processing JSON
#

import urllib.request
import json

def printResults(data):
# Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

# Now we can access the contents of the JSON like any other python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    print("--------------\n")

# Output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded in the past day")
    print("--------------\n")

# For each event print the place where it occurred
    print("All events and wehere they occurred in the past day:")
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("--------------\n")

# Print the events that only have a magnitude greater than 4
    print("All events with magnitude greater than or equal to 4.0 and where they occurred in the past day:")
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
    print("--------------\n")

# Print only the events where at least 1 person reported feeling something
    print("Events that were felt in the past day")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"], "felt", feltReports, "times")

def main():
# Define a variable to hold the source URL
# In this case we'll use the free data feed from the USGS
# This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    print("--------------\n")
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from the serve, cannot print results", webUrl.getcode())

if __name__ == "__main__":
    main()