#Berk Akgün - Function to connect JIRA API - 17 September 2019, Tuesday

 #import all modules needed
from jira import JIRA # to interact with jira
import pandas as pd   # to use dataframes
import tkinter


#username = input("Enter your username: ")
#password = input("Enter your password: ")
def get_jira(username,password,project_name,created_date,out_path):

    # JIRA('http://jira.esensi.local:8080/',basic_auth=('username','password'))
    
    jira = JIRA('http://jira.esensi.local:8080/',basic_auth=(username,password))

    # search issue with advanced query you used in JIRA
    query = 'project = CR AND issuetype = "Change Request" AND component = {} and "CI to be changed"="Source Code" and  cf[11110]="Defect"'
    query = query.format(project_name)
    issues_in_proj = jira.search_issues(query,maxResults = None)

    # def get_projects():
    #     CR = jira.project('CR')
    #     components = jira.project_components(CR)
    #     projects = [c.name for c in components]
    #     print (projects)
    # get_projects()

    create = created_date

    df = []

    # collect your metrics
    count = 0
    for issue in issues_in_proj:
        summ = [issue.key,issue.fields.status.name,issue.fields.reporter,issue.fields.created]
        df.append(summ)
        if issue.fields.created < create:
             count += 1

    total = len(issues_in_proj)
    metric = (total-count)/total
    print(metric)

    # summary = pd.DataFrame(summary)
    file_name = '/metricOf-' + str(project_name) +'.xlsx'
    out_path += file_name
    print(out_path)

    writer = pd.ExcelWriter(out_path, engine = 'xlsxwriter')

    df = pd.DataFrame(df,columns=['Key','Status','Reporter','Creation Time'])
    df.to_excel(writer,sheet_name='Issues')



    df2 = [project_name,created_date,total,count,metric]
    print(df2)
    df2 = pd.DataFrame([df2],columns=['Project Name','Start Date','Total # of Defects to End Item','# of Defects from Test to End Item','Test Effectiveness'])
    df2.to_excel(writer,sheet_name='Metric_Sheet')

    writer.save()
    writer.close()


# Test your function with sample data below
# get_jira('berk.akgun','Ubormetenga+','SaS.FIR.080_TUYGUN','2015-05-27','C://Users/berk.akgun/Desktop')

