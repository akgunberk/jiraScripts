 #Berk Akgün - Risk Mitigation Metric - 17 September 2019, Tuesday
 
from jira import *      # import everything from jira module to access your issues and everything
import pandas as pd 	# pd is always for data science features
import os				#import os to describe the path you want to see your output


# output path is defined as /Desktop/Release-Ticket.xlsx
out_path = os.path.join(os.path.expanduser("~"), "Desktop", "Release-Ticket.xlsx")
# access to JIRA API
jira = JIRA('http://jira.esensi.local:8080/', basic_auth=('berk.akgun', 'Ubor2718+'))
# define the query you want to apply to get your issues in all
query = 'project = RT '
# apply the query just defined above, to see all issues set maxResults to 'None' and to see more field related to the issue set expand to 'changelog'
issues_in_proj = jira.search_issues(query, maxResults = None, expand='changelog')
# define an array to add all the issues which satisfies the is statement below
df = []
for issue in issues_in_proj:
	for history in issue.changelog.histories:
		for item in history.items:
			if item.field == 'status':
				summ = [issue.key,issue.fields.status.name,issue.fields.reporter,history.created,item.fromString,item.toString]
				df.append(summ)

# use the array above to define a pandas dataframe to write and export an excel file
df = pd.DataFrame(df)
writer = pd.ExcelWriter(out_path, engine = 'xlsxwriter') # show the execution path to pandas and define your writer engine for excel files.
df.to_excel(writer, sheet_name = 'RT') # Set the sheet name whatever u'd like 
writer.save()
writer.close()    # save everything that writer did and close it forever.

