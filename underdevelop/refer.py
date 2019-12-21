templet = '''
<img src="https://s2.ax1x.com/2019/12/15/QfMVC6.png" alt="QfMVC6.png" border="0">
<br>
Harvard College<br>
Office of Admissions and Financial Aid<br>
Byerly Hall<br>
8 Garden Street<br>
Cambridge, Massachusetts 02139<br>
<br>
<br>

Dear Mr. [name],<br>
<br>
I am delighted to inform you that the Committee on Admissions has admitted you to the Class of 2009 under the Early Action program. Please accept my personal congratulations for your outstanding achievements.
In recent years, nearly twenty thousand students have applied for the sixteen hundred and fifty places in the freshman class. Faced with many more talented and highly qualified candidates than it has room to admit, the Admissions Committee has taken great care to choose individuals who present extraordinary academic, extracurricular and personal strengths. In making each admission decision, the Committee keeps in mind that the excellence of Harvard College depends most of all on the talent and promise of the people assembled here, particularly our students. In voting to offer you admission, the Committee has demonstrated its firm belief that you can make important contributions during your college years and beyond.
By early March, you will receive an invitation to visit Harvard from Friday, April 29, to Sunday, May 1. Our faculty and students have arranged a special welcome for you and we think the experience will be interesting and useful in making your final college choice. Of course, we would also be happy to have you visit at some other time and we hope you will make a special effort to do so if you will be unable to join us in April.
Especially if you cannot come to Cambridge during the next several months, please do not hesitate to contact us if we can be of help in any way. You will find our application booklet and our website <a href='http://www.admissions.college.harvard.edu/'>(http://www.admissions.college.harvard.edu/)</a> good sources of information about college life and we will be sending you a course catalog in the spring to help familiarize you with our academic opportunities. We are enclosing a statement about choosing a college that might be helpful.
You have until May 1 to respond to our offer. However, we are enclosing with this letter a reply card for your use in case you are able to inform us of your decision before the May 1 reply date. A complete admission packet will be mailed to you in early April.
We very much hope that you will decide to attend Harvard, and we look forward to having you join us in September.

<br><br>
Yours sincerely,<br>
William R. Fitzsimmons<br>
Dean of Admissions and Financial Aid<br>
(Hope you will join us!)
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk

def load_templet(who):
  email_content = templet.replace('[name]', who)
  return email_content

def send_email(email_config,email_to,name):
  smtpserver = email_config['server']
  username = email_config['account']
  password = email_config['password']

  msg = MIMEMultipart('mixed')
  msg['Subject'] = 'Congratulation, ' + name + '!'
  msg['From'] = 'Harvard Admission Office <congradulation@harvard.edu>'
  msg['To'] = name + ' <'+ email_to + '>'
  text = load_templet(name)
  text_plain = MIMEText(text, 'html', 'utf-8')
  msg.attach(text_plain)

  smtp = smtplib.SMTP()
  smtp.connect(smtpserver)
  smtp.login(username, password)
  smtp.sendmail(username,email_to, msg.as_string())
  smtp.quit()


window = tk.Tk()
window.title('Harvard Offer System')
window.geometry('500x400')
window.resizable(False, False)

my_email_account = tk.StringVar()
my_email_password = tk.StringVar()
hack_email_account = tk.StringVar()
hack_name = tk.StringVar()

tk.Label(window,text='Harvard Offer System',bg='grey',font=('rockwell',20)).pack(side='top')
tk.Label(window,text='Email Account: ').place(x=60,y=80)
tk.Label(window,text='Email Password: ').place(x=60,y=120)
tk.Label(window,text='To who: ').place(x=60,y=160)
tk.Label(window,text='His/Her Email: ').place(x=60,y=200)
command_box = tk.Text(window,height=5)
command_box.insert('end','>> Welcome to Harvard Offer System!\n')
tk.Entry(window,textvariable=my_email_account).place(x=190,y=80)
tk.Entry(window,textvariable=my_email_password,show='*').place(x=190,y=120)
tk.Entry(window,textvariable=hack_name).place(x=190,y=160)
tk.Entry(window,textvariable=hack_email_account).place(x=190,y=200)

def begin():
  command_box.insert('end','>> Check input...\n')
  if my_email_account.get() == '' or my_email_password.get() == '' or hack_email_account.get() == '':
    command_box.insert('end','Fail because the input is incomplete!\n')
  else:
    email_config = {
      'server':'smtp.163.com',
      'account':my_email_account.get(),
      'password':my_email_password.get()
    }
    name = hack_name.get()
    email_to = hack_email_account.get()
    try:
      send_email(email_config,email_to,name)
      command_box.insert('end','>> Offer send successfully!\n')
    except Exception as e:
      command_box.insert('end','Error Happen: ' + str(e) + ', please try again!\n')

tk.Button(window,text='Send Offer',command=begin).place(x=200,y=250)
command_box.pack(side='bottom')

tk.mainloop()


