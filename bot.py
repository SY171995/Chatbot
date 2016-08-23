# @Author: shubham
# @Date:   2016-08-23T00:31:31+05:30
# @Last modified by:   shubham
# @Last modified time: 2016-08-23T17:45:49+05:30



import mechanize,requests,random,webbrowser
from bs4 import BeautifulSoup
from Tkinter import *

#def get_reply():
# br = mechanize.Browser()
# br.set_handle_robots(False)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'),('Host' , 'demo.vhost.pandorabots.com'),('Connection' , 'keep-alive')]
# br.open('http://demo.vhost.pandorabots.com/pandora/talk?botid=b0dafd24ee35a477')
# #br.select_form(nr=0)
# br.select_form(name='form1')
# br.form['input'] = 'so'
# response=br.submit()
# r1=requests.get(str(response.geturl()))
# data = r1.text
# soup = BeautifulSoup(data)
# p=soup.find_all("font",color='7E2217')
    #return p
    # data=r.text
    # soup = BeautifulSoup(data)
    # d=soup.find_all('div',class_="fact")
    # return d[0].get_text()

#r=get_reply()

reply=None

def button_destroy():
    global root
    root.destroy()

def button_send():
    global entryBox
    txt=entryBox.get()
    print txt
    cookie={"_ga":"GA1.2.1148782415.1471891514","botcust2":"824b0ce55f3e678d"}
    r=requests.post("http://demo.vhost.pandorabots.com/pandora/talk?botid=b0dafd24ee35a477",data={'input':str(txt)},cookies=cookie)
    data = r.text
    soup = BeautifulSoup(data)
    p=soup.find_all("font",color='7E2217')
    print p[2].text.split('\n')[4]
    global reply
    reply.set(p[2].text.split('\n')[4])

root=Tk()
root.minsize(width=600, height=250)
#root.maxsize(width=300, height=250  )
w=Label(root,text="Chat with Chomsky")
w.pack()
entryBox = Entry(root)
entryBox.pack()
#txt=entryBox.get()
#print txt
SButton = Button(root, text="Send",command = button_send)
SButton.pack()
#print reply+"iajsi"
reply=StringVar()
reply.set("")
replyLabel = Label(root, textvariable=reply)
replyLabel.pack()
myButton = Button(root, text="Exit",command=button_destroy)
myButton.pack()
root.mainloop()


# while(1):
#     var = raw_input("You: ")
#     cookie={"_ga":"GA1.2.1148782415.1471891514","botcust2":"824b0ce55f3e678d"}
#     r=requests.post("http://demo.vhost.pandorabots.com/pandora/talk?botid=b0dafd24ee35a477",data={'input':str(var)},cookies=cookie)
#     data = r.text
#     soup = BeautifulSoup(data)
#     p=soup.find_all("font",color='7E2217')
#     print p[2].text.split('\n')[4]

#
# t=open('bot.html','w')
# t.write(r.text)
# t.close()
