from jira import *
import pandas as pd
import os

out_path = os.path.join(os.path.expanduser("~"), "Desktop", "Release-Ticket.xlsx")

jira = JIRA('http://jira.esensi.local:8080/', basic_auth=('berk.akgun', 'password'))

query = 'project = RT '

issues_in_proj = jira.search_issues(query,maxResults = None,expand='changelog')

df = []
for issue in issues_in_proj:
	for history in issue.changelog.histories:
		for item in history.items:
			if item.field == 'status':
				summ = [issue.key,issue.fields.status.name,issue.fields.reporter,history.created,item.fromString,item.toString]
				df.append(summ)


df = pd.DataFrame(df)
writer = pd.ExcelWriter(out_path, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'RT')
writer.save()
writer.close()

