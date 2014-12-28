#!/usr/bin/env python
#===============================================================
#VoiceForensics
#https://github.com/utkarshp/VoiceForensics
#===============================================================
#Copyright 2014 VoiceForensics
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import csv
import sys

filename = sys.argv[1]
openFileObject = open(filename,'r')
csvfile = csv.reader(openFileObject)
headerRow = True
for row in csvfile:
	rowString = ""
	commaedName = ""
	if headerRow:
		headerRow=False
		commaedName = row[0] + ',' + 'clipId'
	else:
		dashedName = row[0]
		dash = dashedName.find('-')
		commaedName = dashedName[:dash] + ',' + dashedName[dash+1:]
	rowString += commaedName + ','
	for x in xrange(1,len(row)-1):
		rowString += row[x] + ','
	rowString += row[-1]
	print rowString
		
