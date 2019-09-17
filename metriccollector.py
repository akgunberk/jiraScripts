#Berk Akgün - Metric Collector App with Tkinter - 17 September 2019, Tuesday

from tkinter import *
from tkinter import filedialog, messagebox ,ttk
import connect_jira

def browse_button():
	global folder_path
	filename = filedialog.askdirectory()
	folder_path.set(filename)


window = Tk()

window.geometry('800x800+500+100')

window.title("Organizational Metric Collector")

window.configure(background = "cadet blue")


logo = PhotoImage(file="esensi-logo-nav.png")
measure_icon = PhotoImage(file="mesure.png")


main_image = Label(window, image = logo , text = "Organizational Metric Collector", bg="cadet blue", fg= "white",font="none 12 bold")
main_image.place(x=100,y=120)

measure = Label(window, image = measure_icon, bg="cadet blue", fg= "white")
measure.place(x=300,y=450)


headnote_text = Label(window,text = "Organizational Metric Collector", bg="cadet blue", fg= "white",font="none 20 bold")
headnote_text.place(x=180,y=50)

username_label = Label(window, text = 'Username',bg='white')
username_label.place(x=170,y=350)

username = Entry(window,bg='white',width=40)
username.place(x=300,y=350)

password_label = Label(window, text = 'Password',bg='white')
password_label.place(x=170,y=400)
password = Entry(window,show='*', bg='white',width=40)
password.place(x=300,y=400)

project_name_label = Label(window, text = 'Project Name',bg='white')
project_name_label.place(x=170,y=450)


Project_List = ['AVI.FIR.077_LIGHT ISR', 'AVI.FIR.154_SEAP_1.5', 'AVI.FIR.164_EGM808_EGS', 'AVI.FIR.206_KSA_VTOL', 'AVI.RAD.134_TEYDEB_HİBRİT', 'AVI.RAD.168_SAA', 'C-011 RAVIYONIK', 'C-012 SARP', 'EWS.FIR.126_TPAS_FAZ_I', 'EWS.FIR.165_TPAS_FAZ_2', 'EWS.RaD.140_TEYDEB_TPAS', 'EWS.RAD.141_TEYDEB_HF_DF', 'EWS.RAD.185_FOTAS_1501', 'P-001 WAS', 'SaS.FIR.055_GOKGOZ', 'SaS.FIR.056_AISS', 'SaS.FIR.056_GAGS-TK', 'SaS.FIR.056_GIMBAL', 'SaS.FIR.080_TUYGUN', 'SAS.FIR.132_AISS_ET', 'SaS.FIR.133_BGAG', 'SAS.FIR.174_KGAG', 'SaS.FIR.202_BALONGAG_ELD', 'SaS.RaD.092_WAAS-IRAD-2016', 'SAS.RAD.116_WAAS_IRAD_2017', 'SAS.RAD.161_TEYDEB_GAG3', 'SAS.RAD.166_EBABİL', 'SAS.RAD.204_TEYDEB_GAG_3_BV', 'SWS.FIR.065_BINT', 'SWS.FIR.104_Büyük Veri 2', 'SWS.FIR.171_ASELSAN_SST_BV', 'SWS.RAD.142 _Bilkent_1003', 'SWS.RAD.191_MSDF_GK']
project_name = ttk.Combobox(window, values=Project_List)
#project_name.config(bg='white',width=35)
project_name.place(x=300,y=450,width=245)


created_date_label = Label(window, text = 'Created Date\n(YY-MM-DD)',bg='white')
created_date_label.place(x=170,y=500)
created_date = Entry(window, bg='white',width=40)
created_date.place(x=300,y=500)

	
folder_path = StringVar()
button2 = Button(text="Save to: (Click)", command=browse_button)
button2.place(x=170,y=550)
direc = Label(master=window,bg='white',textvariable=folder_path,width=34)
direc.place(x=300,y=550)

button3 = Button(text="Give me my metric!",fg='gray38',width=18,font='none 16 bold',command= lambda: connect_jira.get_jira(username.get(),password.get(),project_name.get(),created_date.get(),folder_path.get()))
button3.place(x=300,y=600)

window.mainloop()

