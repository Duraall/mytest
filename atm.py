from tkinter import *                                                                                                                             
master = Tk ()
canvas = Canvas(master, height =450, width= 700)
canvas.pack()
ana_frame =Frame(master, background= '#b3b3ff')
ana_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
üst_yazı_çerçeve= Frame(master, background= '#ffffff')
üst_yazı= Label(üst_yazı_çerçeve, text = "DRL ATM", font= "Gentium 15 bold" )
üst_yazı.pack(padx=10, pady=10)
üst_yazı_çerçeve.place(relx=0.43, rely=0.029, relheight=0.09, relwidth=0.17)
para_çekme_çerçeve = Frame(master, background= "#ffffff")
para_çekme_çerçeve.place(relx=0.004, rely = 0.4, relheight= 0.11, relwidth= 0.30 )
para_çekme = Frame(master, background= "#ccccff")
para_çekme.place(relx=0.009, rely = 0.41, relheight= 0.09, relwidth= 0.29 )
para_çekme_yazı= Label (para_çekme, background= "#ccccff", text = "para çek", font= "Gentium 12 bold" )
para_çekme_yazı.pack( padx=10, pady=10 )
para_yatirma_cerceve = Frame(master, background= '#ffffff')
para_yatirma_cerceve.place(relx=0.004, rely = 0.55, relheight= 0.11, relwidth= 0.30)
para_yatirma  = Frame(master, background= "#ccccff")
para_yatirma.place(relx=0.009, rely = 0.56, relheight= 0.09, relwidth= 0.29 )
para_yatirma_yazı= Label (para_yatirma, background= "#ccccff", text = "para yatir", font= "Gentium 12 bold" )
para_yatirma_yazı.pack( padx=10, pady=10 )
çıkış_çerçeve = Frame(master, background="#ffffff")
çıkış_çerçeve.place(relx=0.78,rely = 0.85, relheight= 0.11, relwidth= 0.20 )
çıkış = Frame(master, background= "#ccccff")
çıkış.place(relx=0.78499,rely = 0.8539, relheight= 0.10, relwidth= 0.19)
çıkış_yazı= Label (çıkış, background= "#ccccff", text = "çıkış yap", font= "Gentium 12 bold" )
çıkış_yazı.pack( padx=10, pady=10 )



master.mainloop()

