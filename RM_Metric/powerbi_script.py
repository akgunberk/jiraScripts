  #Berk Akgün - Risk Mitigation Metric for PowerBI python script - 17 September 2019, Tuesday

 #import all modules needed
from jira import JIRA # to interact with jira
import pandas as pd   # to use dataframes
import os             # to save excel to Desktop 

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

    df2.to_excel(writer, sheet_name = 'Risk_Mitigation' ,startrow =0, startcol=8)


    writer.save()
    writer.close()

    powerBI_Data = pd.read_excel(out_path)

    return (powerBI_Data)


data = get_jira('berk.akgun','Ubor2718+')

