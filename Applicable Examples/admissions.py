import applicants as apps
import colleges as cols
"""
for x in apps.profiles.keys():
	apps.display_applicant(x)"""
"""
for x in apps.profiles.keys():
	apps.display_applicant(x)

for x in cols.college_list.keys():
	cols.display_college(x)"""

def match(app_id,school_id):
	for x in cols.college_list[school_id].properties():
		if apps.profiles[str(app_id)].x >= cols.college_list[str(school_id)].x:
			print "good"

match(2,2)