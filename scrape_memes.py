import re

import requests
from bs4 import BeautifulSoup

# def spider(maxpages):
# 	page = 1
# 	while page < maxpages:
url ='https://9gag.com/'
sourcecode = requests.get(url)

plaintext = sourcecode.text

##################################################################################tring to look for the regex (below) representing the image url ----- in the website code MATATA
#------------------------------------------------prev plan was to try storing it in a file to see whats diff
#------------------------------------------------prev plan is to download the 9gags html page code and store into  a file and try from there(same as above)


regex = r"\/gag\/[a-zA-Z0-9]+"

test_str = ("/gag/a6oNqm2\n"
	"/gag/anM5g85\n"
	"/gag/aeM5QxB\n"
	"/gag/aOr0x5N\n"
	"https://9gag.com/gag/a6oNqm2")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
