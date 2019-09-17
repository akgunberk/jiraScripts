 #import all modules needed
from jira import JIRA # to interact with jira
import pandas as pd   # to use dataframes
import os             # to save excel to Desktop 
from vincent.colors import brews

def get_jira(username,password):

    # JIRA('http://jira.esensi.local:8080/',basic_auth=('username','password'))
    
    jira = JIRA('http://jira.esensi.local:8080/',basic_auth=(username,password))

    # search issue with advanced query you used in JIRA
    query = 'project = RM'

    issues = jira.search_issues(query,maxResults = None)

    df = []

    # collect your metrics
    for issue in issues:
        if str(issue.fields.issuetype) == 'Threat':
            if (issue.fields.customfield_13508 != None):
                columns = [issue.key,issue.fields.status.name,issue.fields.reporter,issue.fields.customfield_13508.raw.get('value')]
            elif (issue.fields.customfield_13506 != None):
                columns = [issue.key,issue.fields.status.name,issue.fields.reporter,issue.fields.customfield_13506.raw.get('value')]
            else:
                columns = [issue.key,issue.fields.status.name,issue.fields.reporter,issue.fields.status.name]
                
            df.append(columns)

    df = pd.DataFrame(df,columns = ['Key','Status','Reporter','Risk_Status'])

    #print(df)


    out_path = os.path.join(os.path.expanduser("~"), "Desktop", "Risk-Mitigate-Performance.xlsx")

    writer = pd.ExcelWriter(out_path, engine = 'xlsxwriter')

    df.to_excel(writer, sheet_name = 'Risk_Mitigation')

    categories = df.Risk_Status.unique()

    #print(categories)

    percent = df.Risk_Status.value_counts()

    #print(percent)

    df2 = pd.DataFrame([percent], columns = categories).dropna(axis= 1, how = 'any')

    #print(df2)

    df2.to_excel(writer, sheet_name = 'Risk_Mitigation' ,startrow =3, startcol=8)


    # workbook = writer.book
    # worksheet = writer.sheets['Risk_Mitigation']

    # # Create a chart object.
    # chart = workbook.add_chart({'type': 'pie'})

    # # Configure the chart from the dataframe data. Configuring the segment
    # # colours is optional. Without the 'points' option you will get Excel's
    # # default colours.
    # chart.add_series({
    #     'categories': 'Risk_Mitigation!J4:S4',
    #     'values':     'Risk_Mitigation!J5:S5',
    #     'points': [
    #         {'fill': {'color': brews['Set1'][0]}},
    #         {'fill': {'color': brews['Set1'][1]}},
    #         {'fill': {'color': brews['Set1'][2]}},
    #         {'fill': {'color': brews['Set1'][3]}},
    #         {'fill': {'color': brews['Set1'][4]}},
    #     ],
    # })

    # # Insert the chart into the worksheet.
    # worksheet.insert_chart('H4', chart)

    writer.save()
    writer.close()


get_jira('berk.akgun','Ubormetenga+')

