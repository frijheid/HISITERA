#######################################################################################################################################
#IMPORT
import tkinter as tk
from tkinter import ttk
#from tkinter import scrolledtext
from tkinter import Menu
#from tkinter import messagebox
#from tkinter import font
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math #berfungsi untuk eksponen
#######################################################################################################################################

def destroyed():
    splash.destroy()
    PROGRAM()

def PROGRAM():
    def keluar():
        exit()
    #INSTANSI
    win=tk.Tk()
    win.focus_force()
    #======================================================================================================================================
    #PROPERTI INSTANSI
    win.title("H  I  S  I  T  E  R  A")
    ww=(((win.winfo_screenwidth())/2)-275)
    wh=(((win.winfo_screenheight())/2)-275)
    win.geometry("560x560+%d+%d"%(ww,wh))
    win.resizable(0,0)
       
    #======================================================================================================================================
    #PROPERTI TEKS
    judul=("Helvetica",14,("underline","bold"))
    simbol=("Symbol",12)
    tombol=("Helvetica",25,("bold"))
    
    #======================================================================================================================================
    ### FUNGSI ###
    
    #FUNGSI DI BILAH MENU
    def about_klik():
        win_about=tk.Toplevel(win)
        win_about.title("About Me")
        ww=(((win.winfo_screenwidth())/2)-235)
        wh=(((win.winfo_screenheight())/2)-100)
        win_about.geometry("470x200+%d+%d"%(ww,wh))
        win_about.resizable(0,0)
        about_frame=ttk.LabelFrame(win_about,text="HISITERA 0.91")
        about_frame.grid(row=0,column=0,padx=8,pady=4)
        about_teks=ttk.Label(about_frame,text="Copyright by\n"
                            "Andhy Setyo Raharjo\n"
                            "Kelompok Keahlian Rekayasa Sumber Daya Air\n"
                            "Published by Program Studi Teknik Sipil Institut Teknologi Sumatera\n\n"
                            "HISSI adalah program perhitungan hidrograf satuan sintetik dengan metode komputasi,\n"
                            "yang diharapkan dapat bekerja secara cepat dan tepat guna melengkapi data,\n"
                            "yang bisa digunakan untuk berbagai keperluan yang berhubungan dengan air.\n\n"
                            
                            "Masukan, kritik, dan saran sangat diterima.\n"
                            "Email: mashuri@si.itera.ac.id"
                            )
        win_about.focus()
        win_about.attributes("-topmost","True")
        about_teks.grid(row=0,column=0)
#======================================================================================================================================
#BILAH MENU
    menu_bar=tk.Menu(win)
    win.config(menu=menu_bar)
    #------------------------------------------------------------------------------------
    file_menu=Menu(menu_bar,tearoff=0)#tearoff berfungsi menghilangkan garis patah patah di bawah file menu
    file_menu.add_command(label="EXIT",command=keluar)
    help_menu=Menu(menu_bar,tearoff=0)
    help_menu.add_command(label="About",command=about_klik)
    #------------------------------------------------------------------------------------
    menu_bar.add_cascade(label="File",menu=file_menu)
    menu_bar.add_cascade(label="Help",menu=help_menu)
    #======================================================================================================================================
    #BILAH TABS
    tabControl=ttk.Notebook(win)
    tab1=ttk.Frame(tabControl)
    tabControl.add(tab1,text="DATA")
    tab2=ttk.Frame(tabControl)
    tabControl.add(tab2,text="Nakayasu")
    tab3=ttk.Frame(tabControl)
    tabControl.add(tab3,text="Snyder")
    tab4=ttk.Frame(tabControl)
    tabControl.add(tab4,text="SCS")
    tab5=ttk.Frame(tabControl)
    tabControl.add(tab5,text="GAMA-1")
    #------------------------------------------------------------------------------------
    tabControl.pack(expand=1,fill="both")
    #======================================================================================================================================
    #LABEL FRAME
    mighty1=ttk.LabelFrame(tab1,text="Data Diketahui:")
    mighty1.grid(row=0,column=0,padx=8,pady=4)
    mighty2=ttk.Labelframe(tab2,text="Nakayasu Method")
    mighty2.grid(row=0,column=0,padx=8,pady=4)
    mighty3=ttk.Labelframe(tab3,text="Snyder Method")
    mighty3.grid(row=0,column=0,padx=8,pady=4)
    mighty4=ttk.Labelframe(tab4,text="SCS Method")
    mighty4.grid(row=0,column=0,padx=8,pady=4)
    mighty5=ttk.Labelframe(tab5,text="GAMA-1 Method")
    mighty5.grid(row=0,column=0,padx=8,pady=4)
#======================================================================================================================================
##Tooltip
    class Tooltip(object):
        def __init__(self,widget,tip_text=None):
            self.widget=widget
            self.tip_text=tip_text
            widget.bind("<Enter>",self.mouse_enter)
            widget.bind("<Leave>",self.mouse_leave)

        def mouse_enter(self,_event):
            self.show_tooltip()
        def mouse_leave(self,_event):
            self.hide_tooltip()

        def show_tooltip(self):
            if self.tip_text:
                x_left=self.widget.winfo_rootx()
                y_top=self.widget.winfo_rooty()-18
                self.tip_window=tk.Toplevel(self.widget)
                self.tip_window.overrideredirect(True)
                self.tip_window.geometry("+%d+%d"%(x_left,y_top))
                label=tk.Label(self.tip_window,text=self.tip_text,justify=tk.LEFT,
                background="#ffffe0",relief=tk.SOLID,borderwidth=1,
                font=("tahoma","8","normal"))
                label.pack(ipadx=1)
        def hide_tooltip(self):
            if self.tip_window:
                self.tip_window.destroy()
#======================================================================================================================================
### ISI TAB 1 ###
    judul_tab1=ttk.Label(mighty1,text="DATA KARAKTERISTIK DAS",font=judul)
    judul_tab1.grid(row=0,column=0,columnspan=4,pady=(0,10),sticky="W")
    #------------------------------------------------------------------------------------
    adas_teks_tab1=ttk.Label(mighty1,text="Luas DAS")
    adas_teks_tab1.grid(row=1,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=1,column=1)
    adas_var=tk.DoubleVar()
    adas_entry=ttk.Entry(mighty1,textvariable=adas_var)
    adas_entry.grid(row=1,column=2,padx=10,pady=5)
    adas_satuan_tab1=ttk.Label(mighty1,text=u"km\u00B2")
    adas_satuan_tab1.grid(row=1,column=3)
    #------------------------------------------------------------------------------------
    ldas_teks_tab1=ttk.Label(mighty1,text="Panjang Sungai Utama")
    ldas_teks_tab1.grid(row=2,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=2,column=1)
    lsungai_var=tk.DoubleVar()
    lsungai_entry=ttk.Entry(mighty1,textvariable=lsungai_var)
    lsungai_entry.grid(row=2,column=2,padx=10,pady=5)
    lsungai_satuan_tab1=ttk.Label(mighty1,text="km")
    lsungai_satuan_tab1.grid(row=2,column=3)
    #------------------------------------------------------------------------------------
#INFILTRASI HORTON TEKS
    judu2_tab1=ttk.Label(mighty1,text="INFILTRASI HORTON",font=judul)
    judu2_tab1.grid(row=3,column=0,columnspan=4,pady=(20,0),sticky="W")
    #------------------------------------------------------------------------------------
    hortonfo1_teks_tab1=ttk.Label(mighty1,text="Persen fo")
    hortonfo1_teks_tab1.grid(row=4,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=4,column=1)
    hortonfo1_var=tk.DoubleVar()
    hortonfo1_entry=ttk.Entry(mighty1,textvariable=hortonfo1_var)
    hortonfo1_entry.grid(row=4,column=2,padx=10,pady=5)
    hortonfo1_satuan_tab1=ttk.Label(mighty1,text="%")
    hortonfo1_satuan_tab1.grid(row=4,column=3)
    #------------------------------------------------------------------------------------
    hortonfo2_teks_tab1=ttk.Label(mighty1,text="fo")
    hortonfo2_teks_tab1.grid(row=5,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=5,column=1)
    hortonfo2_var=tk.DoubleVar()
    hortonfo2_entry=ttk.Entry(mighty1,textvariable=hortonfo2_var,state="readonly")
    hortonfo2_entry.grid(row=5,column=2,padx=10,pady=5)
    hortonfo2_satuan_tab1=ttk.Label(mighty1,text="mm")
    hortonfo2_satuan_tab1.grid(row=5,column=3)
    #------------------------------------------------------------------------------------
    hortonfc_teks_tab1=ttk.Label(mighty1,text="fc")
    hortonfc_teks_tab1.grid(row=6,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=6,column=1)
    hortonfc_var=tk.DoubleVar()
    hortonfc_entry=ttk.Entry(mighty1,textvariable=hortonfc_var)
    hortonfc_entry.grid(row=6,column=2,padx=10,pady=5)
    hortonfc_satuan_tab1=ttk.Label(mighty1,text="cm/jam")
    hortonfc_satuan_tab1.grid(row=6,column=3)
    #------------------------------------------------------------------------------------
    hortonk_teks_tab1=ttk.Label(mighty1,text="k")
    hortonk_teks_tab1.grid(row=7,column=0,sticky="W",padx=(0,5))
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=7,column=1)
    hortonk_var=tk.DoubleVar()
    hortonk_entry=ttk.Entry(mighty1,textvariable=hortonk_var)
    hortonk_entry.grid(row=7,column=2,padx=10,pady=5)
    #hortonk_satuan_tab1=ttk.Label(mighty1,text="mm")
    #hortonk_satuan_tab1.grid(row=7,column=3)
    #------------------------------------------------------------------------------------
    #FUNGSI
    def hitung_fo2():
        hortonfo2_entry.configure(state="normal")
        hortonfo2_entry.delete(0,"end")
        hortonfo2_entry.insert(tk.INSERT,((hortonfo1_var.get()/100)*rtot_kolom71_var_tab1.get()))
        hortonfo2_entry.configure(state="readonly")
    #TOMBOL
    hortonfo2_hitung=tk.Button(mighty1,text="Hitung fo",command=hitung_fo2)
    hortonfo2_hitung.grid(row=5,column=4,padx=10)
#------------------------------------------------------------------------------------
#INFILTRASI HORTON INPUT
    input_rtot_frame=tk.LabelFrame(mighty1,text="Input Data R Total")
    input_rtot_frame.grid(row=8,columnspan=4,sticky="w")
    #------------------------------------------------------------------------------------
    def validate():
        return False
#Kolom jam
    judul_rtot_kolom00_var=tk.StringVar(value="Jam")
    judul_rtot_kolom00=tk.Entry(input_rtot_frame,justify="center",textvariable=judul_rtot_kolom00_var,validatecommand=validate,bg="gray",fg="white",width=10)
    judul_rtot_kolom00.update()
    judul_rtot_kolom00.configure(validate="key")
    judul_rtot_kolom00.grid(row=0,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom10_var_tab1=tk.StringVar(value="1")
    jam_kolom10_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom10_var_tab1,validatecommand=validate,width=10)
    jam_kolom10_tab1.update()
    jam_kolom10_tab1.configure(validate="key")
    jam_kolom10_tab1.grid(row=1,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom20_var_tab1=tk.StringVar(value="2")
    jam_kolom20_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom20_var_tab1,validatecommand=validate,width=10)
    jam_kolom20_tab1.update()
    jam_kolom20_tab1.configure(validate="key")
    jam_kolom20_tab1.grid(row=2,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom30_var_tab1=tk.StringVar(value="3")
    jam_kolom30_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom30_var_tab1,validatecommand=validate,width=10)
    jam_kolom30_tab1.update()
    jam_kolom30_tab1.configure(validate="key")
    jam_kolom30_tab1.grid(row=3,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom40_var_tab1=tk.StringVar(value="4")
    jam_kolom40_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom40_var_tab1,validatecommand=validate,width=10)
    jam_kolom40_tab1.update()
    jam_kolom40_tab1.configure(validate="key")
    jam_kolom40_tab1.grid(row=4,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom50_var_tab1=tk.StringVar(value="5")
    jam_kolom50_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom50_var_tab1,validatecommand=validate,width=10)
    jam_kolom50_tab1.update()
    jam_kolom50_tab1.configure(validate="key")
    jam_kolom50_tab1.grid(row=5,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom60_var_tab1=tk.StringVar(value="6")
    jam_kolom60_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom60_var_tab1,validatecommand=validate,width=10)
    jam_kolom60_tab1.update()
    jam_kolom60_tab1.configure(validate="key")
    jam_kolom60_tab1.grid(row=6,column=0)
    #------------------------------------------------------------------------------------
    jam_kolom70_var_tab1=tk.StringVar(value="Total")
    jam_kolom70_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=jam_kolom70_var_tab1,validatecommand=validate,width=10)
    jam_kolom70_tab1.update()
    jam_kolom70_tab1.configure(validate="key")
    jam_kolom70_tab1.grid(row=7,column=0)
#------------------------------------------------------------------------------------
#Kolom Rtot
    judul_rtot_kolom01_var=tk.StringVar(value="Rtot (mm)")
    judul_rtot_kolom01=tk.Entry(input_rtot_frame,justify="center",textvariable=judul_rtot_kolom01_var,validatecommand=validate,bg="gray",fg="white")
    judul_rtot_kolom01.update()
    judul_rtot_kolom01.configure(validate="key")
    judul_rtot_kolom01.grid(row=0,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom11_var_tab1=tk.DoubleVar()
    rtot_kolom11_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom11_var_tab1)
    rtot_kolom11_tab1.grid(row=1,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom21_var_tab1=tk.DoubleVar()
    rtot_kolom21_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom21_var_tab1)
    rtot_kolom21_tab1.grid(row=2,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom31_var_tab1=tk.DoubleVar()
    rtot_kolom31_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom31_var_tab1)
    rtot_kolom31_tab1.grid(row=3,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom41_var_tab1=tk.DoubleVar()
    rtot_kolom41_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom41_var_tab1)
    rtot_kolom41_tab1.grid(row=4,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom51_var_tab1=tk.DoubleVar()
    rtot_kolom51_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom51_var_tab1)
    rtot_kolom51_tab1.grid(row=5,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom61_var_tab1=tk.DoubleVar()
    rtot_kolom61_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom61_var_tab1)
    rtot_kolom61_tab1.grid(row=6,column=1)
    #------------------------------------------------------------------------------------
    rtot_kolom71_var_tab1=tk.DoubleVar()
    rtot_kolom71_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=rtot_kolom71_var_tab1,state="readonly")
    rtot_kolom71_tab1.grid(row=7,column=1)
    #------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#Kolom Infiltrasi
    judul_rtot_kolom02_var=tk.StringVar(value="Infil (mm)")
    judul_rtot_kolom02=tk.Entry(input_rtot_frame,justify="center",textvariable=judul_rtot_kolom02_var,validatecommand=validate,bg="gray",fg="white")
    judul_rtot_kolom02.update()
    judul_rtot_kolom02.configure(validate="key")
    judul_rtot_kolom02.grid(row=0,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom12_var_tab1=tk.DoubleVar()
    infil_kolom12_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom12_var_tab1)
    infil_kolom12_tab1.grid(row=1,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom22_var_tab1=tk.DoubleVar()
    infil_kolom22_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom22_var_tab1)
    infil_kolom22_tab1.grid(row=2,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom32_var_tab1=tk.DoubleVar()
    infil_kolom32_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom32_var_tab1)
    infil_kolom32_tab1.grid(row=3,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom42_var_tab1=tk.DoubleVar()
    infil_kolom42_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom42_var_tab1)
    infil_kolom42_tab1.grid(row=4,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom52_var_tab1=tk.DoubleVar()
    infil_kolom52_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom52_var_tab1)
    infil_kolom52_tab1.grid(row=5,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom62_var_tab1=tk.DoubleVar()
    infil_kolom62_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom62_var_tab1)
    infil_kolom62_tab1.grid(row=6,column=2)
    #------------------------------------------------------------------------------------
    infil_kolom72_var_tab1=tk.DoubleVar()
    infil_kolom72_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=infil_kolom72_var_tab1,state="readonly")
    infil_kolom72_tab1.grid(row=7,column=2)
#------------------------------------------------------------------------------------
#Kolom Reff
    judul_rtot_kolom03_var=tk.StringVar(value="Reff (mm)")
    judul_rtot_kolom03=tk.Entry(input_rtot_frame,justify="center",textvariable=judul_rtot_kolom03_var,validatecommand=validate,bg="gray",fg="white")
    judul_rtot_kolom03.update()
    judul_rtot_kolom03.configure(validate="key")
    judul_rtot_kolom03.grid(row=0,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom13_var_tab1=tk.DoubleVar()
    reff_kolom13_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom13_var_tab1)
    reff_kolom13_tab1.grid(row=1,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom23_var_tab1=tk.DoubleVar()
    reff_kolom23_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom23_var_tab1)
    reff_kolom23_tab1.grid(row=2,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom33_var_tab1=tk.DoubleVar()
    reff_kolom33_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom33_var_tab1)
    reff_kolom33_tab1.grid(row=3,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom43_var_tab1=tk.DoubleVar()
    reff_kolom43_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom43_var_tab1)
    reff_kolom43_tab1.grid(row=4,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom53_var_tab1=tk.DoubleVar()
    reff_kolom53_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom53_var_tab1)
    reff_kolom53_tab1.grid(row=5,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom63_var_tab1=tk.DoubleVar()
    reff_kolom63_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom63_var_tab1)
    reff_kolom63_tab1.grid(row=6,column=3)
    #------------------------------------------------------------------------------------
    reff_kolom73_var_tab1=tk.DoubleVar()
    reff_kolom73_tab1=ttk.Entry(input_rtot_frame,justify="center",textvariable=reff_kolom73_var_tab1,state="readonly")
    reff_kolom73_tab1.grid(row=7,column=3)
    #------------------------------------------------------------------------------------
    
        
    """
    ch_teks_tab1=ttk.Label(mighty1,text="Tinggi Hujan")
    ch_teks_tab1.grid(row=3,column=0,sticky="W")
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=3,column=1)
    ch_var=tk.DoubleVar()
    ch_entry=ttk.Entry(mighty1,textvariable=ch_var)
    ch_entry.grid(row=3,column=2,padx=10,pady=5)
    ch_satuan_tab1=ttk.Label(mighty1,text="mm")
    ch_satuan_tab1.grid(row=3,column=3)"""
    #------------------------------------------------------------------------------------
    """t_teks_tab1=ttk.Label(mighty1,text="Durasi Hujan")
    t_teks_tab1.grid(row=4,column=0,sticky="W")
    samad_tab1=ttk.Label(mighty1,text="=")
    samad_tab1.grid(row=4,column=1)
    t_var=tk.DoubleVar()
    t_entry=ttk.Entry(mighty1,textvariable=t_var)
    t_entry.grid(row=4,column=2,padx=10,pady=5)
    t_satuan_tab1=ttk.Label(mighty1,text="jam")
    t_satuan_tab1.grid(row=4,column=3)"""
    #------------------------------------------------------------------------------------
    #adas_entry.delete(0,"end")
    #adas_entry.insert(tk.INSERT,216.37)
    #lsungai_entry.delete(0,"end")
    #lsungai_entry.insert(tk.INSERT,65)
    #ch_entry.delete(0,"end")
    #ch_entry.insert(tk.INSERT,1)
#------------------------------------------------------------------------------------
#Hitung Tabel Horton
    def hitung_horton_tabel():
        #JUMLAH RTOT
            rtot_kolom71_tab1.configure(state="normal")
            rtot_kolom71_tab1.delete(0,"end")
            rtot_jumlah=(
                rtot_kolom11_var_tab1.get()+rtot_kolom21_var_tab1.get()+
                rtot_kolom31_var_tab1.get()+rtot_kolom41_var_tab1.get()+
                rtot_kolom51_var_tab1.get()+rtot_kolom61_var_tab1.get()
                )
            rtot_kolom71_tab1.insert(tk.INSERT,rtot_jumlah)
            rtot_kolom71_tab1.configure(state="readonly")
        #------------------------------------------------------------------------------------
        #PERHITUNGAN INFILTRASI
            #if (hortonfo2_var.get()!=0):
            infil_kolom12_tab1.delete(0,"end")
            infil_kolom12_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*1))
                )
            infil_kolom22_tab1.delete(0,"end")
            infil_kolom22_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*2))
                )
            infil_kolom32_tab1.delete(0,"end")
            infil_kolom32_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*3))
                )
            infil_kolom42_tab1.delete(0,"end")
            infil_kolom42_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*4))
                )
            infil_kolom52_tab1.delete(0,"end")
            infil_kolom52_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*5))
                )
            infil_kolom62_tab1.delete(0,"end")
            infil_kolom62_tab1.insert(
                tk.INSERT,
                hortonfc_var.get()+
                ((hortonfo2_var.get()-hortonfc_var.get())*math.exp((-hortonk_var.get())*6))
                )
            #------------------------------------------------------------------------------------
            #JUMLAH INFILTRESI
            infil_kolom72_tab1.configure(state="normal")
            infil_kolom72_tab1.delete(0,"end")
            infil_jumlah=(
                infil_kolom12_var_tab1.get()+infil_kolom22_var_tab1.get()+
                infil_kolom32_var_tab1.get()+infil_kolom42_var_tab1.get()+
                infil_kolom52_var_tab1.get()+infil_kolom62_var_tab1.get()
                )
            infil_kolom72_tab1.insert(tk.INSERT,infil_jumlah)
            infil_kolom72_tab1.configure(state="readonly")
            """else:
                infil_kolom12_tab1.delete(0,"end")
                infil_kolom12_tab1.insert(tk.INSERT,0.0)
                infil_kolom22_tab1.delete(0,"end")
                infil_kolom22_tab1.insert(tk.INSERT,0.0)
                infil_kolom32_tab1.delete(0,"end")
                infil_kolom32_tab1.insert(tk.INSERT,0.0)
                infil_kolom42_tab1.delete(0,"end")
                infil_kolom42_tab1.insert(tk.INSERT,0.0)
                infil_kolom52_tab1.delete(0,"end")
                infil_kolom52_tab1.insert(tk.INSERT,0.0)
                infil_kolom62_tab1.delete(0,"end")
                infil_kolom62_tab1.insert(tk.INSERT,0.0)
                
                infil_kolom72_tab1.delete(0,"end")
                infil_kolom72_tab1.insert(tk.INSERT,0.0)"""    
        #------------------------------------------------------------------------------------
        #PERHITUNGAN REFF
            
            reff_kolom13_tab1.delete(0,"end")
            reff_kolom13_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom11_var_tab1.get()-infil_kolom12_var_tab1.get())
                )
            )    
            reff_kolom23_tab1.delete(0,"end")
            reff_kolom23_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom21_var_tab1.get()-infil_kolom22_var_tab1.get())
                )
            )
            reff_kolom33_tab1.delete(0,"end")
            reff_kolom33_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom31_var_tab1.get()-infil_kolom32_var_tab1.get())
                )
            )
            reff_kolom43_tab1.delete(0,"end")
            reff_kolom43_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom41_var_tab1.get()-infil_kolom42_var_tab1.get())
                )
            )
            reff_kolom53_tab1.delete(0,"end")
            reff_kolom53_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom51_var_tab1.get()-infil_kolom52_var_tab1.get())
                )
            )
            reff_kolom63_tab1.delete(0,"end")
            reff_kolom63_tab1.insert(
                tk.INSERT,
                max(
                    0,
                    (rtot_kolom61_var_tab1.get()-infil_kolom62_var_tab1.get())
                )
            )
            #------------------------------------------------------------------------------------
            #JUMLAH REFF
            reff_kolom73_tab1.configure(state="normal")
            reff_kolom73_tab1.delete(0,"end")
            reff_jumlah=(
                reff_kolom13_var_tab1.get()+reff_kolom23_var_tab1.get()+
                reff_kolom33_var_tab1.get()+reff_kolom43_var_tab1.get()+
                reff_kolom53_var_tab1.get()+reff_kolom63_var_tab1.get()
                )
            reff_kolom73_tab1.insert(tk.INSERT,reff_jumlah)
            reff_kolom73_tab1.configure(state="readonly")
    

    #------------------------------------------------------------------------------------
    #TOMBOL HORTON
    horton_hitung_tombol=tk.Button(input_rtot_frame,width=30,text="HITUNG",command=hitung_horton_tabel)
    horton_hitung_tombol.grid(row=8,column=0,columnspan=4,pady=10)
#======================================================================================================================================
### ISI TAB 2 ###
    judul1_tab2=ttk.Label(mighty2,text="DATA",font=judul)
    judul1_tab2.grid(row=0,column=0,columnspan=8,pady=(0,10),sticky="W")
    #------------------------------------------------------------------------------------
    alfa_teks_tab2=ttk.Label(mighty2,text=u"\u221D",font=simbol)
    alfa_teks_tab2.grid(row=1,column=0,sticky="W",padx=(0,20))
    alfa_var=tk.DoubleVar()
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=1,column=1)
    alfa_entry=ttk.Entry(mighty2,textvariable=alfa_var)
    alfa_entry.grid(row=1,column=2)
    #------------------------------------------------------------------------------------
    """ch_teks_tab1=ttk.Label(mighty2,text="Tinggi Hujan")
    ch_teks_tab1.grid(row=1,column=4,sticky="W")
    samad_tab1=ttk.Label(mighty2,text="=")
    samad_tab1.grid(row=1,column=5)
    ch_var=tk.DoubleVar()
    ch_entry=ttk.Entry(mighty2,textvariable=ch_var)
    ch_entry.grid(row=1,column=6,padx=10,pady=5)
    ch_satuan_tab1=ttk.Label(mighty2,text="mm")
    ch_satuan_tab1.grid(row=1,column=7)"""
    ch_var=tk.DoubleVar()
    ch_var.set(1)
    #------------------------------------------------------------------------------------
    judul2_tab2=ttk.Label(mighty2,text="HASIL PERHITUNGAN",font=judul)
    judul2_tab2.grid(row=2,column=0,columnspan=8,pady=(20,10),sticky="W")
    #------------------------------------------------------------------------------------
    tg_teks_tab2=ttk.Label(mighty2,text="tg")
    tg_teks_tab2.grid(row=3,column=0,sticky="W")
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=3,column=1)
    tg_var=tk.DoubleVar()
    tg_entry=ttk.Entry(mighty2,textvariable=tg_var,state="readonly")
    tg_entry.grid(row=3,column=2,padx=10,pady=5)
    tg_satuan_tab2=ttk.Label(mighty2,text="jam")
    tg_satuan_tab2.grid(row=3,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    t03_teks_tab2=ttk.Label(mighty2,text="T0,3")
    t03_teks_tab2.grid(row=4,column=0,sticky="W")
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=4,column=1)
    t03_var=tk.DoubleVar()
    t03_entry=ttk.Entry(mighty2,textvariable=t03_var,state="readonly")
    t03_entry.grid(row=4,column=2,padx=10,pady=5)
    t03_satuan_tab2=ttk.Label(mighty2,text="jam")
    t03_satuan_tab2.grid(row=4,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tr_teks_tab2=ttk.Label(mighty2,text="tr")
    tr_teks_tab2.grid(row=5,column=0,sticky="W")
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=5,column=1)
    tr_var=tk.DoubleVar()
    tr_entry=ttk.Entry(mighty2,textvariable=tr_var,state="readonly")
    tr_entry.grid(row=5,column=2,padx=10,pady=5)
    tr_satuan_tab2=ttk.Label(mighty2,text="jam")
    tr_satuan_tab2.grid(row=5,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tp_teks_tab2=ttk.Label(mighty2,text="Tp")
    tp_teks_tab2.grid(row=6,column=0,sticky="W")
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=6,column=1)
    tp1_var=tk.DoubleVar()
    tp_entry=ttk.Entry(mighty2,textvariable=tp1_var,state="readonly")
    tp_entry.grid(row=6,column=2,padx=10,pady=5)
    tp_satuan_tab2=ttk.Label(mighty2,text="jam")
    tp_satuan_tab2.grid(row=6,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    qp_teks_tab2=ttk.Label(mighty2,text=u"Qp")
    qp_teks_tab2.grid(row=7,column=0,sticky="W")
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=7,column=1)
    qp1_var=tk.DoubleVar()
    qp1_entry=ttk.Entry(mighty2,textvariable=qp1_var,state="readonly")
    qp1_entry.grid(row=7,column=2,padx=10,pady=5)
    qp_satuan_tab2=ttk.Label(mighty2,text=u"m\u00B3/s")
    qp_satuan_tab2.grid(row=7,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    vol_teks_tab2=ttk.Label(mighty2,text="Vol HSS")
    vol_teks_tab2.grid(row=3,column=4,sticky="W",padx=20)
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=3,column=5)
    vol_var_tab2=tk.DoubleVar()
    vol_entry_tab2=ttk.Entry(mighty2,textvariable=vol_var_tab2,state="readonly")
    vol_entry_tab2.grid(row=3,column=6,padx=10,pady=5)
    qp_satuan_tab2=ttk.Label(mighty2,text=u"m\u00B3")
    qp_satuan_tab2.grid(row=3,column=7,sticky="W")
    #------------------------------------------------------------------------------------
    dro_teks_tab2=ttk.Label(mighty2,text="DRO")
    dro_teks_tab2.grid(row=4,column=4,sticky="W",padx=20)
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=4,column=5)
    dro_var_tab2=tk.DoubleVar()
    dro_entry_tab2=ttk.Entry(mighty2,textvariable=dro_var_tab2,state="readonly")
    dro_entry_tab2.grid(row=4,column=6,padx=10,pady=5)
    dro_satuan_tab2=ttk.Label(mighty2,text="mm")
    dro_satuan_tab2.grid(row=4,column=7,sticky="W")
    #------------------------------------------------------------------------------------
    error_teks_tab2=ttk.Label(mighty2,text="error")
    error_teks_tab2.grid(row=5,column=4,sticky="W",padx=20)
    samad_tab2=ttk.Label(mighty2,text="=")
    samad_tab2.grid(row=5,column=5)
    error_var_tab2=tk.DoubleVar()
    error_entry_tab2=ttk.Entry(mighty2,textvariable=error_var_tab2,state="readonly")
    error_entry_tab2.grid(row=5,column=6,padx=10,pady=5)
    error_satuan_tab2=ttk.Label(mighty2,text="%")
    error_satuan_tab2.grid(row=5,column=7,sticky="W")
#======================================================================================================================================
### HITUNG TAB 2 ###
#Hitung Bagian 1(Variabel)
    def hitung_tab2():
        tg_entry.configure(state="normal")
        t03_entry.configure(state="normal")
        tr_entry.configure(state="readonly")
        tp_entry.configure(state="normal")
        qp1_entry.configure(state="normal")
        vol_entry_tab2.configure(state="normal")
        dro_entry_tab2.configure(state="normal")
        error_entry_tab2.configure(state="normal")

        if (adas_var.get==0 or lsungai_var.get()==0 or ch_var.get()==0 or alfa_var.get()==0):# or t_var.get()==0
            tk.messagebox.showwarning("GALAT","Data belum lengkap")
        
        #Tg
        if lsungai_var.get()>15:
            tg_entry.delete(0,"end")
            tg_tab1=0.4+(0.058*lsungai_var.get())
            tg_entry.insert(tk.INSERT,tg_tab1)
        elif lsungai_var.get()<=15:
            tg_entry.delete(0,"end")
            tg_tab1=0.21*((lsungai_var.get())**0.7)
            tg_entry.insert(tk.INSERT,tg_tab1)
        
        #t0,3
        t03_entry.delete(0,"end")
        t03=alfa_var.get()*tg_var.get()
        t03_entry.insert(tk.INSERT,t03)

        #tr
        if tg_var.get()!=0:
            tr_entry.configure(state="normal")
            tr_entry.delete(0,"end")
            tr=(0.75*tg_var.get())
            tr_entry.insert(tk.INSERT,tr)
        
            
        #Tp
        if tr_var.get()!=0:
            tp_entry.delete(0,"end")
            tp=tg_var.get()+(0.8*tr_var.get())
            tp_entry.insert(tk.INSERT,tp)

            
        #Qp
        if (adas_var.get()!=0 and ch_var.get()!=0 and tp1_var.get()!=0 and t03_var.get()!=0):
            qp1_entry.delete(0,"end")
            qp=((1/3.6)*((adas_var.get()*ch_var.get())/((0.3*tp1_var.get())+t03_var.get())))
            qp1_entry.insert(tk.INSERT,qp)

    
        tg_entry.configure(state="readonly")
        t03_entry.configure(state="readonly")
        tr_entry.configure(state="readonly")
        tp_entry.configure(state="readonly")
        qp1_entry.configure(state="readonly")
#------------------------------------------------------------------------------------
#Hitung Bagian 2 (t dan Qt)
        #===========================================================
        global t
        global qt
        global qt_nakayasu_koreksi

        qt=[]
        qt_nakayasu_koreksi=[]
        tp=tp1_var.get()
        qp=qp1_var.get()
        t03=t03_var.get()
        voltab2=([0])
        #===========================================================
        #Kurva Naik
        awal=0
        akhir=tp
        if round(tp)>tp:
            #Qt
            for x in range(awal,round(akhir),1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            b=(qp*((tp/tp)**2.4))
            qt.append(b)
            #Tp
            t=list(range(round(tp)))
            t.append(tp)
        

        elif round(tp)<tp:
            #Qt
            for x in range(awal,round(akhir)+1,1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            b=(qp*((tp/tp)**2.4))
            qt.append(b)
            #Tp
            t=list(range(round(akhir)+1))
            t.append(tp)

        elif round(tp)==tp:
            #Qt
            for x in range(akhir+1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            #Tp
            t=list(range(round(akhir)+1))

        #print(t,"\n",qt,"\n")
        #===========================================================
        #Kurva Turun 1
        
        awal=tp
        akhir=tp+t03

        if round(awal)>awal:
            awal=round(round(awal))
        elif round(awal)<awal:
            awal=round(awal)+1
      
        if round(akhir)>akhir:
            #qt
            for x in range (awal,round(akhir),1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            b=(qp*((0.3)**((akhir-tp)/t03)))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)))
            t=t+t1
            t.append(akhir)

        if round(akhir)<akhir:
            for x in range (awal,round(akhir)+1,1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            b=(qp*((0.3)**((akhir-tp)/t03)))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)+1,1))
            t=t+t1
            t.append(akhir)

        elif round(akhir)==akhir:
            #Qt
            for x in range(awal,akhir+1,1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            #Tp
            t1=list(range(akhir+1))
            t=t+t1
            
       # print(t,"\n",qt,"\n")


        #===========================================================
        #Kurva Turun 2
        awal=tp+t03
        akhir=tp+t03+(1.5*t03)

        if round(awal)>awal:
            awal=round(round(awal))
        elif round(awal)<awal:
            awal=round(awal)+1
        #----------------------------
        if round(akhir)>akhir:
            #qt
            for x in range (awal,round(akhir),1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            b=(qp*((0.3)**(((akhir-tp)+(0.5*t03))/(1.5*t03))))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)))
            t=t+t1
            t.append(akhir)

        if round(akhir)<akhir:
            for x in range (awal,round(akhir)+1,1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            b=(qp*((0.3)**(((akhir-tp)+(0.5*t03))/(1.5*t03))))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)+1,1))
            t=t+t1
            t.append(akhir)

        elif round(akhir)==akhir:
            #Qt
            for x in range(awal,akhir+1,1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            #Tp
            t1=list(range(akhir+1))
            t=t+t1
        #===========================================================
        #TURUN 3
        awal=tp+t03+(1.5*t03)
        if round(awal)>awal:
            awal=round(awal)
        elif round(awal)<awal:
            awal=round(awal)+1
        #----------------------------
        x=awal

        while (a>0.1):
            a=(qp*((0.3)**(((x-tp)+(1.5*t03))/(2*t03))))
            if (a>0.1):
                qt.append(a)
                t.append(x)
            x+=1

        #VOLUME
        qtot_nakayasu=sum(qt)
        vll_nakayasu=qtot_nakayasu*60*60
        

        #DRO
        dro_nakayasu=(vll_nakayasu/(adas_var.get()*10**6))*1000

        #QT_Koreksi
        for i in range(len(t)):
            qt_nakayasu_koreksi.append(qt[i]/dro_nakayasu)

        #VLL KOREKSI
        vll_nakayasu_koreksi=(sum(qt_nakayasu_koreksi)*60*60)

        #DRO KOREKSI
        dro_nakayasu_koreksi=(vll_nakayasu_koreksi/(adas_var.get()*10**6))*1000

        #Hitung Bagian 3 (Output ke Vol dan DRO)
#------------------------------------------------------------------------------------
#Hitung Bagian 3 (Output ke Vol dan DRO)
        vol_entry_tab2.delete(0,"end")
        vol_entry_tab2.insert(tk.INSERT,round(vll_nakayasu_koreksi))
        
        dro_entry_tab2.delete(0,"end")
        dro_entry_tab2.insert(tk.INSERT,round(dro_nakayasu_koreksi))

        error2=round((abs(float(dro_entry_tab2.get())-ch_var.get())/ch_var.get())*100)
        error_entry_tab2.delete(0,"end")
        error_entry_tab2.insert(tk.INSERT,error2)

        vol_entry_tab2.configure(state="readonly")
        dro_entry_tab2.configure(state="readonly")
        error_entry_tab2.configure(state="readonly")
#------------------------------------------------------------------------------------
### TABEL TAB 2 ###
    def show_table_nakayasu():
        won=tk.Tk()
        won.title(u"TABEL NAKAYASU")
        won.geometry("400x500")
        lisjudul=["t (s)","Qt (m^3/jam)","Qkoreksi (m^3)"]
        def fconf(self):
            woncanfas.configure(scrollregion=woncanfas.bbox("all"))
        woncanfas=tk.Canvas(won)
        wonframe=tk.Frame(woncanfas)
        scrolly=tk.Scrollbar(won,command=woncanfas.yview)
        woncanfas.configure(yscrollcommand=scrolly.set)
        woncanfas.create_window((4,4),window=wonframe,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas.pack(side="top",fill="both",expand=True)
        wonframe.bind("<Configure>",fconf)
        for i in range(3):
            judul=tk.Entry(wonframe,bg="gray",fg="white")
            judul.grid(row=0,column=i)
            judul.insert(tk.INSERT,lisjudul[i])
        

        for i in range(len(t)):
            a=tk.Entry(wonframe)
            a.grid(row=i+1,column=0)
            a.insert(tk.INSERT,t[i])
            b=tk.Entry(wonframe)
            b.grid(row=i+1,column=1)
            b.insert(tk.INSERT,qt[i])
            c=tk.Entry(wonframe)
            c.grid(row=i+1,column=2)
            c.insert(tk.INSERT,qt_nakayasu_koreksi[i])
        
        

        
        
        ex=pd.DataFrame(
            {
                "t (jam)":t,
                "qt (m3/s)":qt,
                "Vol (m3)":qt
            }
        )
        ex=ex[["t (jam)","qt (m3/s)","Vol (m3)"]]
        ex.to_clipboard(excel=True,index=False)
##############################################    
    def show_table_nakayasu_superposisi():
        won1=tk.Tk()
        won1.title(u"TABEL HIDROGRAF BANJIR NAKAYASU")
        won1.geometry("1300x500")

        def fconf(self):
            woncanfas.configure(scrollregion=woncanfas.bbox("all"))
        woncanfas=tk.Canvas(won1)
        wonframe=tk.Frame(woncanfas)
        scrolly=tk.Scrollbar(won1,command=woncanfas.yview)
        woncanfas.configure(yscrollcommand=scrolly.set)
        woncanfas.create_window((4,4),window=wonframe,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas.pack(side="top",fill="both",expand=True)
        wonframe.bind("<Configure>",fconf)
####################
        R=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
            )
        A=adas_var.get()
        t_nakayasu_superposisi=t[:]
        qt_nakayasu_superposisi=qt_nakayasu_koreksi[:]
        
        
        list1=["t (jam)","Q HSS (m^3/jam)"]
        list2="Tinggi Hujan (mm/jam)"
        list3="Hydrograf Total"
        list4="Volume Hidrograf"
        #header
        for i in range(len(list1)):
                header1=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
                header1.grid(row=0,column=i,rowspan=3,sticky="nesw")
                header1.insert(tk.INSERT,list1[i])
        #tinggi hujan
        header2=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header2.grid(row=0,column=2,columnspan=6,sticky="nesw")
        header2.insert(tk.INSERT,list2)

        #nomor tinggi hujan jam ke
        for i in range(6):
                header3=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header3.grid(row=1,column=i+2,sticky="nesw")
                header3.insert(tk.INSERT,i+1)

        #Tinggi hujan (dari reff)
        for i in range(len(R)):
                header4=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header4.grid(row=2,column=i+2,sticky="nesw")
                header4.insert(tk.INSERT,R[i])
        #head hidrograf total
        header5=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header5.grid(row=0,column=8,rowspan=2,sticky="nesw")
        header5.insert(tk.INSERT,list3)
        #total reff
        header6=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
        header6.grid(row=2,column=8,sticky="nesw")
        header6.insert(tk.INSERT,sum(R))
        #head volume hidrograf
        header7=tk.Entry(wonframe,bg="gray",fg="white",width=18,justify="center")
        header7.grid(row=0,column=9,rowspan=3,sticky="nesw")
        header7.insert(tk.INSERT,list4)

        #pembuatan superposisi kolom
        kolom1=[]
        kolom2=[0]
        kolom3=[0,0]
        kolom4=[0,0,0]
        kolom5=[0,0,0,0]
        kolom6=[0,0,0,0,0]
        for i in range(len(t_nakayasu_superposisi)):
                kolom1.append(qt_nakayasu_superposisi[i]*R[0])
                kolom2.append(qt_nakayasu_superposisi[i]*R[1])
                kolom3.append(qt_nakayasu_superposisi[i]*R[2])
                kolom4.append(qt_nakayasu_superposisi[i]*R[3])
                kolom5.append(qt_nakayasu_superposisi[i]*R[4])
                kolom6.append(qt_nakayasu_superposisi[i]*R[5])
        koloma=kolom1+[0,0,0,0,0]
        kolomb=kolom2+[0,0,0,0]
        kolomc=kolom3+[0,0,0]
        kolomd=kolom4+[0,0]
        kolome=kolom5+[0]
        kolomf=kolom6
        print(len(koloma),len(kolomb),len(kolomc))
        #----------------------------------------------------------
        #QHSS
        for k in range(len(t_nakayasu_superposisi)):
                b=tk.Entry(wonframe)
                b.grid(row=k+3,column=1)
                b.insert(tk.INSERT,qt_nakayasu_superposisi[k])

        #hasil kali reff ke superposisi
        for i in range(len(koloma)):
                c=tk.Entry(wonframe)
                c.grid(row=i+3,column=2)
                c.insert(tk.INSERT,koloma[i])
                d=tk.Entry(wonframe)
                d.grid(row=i+3,column=3)
                d.insert(tk.INSERT,kolomb[i])
                e=tk.Entry(wonframe)
                e.grid(row=i+3,column=4)
                e.insert(tk.INSERT,kolomc[i])
                f=tk.Entry(wonframe)
                f.grid(row=i+3,column=5)
                f.insert(tk.INSERT,kolomd[i])
                g=tk.Entry(wonframe)
                g.grid(row=i+3,column=6)
                g.insert(tk.INSERT,kolome[i])
                h=tk.Entry(wonframe)
                h.grid(row=i+3,column=7)
                h.insert(tk.INSERT,kolomf[i])
        global tsuperp1
        tsuperp1=t_nakayasu_superposisi
        j=t_nakayasu_superposisi[-1]+1
        for k in range(j,j+5):
                tsuperp1.append(k)
        
        #isi waktu
        for i in range(len(tsuperp1)):
                a=tk.Entry(wonframe)
                a.grid(row=i+3,column=0)
                a.insert(tk.INSERT,tsuperp1[i])

        #isi hidrograf total
        global qsuperp1
        qsuperp1=[]
        for i in range (len(koloma)):
                m=tk.Entry(wonframe)
                m.grid(row=i+3,column=8)
                voltabb=koloma[i]+kolomb[i]+kolomc[i]+kolomd[i]+kolome[i]+kolomf[i]
                qsuperp1.append(voltabb)
                m.insert(tk.INSERT,qsuperp1[i])

        vsuperp1=[0]
        for a in range(1,len(kolomc)):
                rumus=0.5*3600*(tsuperp1[a]-tsuperp1[a-1])*(qsuperp1[a]+qsuperp1[a-1])
                
                vsuperp1.append(rumus)

        for b in range(len(vsuperp1)):
                n=tk.Entry(wonframe)
                n.grid(row=b+3,column=9)
                n.insert(tk.INSERT,vsuperp1[b])



        total=sum(vsuperp1)
        tot=tk.Entry(wonframe)
        tot.grid(row=len(vsuperp1)+4,column=9)
        tot.insert(tk.INSERT,total)
        total_teks=tk.Label(wonframe,text="Vol(m3) =")
        total_teks.grid(row=len(vsuperp1)+4,column=8)

        A_teks=tk.Label(wonframe,text="A (km2) =")
        A_teks.grid(row=len(vsuperp1)+5,column=8)
        A_entry=tk.Entry(wonframe)
        A_entry.grid(row=len(vsuperp1)+5,column=9)
        A_entry.insert(tk.INSERT,A)

        Rb=tk.DoubleVar(wonframe,value=(total/A/1000))
        Rb_teks=tk.Label(wonframe,text="R (mm) =")
        Rb_teks.grid(row=len(vsuperp1)+6,column=8)
        Rb_entry=tk.Entry(wonframe,textvariable=Rb)
        Rb_entry.grid(row=len(vsuperp1)+6,column=9)

        persen_teks=tk.Label(wonframe,text="%HDRO")
        persen_teks.grid(row=len(vsuperp1)+7,column=8)
        persen_entry=tk.Entry(wonframe)
        persen_entry.grid(row=len(vsuperp1)+7,column=9)
        persen_entry.insert(tk.INSERT,Rb.get()/sum(R)*100)
        won1.mainloop()
#########################
#------------------------------------------------------------------------------------
### GRAFIK TAB 2 ###
    def show_graph_nakayasu():
        """#Kurva naik (0 < t < Tp)
        qt=[]
        tp=tp1_var.get()
        qp=qp1_var.get()
        t03=t03_var.get()
        #===========================================================
        #Kurva Naik
        awal=0
        akhir=tp
        if round(tp)>tp:
            #Qt
            for x in range(awal,round(akhir),1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            b=(qp*((tp/tp)**2.4))
            qt.append(b)
            #Tp
            t=list(range(round(tp)))
            t.append(tp)

        elif round(tp)<tp:
            #Qt
            for x in range(awal,round(akhir)+1,1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            b=b=(qp*((tp/tp)**2.4))
            qt.append(b)
            #Tp
            t=list(range(round(akhir)+1))
            t.append(tp)

        elif round(tp)==tp:
            #Qt
            for x in range(akhir+1):
                a=(qp*((x/tp)**2.4))
                qt.append(a)
            #Tp
            t=list(range(round(akhir)+1))

        print(t,"\n",qt,"\n")
        #===========================================================
        #Kurva Turun 1
        
        awal=tp
        akhir=tp+t03

        if round(awal)>awal:
            awal=round(round(awal))
        elif round(awal)<awal:
            awal=round(awal)+1
      
        
        if round(akhir)>akhir:
            #qt
            for x in range (awal,round(akhir),1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            b=(qp*((0.3)**((akhir-tp)/t03)))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)))
            t1.append(akhir)
            t=t+t1

        if round(akhir)<akhir:
            for x in range (awal,round(akhir)+1,1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            b=(qp*((0.3)**((akhir-tp)/t03)))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)+1,1))
            t1.append(akhir)
            t=t+t1

        elif round(akhir)==akhir:
            #Qt
            for x in range(awal,akhir+1,1):
                a=(qp*((0.3)**((x-tp)/t03)))
                qt.append(a)
            #Tp
            t1=list(range(akhir+1))
            t=t+t1
            
        print(t,"\n",qt,"\n")


        #===========================================================
    
        awal=tp+t03
        akhir=tp+t03+(1.5*t03)

        if round(awal)>awal:
            awal=round(round(awal))
        elif round(awal)<awal:
            awal=round(awal)+1
        #----------------------------
        if round(akhir)>akhir:
            #qt
            for x in range (awal,round(akhir),1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            b=(qp*((0.3)**(((akhir-tp)+(0.5*t03))/(1.5*t03))))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)))
            t1.append(akhir)
            t=t+t1

        if round(akhir)<akhir:
            for x in range (awal,round(akhir)+1,1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            b=(qp*((0.3)**(((akhir-tp)+(0.5*t03))/(1.5*t03))))
            qt.append(b)
            #Tp
            t1=list(range(awal,round(akhir)+1,1))
            t1.append(akhir)
            t=t+t1

        elif round(akhir)==akhir:
            #Qt
            for x in range(awal,akhir+1,1):
                a=(qp*((0.3)**(((x-tp)+(0.5*t03))/(1.5*t03))))
                qt.append(a)
            #Tp
            t1=list(range(akhir+1))
            t=t+t1
        print(t,"\n",qt,"\n")


        #TURUN 3
        awal=tp+t03+(1.5*t03)
        print (awal)
        if round(awal)>awal:
            awal=round(awal)
        elif round(awal)<awal:
            awal=round(awal)+1
        #----------------------------
        x=awal
        #print(x)
        #print(qp)
                

        while (round(a,3)>0.01): #????????????????????????????????????????????????????????????????????????????
            a=(qp*((0.3)**(((x-tp)+(1.5*t03))/(2*t03))))#x=10319,((x-tp)+(1.5*t03))/(2*t03))=0
            qt.append(a)
            x+=1
        
            
        t1=list(range(awal,x,1))
        t=t+t1
        print(t,"\n",qt,"\n")"""

        
        fig=plt.figure("NAKAYASU")
        ax1=fig.add_subplot(111)
        ax1.plot(t,qt_nakayasu_koreksi,label="Nakayasu")
        ax1.grid(True)
        ax1.set_xlabel("t (jam)")
        ax1.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$") #Q (m^3/s)
        ax1.set_title("GRAFIK HSS METODE NAKAYASU")
#-----------
        ax1.set_ylim(0,qp1_var.get()+2)
        ax2=ax1.twinx()
        ax2.set_ylabel("R (mm)")
        ax2.bar([1],1,color="b",label="Hujan eff (mm)")
        #ax2.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
        #ax2.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
        ax2.set_ylim(qp1_var.get()*2,0)
        ax2.legend()
#-----------
        plt.show()

    def show_graph_nakayasu_superposisi():
        rtot=(
            rtot_kolom11_var_tab1.get(),rtot_kolom21_var_tab1.get(),
            rtot_kolom31_var_tab1.get(),rtot_kolom41_var_tab1.get(),
            rtot_kolom51_var_tab1.get(),rtot_kolom61_var_tab1.get()
        )
        infiltrasi=(
            infil_kolom12_var_tab1.get(),infil_kolom22_var_tab1.get(),
            infil_kolom32_var_tab1.get(),infil_kolom42_var_tab1.get(),
            infil_kolom52_var_tab1.get(),infil_kolom62_var_tab1.get()
            )
        reff=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
        )
        fig=plt.figure("HIDROGRAF BANJIR NAKAYASU")
        ax1=fig.add_subplot(111)
        ax1.plot(tsuperp1,qsuperp1,label="Hidrograf Banjir Nakayasu")
        ax1.grid(True)
        ax1.set_xlabel("t (jam)")
        ax1.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$") #Q (m^3/s)
        ax1.set_title("GRAFIK HIDROGRAF BANJIR NAKAYASU")
        if (hortonfo1_var.get()!=0 or hortonfo2_var.get()!=0 or hortonfc_var.get()!=0 or hortonk_var.get()!=0):
            ax1.set_ylim(0,max(qsuperp1)*2)
            ax2=ax1.twinx()
            ax2.set_ylabel("R (mm)")
            ax2.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
            ax2.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
            ax2.set_ylim((max(rtot)*3),0)
            ax2.legend()
        plt.show()

#------------------------------------------------------------------------------------
### TOMBOL TAB 2 ###
    hitung_tab2=ttk.Button(mighty2,text="HITUNG",width=30,command=hitung_tab2)
    hitung_tab2.grid(row=8,columnspan=5,sticky="W",pady=(20,0))
    tampil_tabel1=ttk.Button(mighty2,text="Tampilkan Tabel",width=30,command=show_table_nakayasu)
    tampil_tabel1.grid(row=9,columnspan=5,sticky="W")
    tampil_grafik1=ttk.Button(mighty2,text="Tampilkan Grafik HSS",width=30,command=show_graph_nakayasu)
    tampil_grafik1.grid(row=10,columnspan=5,sticky="W")
    tampil_superp1=ttk.Button(mighty2,text="Tabel Hidrograf Banjir",width=30,command=show_table_nakayasu_superposisi)
    tampil_superp1.grid(row=11,columnspan=6,sticky="W")
    tampil_superp1_grafik1=ttk.Button(mighty2,text="Grafik Hidrograf Banjir",width=30,command=show_graph_nakayasu_superposisi)
    tampil_superp1_grafik1.grid(row=12,columnspan=5,sticky="W")

#======================================================================================================================================
#ISI TAB 3(SNYDER)
    judul1_tab3=ttk.Label(mighty3,text="DATA",font=judul)
    judul1_tab3.grid(row=0,column=0,columnspan=8,sticky="W",pady=(0,10))
    #------------------------------------------------------------------------------------
    lc_teks_tab3=ttk.Label(mighty3,text="Lc")
    lc_teks_tab3.grid(row=1,column=0,sticky="W")
    lc_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=1,column=1,sticky="W")
    lc_entry=ttk.Entry(mighty3,textvariable=lc_var_tab3)
    lc_entry.grid(row=1,column=2)
    lc_satuan_tab3=ttk.Label(mighty3,text="km")
    lc_satuan_tab3.grid(row=1,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    ct_teks_tab3=ttk.Label(mighty3,text="Ct")
    ct_teks_tab3.grid(row=2,column=0,sticky="W")
    ct_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=2,column=1,sticky="W")
    ct_entry_tab3=ttk.Entry(mighty3,textvariable=ct_var_tab3)
    ct_entry_tab3.grid(row=2,column=2)
    #------------------------------------------------------------------------------------
    cp_teks_tab3=ttk.Label(mighty3,text="Cp")
    cp_teks_tab3.grid(row=3,column=0,sticky="W")
    cp_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=3,column=1,sticky="W")
    cp_entry_tab3=ttk.Entry(mighty3,textvariable=cp_var_tab3)
    cp_entry_tab3.grid(row=3,column=2)
    #------------------------------------------------------------------------------------
    tr_teks_tab3=ttk.Label(mighty3,text="tr")
    tr_teks_tab3.grid(row=4,column=0,sticky="W")
    tr_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=4,column=1,sticky="W")
    tr_entry_tab3=ttk.Entry(mighty3,textvariable=tr_var_tab3)
    tr_entry_tab3.grid(row=4,column=2)
    tr_satuan_tab3=ttk.Label(mighty3,text="jam")
    tr_satuan_tab3.grid(row=4,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    judul2_tab3=ttk.Label(mighty3,text="HASIL PERHITUNGAN",font=judul)
    judul2_tab3.grid(row=5,column=0,columnspan=3,sticky="W",pady=(20,10))
    #------------------------------------------------------------------------------------
    tp_teks_tab3=ttk.Label(mighty3,text="tp")
    tp_teks_tab3.grid(row=6,column=0,sticky="W")
    tp_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=6,column=1,sticky="W")
    tp_entry_tab3=ttk.Entry(mighty3,textvariable=tp_var_tab3,state="readonly")
    tp_entry_tab3.grid(row=6,column=2)
    tp_satuan_tab3=ttk.Label(mighty3,text="jam")
    tp_satuan_tab3.grid(row=6,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    qp_teks_tab3=ttk.Label(mighty3,text="Qp")
    qp_teks_tab3.grid(row=7,column=0,sticky="W")
    qp_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=7,column=1,sticky="W")
    qp_entry_tab3=ttk.Entry(mighty3,textvariable=qp_var_tab3,state="readonly")
    qp_entry_tab3.grid(row=7,column=2)
    qp_satuan_tab3=ttk.Label(mighty3,text=u"m\u00B3/s")
    qp_satuan_tab3.grid(row=7,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    T_teks_tab3=ttk.Label(mighty3,text="T")
    T_teks_tab3.grid(row=8,column=0,sticky="W")
    T_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=8,column=1,sticky="W")
    T_entry_tab3=ttk.Entry(mighty3,textvariable=T_var_tab3,state="readonly")
    T_entry_tab3.grid(row=8,column=2)
    T_satuan_tab3=ttk.Label(mighty3,text="hari")
    T_satuan_tab3.grid(row=8,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tjam_teks_tab3=ttk.Label(mighty3,text="=>")
    tjam_teks_tab3.grid(row=8,column=4,padx=20)
    tjam_var_tab3=tk.DoubleVar()
    tjam_entry_tab3=ttk.Entry(mighty3,textvariable=tjam_var_tab3,state="readonly")
    tjam_entry_tab3.grid(row=8,column=6)
    tjam_satuan_tab3=ttk.Label(mighty3,text="jam")
    tjam_satuan_tab3.grid(row=8,column=7,sticky="W")
    #------------------------------------------------------------------------------------
    td_teks_tab3=ttk.Label(mighty3,text="tD")
    td_teks_tab3.grid(row=9,column=0,sticky="W")
    td_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=9,column=1,sticky="W")
    td_entry_tab3=ttk.Entry(mighty3,textvariable=td_var_tab3,state="readonly")
    td_entry_tab3.grid(row=9,column=2)
    td_satuan_tab3=ttk.Label(mighty3,text="jam")
    td_satuan_tab3.grid(row=9,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tpr_teks_tab3=ttk.Label(mighty3,text="tpR")
    tpr_teks_tab3.grid(row=11,column=0,sticky="W")
    tpr_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=11,column=1,sticky="W")
    tpr_entry_tab3=ttk.Entry(mighty3,textvariable=tpr_var_tab3,state="readonly")
    tpr_entry_tab3.grid(row=11,column=2)
    tpr_satuan_tab3=ttk.Label(mighty3,text="jam")
    tpr_satuan_tab3.grid(row=11,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    qpr_teks_tab3=ttk.Label(mighty3,text="QpR")
    qpr_teks_tab3.grid(row=12,column=0,sticky="W")
    qpr_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=12,column=1,sticky="W")
    qpr_entry_tab3=ttk.Entry(mighty3,textvariable=qpr_var_tab3,state="readonly")
    qpr_entry_tab3.grid(row=12,column=2)
    qpr_satuan_tab3=ttk.Label(mighty3,text=u"m\u00B3/s")
    qpr_satuan_tab3.grid(row=12,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    pr_teks_tab3=ttk.Label(mighty3,text="Pr")
    pr_teks_tab3.grid(row=13,column=0,sticky="W")
    pr_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=13,column=1,sticky="W")
    pr_entry_tab3=ttk.Entry(mighty3,textvariable=pr_var_tab3,state="readonly")
    pr_entry_tab3.grid(row=13,column=2)
    pr_satuan_tab3=ttk.Label(mighty3,text="jam")
    pr_satuan_tab3.grid(row=13,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    w50_teks_tab3=ttk.Label(mighty3,text="W50")
    w50_teks_tab3.grid(row=14,column=0,sticky="W")
    w50_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=14,column=1,sticky="W")
    w50_entry_tab3=ttk.Entry(mighty3,textvariable=w50_var_tab3,state="readonly")
    w50_entry_tab3.grid(row=14,column=2)
    w50_satuan_tab3=ttk.Label(mighty3,text="jam")
    w50_satuan_tab3.grid(row=14,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    w75_teks_tab3=ttk.Label(mighty3,text="W75")
    w75_teks_tab3.grid(row=15,column=0,sticky="W")
    w75_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=15,column=1,sticky="W")
    w75_entry_tab3=ttk.Entry(mighty3,textvariable=w75_var_tab3,state="readonly")
    w75_entry_tab3.grid(row=15,column=2)
    w75_satuan_tab3=ttk.Label(mighty3,text="jam")
    w75_satuan_tab3.grid(row=15,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    vol_hss_tab3=ttk.Label(mighty3,text="Vol HSS")
    vol_hss_tab3.grid(row=13,column=4,sticky="W",padx=(20,10))
    vol_hss_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=13,column=5,sticky="W")
    vol_hss_entry_tab3=ttk.Entry(mighty3,textvariable=vol_hss_var_tab3,state="readonly")
    vol_hss_entry_tab3.grid(row=13,column=6,padx=5)
    vol_hss_satuan=ttk.Label(mighty3,text=u"m\u00B3")
    vol_hss_satuan.grid(row=13,column=7,sticky="W")
    #------------------------------------------------------------------------------------
    dro_teks_tab3=ttk.Label(mighty3,text="DRO")
    dro_teks_tab3.grid(row=14,column=4,sticky="W",padx=(20,10))
    dro_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=14,column=5,sticky="W")
    dro_entry_tab3=ttk.Entry(mighty3,textvariable=dro_var_tab3,state="readonly")
    dro_entry_tab3.grid(row=14,column=6)
    #------------------------------------------------------------------------------------
    error_teks_tab3=ttk.Label(mighty3,text="error")
    error_teks_tab3.grid(row=15,column=4,sticky="W",padx=(20,10))
    error_var_tab3=tk.DoubleVar()
    samad_tab3=ttk.Label(mighty3,text="=")
    samad_tab3.grid(row=15,column=5,sticky="W")
    error_entry_tab3=ttk.Entry(mighty3,textvariable=error_var_tab3,state="readonly")
    error_entry_tab3.grid(row=15,column=6)
    error_satuan_tab3=ttk.Label(mighty3,text="%")
    error_satuan_tab3.grid(row=15,column=7,sticky="W")
#======================================================================================================================================
    def hitung_snyder():
        tp_entry_tab3.configure(state="normal")
        qp_entry_tab3.configure(state="normal")
        T_entry_tab3.configure(state="normal")
        td_entry_tab3.configure(state="normal")
        tpr_entry_tab3.configure(state="normal")
        qpr_entry_tab3.configure(state="normal")
        pr_entry_tab3.configure(state="normal")
        w50_entry_tab3.configure(state="normal")
        w75_entry_tab3.configure(state="normal")
        tjam_entry_tab3.configure(state="normal")
        vol_hss_entry_tab3.configure(state="normal")
        dro_entry_tab3.configure(state="normal")
        error_entry_tab3.configure(state="normal")

        tp_tab3=ct_var_tab3.get()*(((lsungai_var.get()*lc_var_tab3.get()))**0.3)
        tp_entry_tab3.delete(0,"end")
        tp_entry_tab3.insert(tk.INSERT,tp_tab3)

        qp_tab3=((cp_var_tab3.get()*adas_var.get())/tp_var_tab3.get())
        qp_entry_tab3.delete(0,"end")
        qp_entry_tab3.insert(tk.INSERT,qp_tab3)

        T_tab3=3+(tp_var_tab3.get()/8)
        T_entry_tab3.delete(0,"end")
        T_entry_tab3.insert(tk.INSERT,T_tab3)
        
        tjam_tab3=T_var_tab3.get()*24
        tjam_entry_tab3.delete(0,"end")
        tjam_entry_tab3.insert(tk.INSERT,tjam_tab3)

        td_tab3=tp_var_tab3.get()/5.5
        td_entry_tab3.delete(0,"end")
        td_entry_tab3.insert(tk.INSERT,td_tab3)

        if tr_var_tab3.get()!=td_var_tab3.get():
            tpr_tab3=tp_var_tab3.get()+((0.25)*(tr_var_tab3.get()-td_var_tab3.get()))
            tpr_entry_tab3.delete(0,"end")
            tpr_entry_tab3.insert(tk.INSERT,tpr_tab3)
            
            qpr_tab3=qp_var_tab3.get()*(tp_var_tab3.get()/tpr_var_tab3.get())
            qpr_entry_tab3.delete(0,"end")
            qpr_entry_tab3.insert(tk.INSERT,qpr_tab3)
        
            tp_hitung_tab3=tpr_var_tab3.get()
            qp_hitung_tab3=qpr_var_tab3.get()

        elif (tr_var_tab3.get()==td_var_tab3.get()):
            tp_hitung_tab3=tp_var_tab3.get()
            qp_hitung_tab3=qp_var_tab3.get()

        pr_tab3=(tr_var_tab3.get()/2)+tp_hitung_tab3
        pr_entry_tab3.delete(0,"end")
        pr_entry_tab3.insert(tk.INSERT,pr_tab3)

        w50_tab3=(0.23*(adas_var.get()**1.08))/(qp_hitung_tab3**1.08)
        w50_entry_tab3.delete(0,"end")
        w50_entry_tab3.insert(tk.INSERT,w50_tab3)

        w75_tab3=(0.13*(adas_var.get()**1.08))/(qp_hitung_tab3**1.08)
        w75_entry_tab3.delete(0,"end")
        w75_entry_tab3.insert(tk.INSERT,w75_tab3)

        tp_entry_tab3.configure(state="readonly")
        qp_entry_tab3.configure(state="readonly")
        T_entry_tab3.configure(state="readonly")
        td_entry_tab3.configure(state="readonly")
        tpr_entry_tab3.configure(state="readonly")
        qpr_entry_tab3.configure(state="readonly")
        pr_entry_tab3.configure(state="readonly")
        w50_entry_tab3.configure(state="readonly")
        w75_entry_tab3.configure(state="readonly")
        tjam_entry_tab3.configure(state="readonly")

#t dan qp
        global t_tab3
        global qt_tab3
        global volhss3
        global qt_snyder_koreksi


        t_tab3=[0]
        qt_tab3=[0]
        qt_snyder_koreksi=[]
        volhss3=[0]
        vll_snyder_koreksi=[]
        #-----------------
        t2_tab3=tp_hitung_tab3-((1/3)*w50_var_tab3.get())
        t3_tab3=tp_hitung_tab3-((1/3)*w75_var_tab3.get())
        t4_tab3=tp_hitung_tab3
        t5_tab3=tp_hitung_tab3+((2/3)*w75_var_tab3.get())
        t6_tab3=tp_hitung_tab3+((2/3)*w50_var_tab3.get())
        t7_tab3=tjam_var_tab3.get()
        #-----------------
        qt2_tab3=(50/100)*qp_hitung_tab3
        qt3_tab3=(75/100)*qp_hitung_tab3
        qt4_tab3=qp_hitung_tab3
        qt5_tab3=qt3_tab3
        qt6_tab3=qt2_tab3
        qt7_tab3=0

        time=1
        while (time<t2_tab3):
            t_tab3.append(time)
            debit=0-(((0-time)*(0-qt2_tab3))/(0-t2_tab3)) #(time/t2_tab3)*qt2_tab3
            qt_tab3.append(debit)
            time+=1
        t_tab3.append(t2_tab3)
        qt_tab3.append(qt2_tab3)

        if(round(t2_tab3)==t2_tab3):
            time=t2_tab3+1
        elif(round(t2_tab3)>t2_tab3):
            time=round(t2_tab3)
        elif(round(t2_tab3)<t2_tab3):
            time=time=round(t2_tab3)+1
        while(time<t3_tab3):
            t_tab3.append(time)
            debit=qt2_tab3-(((t2_tab3-time)*(qt2_tab3-qt3_tab3))/(t2_tab3-t3_tab3))
            qt_tab3.append(debit)
            time+=1
        t_tab3.append(t3_tab3)
        qt_tab3.append(qt3_tab3)

        if(round(t3_tab3)==t3_tab3):
            time=t3_tab3+1
        elif(round(t3_tab3)>t3_tab3):
            time=round(t3_tab3)
        elif(round(t3_tab3)<t3_tab3):
            time=round(t3_tab3)+1
        while(time<t4_tab3):
            t_tab3.append(time)
            debit=qt3_tab3-(((t3_tab3-time)*(qt3_tab3-qt4_tab3))/(t3_tab3-t4_tab3))
            qt_tab3.append(debit)
            time+=1
        t_tab3.append(t4_tab3)
        qt_tab3.append(qt4_tab3)

        if(round(t4_tab3)==t4_tab3):
            time=t4_tab3+1
        elif(round(t4_tab3)>t4_tab3):
            time=round(t4_tab3)
        elif(round(t4_tab3)<t4_tab3):
            time=round(t4_tab3)+1
        while(time<t5_tab3):
            t_tab3.append(time)
            debit=qt4_tab3-(((t4_tab3-time)*(qt4_tab3-qt5_tab3))/(t4_tab3-t5_tab3))
            qt_tab3.append(debit)
            time+=1
        t_tab3.append(t5_tab3)
        qt_tab3.append(qt5_tab3)

        if(round(t5_tab3)==t5_tab3):
            time=t5_tab3+1
        elif(round(t5_tab3)>t5_tab3):
            time=round(t5_tab3)
        elif(round(t5_tab3)<t5_tab3):
            time=round(t5_tab3)+1
        while(time<t6_tab3):
            t_tab3.append(time)
            debit=qt5_tab3-(((t5_tab3-time)*(qt5_tab3-qt6_tab3))/(t5_tab3-t6_tab3))
            qt_tab3.append(debit)
            time+=1
        t_tab3.append(t6_tab3)
        qt_tab3.append(qt6_tab3)

        if(round(t6_tab3)==t6_tab3):
            time=t6_tab3+1
        elif(round(t6_tab3)>t6_tab3):
            time=round(t6_tab3)
        elif(round(t6_tab3)<t6_tab3):
            time=round(t6_tab3)+1
        while(debit>0):
            debit=qt6_tab3-(((t6_tab3-time)*(qt6_tab3-qt7_tab3))/(t6_tab3-t7_tab3))
            if(debit>0):
                qt_tab3.append(debit)
                t_tab3.append(time)
            time+=1
        t_tab3.append(t7_tab3)
        qt_tab3.append(qt7_tab3)
        
        #Volume HSS
        qtot_snyder=sum(qt_tab3)
        vll_snyder=qtot_snyder*60*60
        
        #DRO
        dro_snyder=(vll_snyder/(adas_var.get()*10**6))*1000
        
        #Qt koreksi
        for i in range(len(t_tab3)):
            qt_snyder_koreksi.append(qt_tab3[i]/dro_snyder)
        
        #volume koreksi
        vll_snyder_koreksi=sum(qt_snyder_koreksi*60*60)
        
        #dro koreksi
        dro_snyder_koreksi=(vll_snyder_koreksi/(adas_var.get()*10**6))*1000

        #Menampilkan volhss dan dro ke entry
        vol_hss_entry_tab3.delete(0,"end")
        vol_hss_entry_tab3.insert(tk.INSERT,round(vll_snyder_koreksi))

        dro_entry_tab3.delete(0,"end")
        dro_entry_tab3.insert(tk.INSERT,round(dro_snyder_koreksi))

        error3=round(((abs(dro_snyder_koreksi-1))/1)*100)
        error_entry_tab3.delete(0,"end")
        error_entry_tab3.insert(tk.INSERT,error3)

        vol_hss_entry_tab3.configure(state="readonly")
        dro_entry_tab3.configure(state="readonly")
        error_entry_tab3.configure(state="readonly")
#
#TABEL SNYDER
    def tabel_snyder():
        won3=tk.Tk()
        won3.title(u"TABEL SNYDER")
        won3.geometry("400x500")
        lisjudul=["t (s)","Qt (m^3/s)","Qkoreksi (m^3)"]
        def fconf(self):
            woncanfas3.configure(scrollregion=woncanfas3.bbox("all"))
        woncanfas3=tk.Canvas(won3)
        wonframe3=tk.Frame(woncanfas3)
        scrolly=tk.Scrollbar(won3,command=woncanfas3.yview)
        woncanfas3.configure(yscrollcommand=scrolly.set)
        woncanfas3.create_window((4,4),window=wonframe3,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas3.pack(side="top",fill="both",expand=True)
        wonframe3.bind("<Configure>",fconf)
        for i in range(3):
            judul=tk.Entry(wonframe3,bg="gray",fg="white",justify="center")
            judul.grid(row=0,column=i)
            judul.insert(tk.INSERT,lisjudul[i])

        for i in range(len(t_tab3)):
            a=tk.Entry(wonframe3)
            a.grid(row=i+1,column=0)
            a.insert(tk.INSERT,t_tab3[i])
            b=tk.Entry(wonframe3)
            b.grid(row=i+1,column=1)
            b.insert(tk.INSERT,qt_tab3[i])
            c=tk.Entry(wonframe3)
            c.grid(row=i+1,column=2)
            c.insert(tk.INSERT,qt_snyder_koreksi[i])
#            
    def tabel_snyder_superposisi():
        won1=tk.Tk()
        won1.title(u"TABEL HIDROGRAF BANJIR SNYDER")
        won1.geometry("1300x500")


        def fconf(self):
                woncanfas.configure(scrollregion=woncanfas.bbox("all"))
        woncanfas=tk.Canvas(won1)
        wonframe=tk.Frame(woncanfas)
        scrolly=tk.Scrollbar(won1,command=woncanfas.yview)
        woncanfas.configure(yscrollcommand=scrolly.set)
        woncanfas.create_window((4,4),window=wonframe,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas.pack(side="top",fill="both",expand=True)
        wonframe.bind("<Configure>",fconf)

        t=t_tab3[:]
        qt_snyder_superposisi=qt_snyder_koreksi[:]
        R=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
            )
        A=adas_var.get()

        list1=["t (jam)","Q HSS (m^3/jam)"]
        list2="Tinggi Hujan (mm/jam)"
        list3="Hydrograf Total"
        list4="Volume Hidrograf"
        #header
        for i in range(len(list1)):
                header1=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
                header1.grid(row=0,column=i,rowspan=3,sticky="nesw")
                header1.insert(tk.INSERT,list1[i])
        #tinggi hujan
        header2=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header2.grid(row=0,column=2,columnspan=6,sticky="nesw")
        header2.insert(tk.INSERT,list2)

        #nomor tinggi hujan jam ke
        for i in range(6):
                header3=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header3.grid(row=1,column=i+2,sticky="nesw")
                header3.insert(tk.INSERT,i+1)

        #Tinggi hujan (dari reff)
        for i in range(len(R)):
                header4=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header4.grid(row=2,column=i+2,sticky="nesw")
                header4.insert(tk.INSERT,R[i])
        #head hidrograf total
        header5=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header5.grid(row=0,column=8,rowspan=2,sticky="nesw")
        header5.insert(tk.INSERT,list3)
        #total reff
        header6=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
        header6.grid(row=2,column=8,sticky="nesw")
        header6.insert(tk.INSERT,sum(R))
        #head volume hidrograf
        header7=tk.Entry(wonframe,bg="gray",fg="white",width=18,justify="center")
        header7.grid(row=0,column=9,rowspan=3,sticky="nesw")
        header7.insert(tk.INSERT,list4)

        #pembuatan superposisi kolom
        kolom1=[]
        kolom2=[0]
        kolom3=[0,0]
        kolom4=[0,0,0]
        kolom5=[0,0,0,0]
        kolom6=[0,0,0,0,0]
        for i in range(len(t)):
                kolom1.append(qt_snyder_superposisi[i]*R[0])
                kolom2.append(qt_snyder_superposisi[i]*R[1])
                kolom3.append(qt_snyder_superposisi[i]*R[2])
                kolom4.append(qt_snyder_superposisi[i]*R[3])
                kolom5.append(qt_snyder_superposisi[i]*R[4])
                kolom6.append(qt_snyder_superposisi[i]*R[5])
        koloma=kolom1+[0,0,0,0,0]
        kolomb=kolom2+[0,0,0,0]
        kolomc=kolom3+[0,0,0]
        kolomd=kolom4+[0,0]
        kolome=kolom5+[0]
        kolomf=kolom6
        #----------------------------------------------------------
        #QHSS
        for k in range(len(t)):
                b=tk.Entry(wonframe)
                b.grid(row=k+3,column=1)
                b.insert(tk.INSERT,qt_snyder_superposisi[k])

        #hasil kali reff ke superposisi
        for i in range(len(koloma)):
                c=tk.Entry(wonframe)
                c.grid(row=i+3,column=2)
                c.insert(tk.INSERT,koloma[i])
                d=tk.Entry(wonframe)
                d.grid(row=i+3,column=3)
                d.insert(tk.INSERT,kolomb[i])
                e=tk.Entry(wonframe)
                e.grid(row=i+3,column=4)
                e.insert(tk.INSERT,kolomc[i])
                f=tk.Entry(wonframe)
                f.grid(row=i+3,column=5)
                f.insert(tk.INSERT,kolomd[i])
                g=tk.Entry(wonframe)
                g.grid(row=i+3,column=6)
                g.insert(tk.INSERT,kolome[i])
                h=tk.Entry(wonframe)
                h.grid(row=i+3,column=7)
                h.insert(tk.INSERT,kolomf[i])
        global tsuperp2
        tsuperp2=t[:]
        j=t[-1]+1
        j=round(j)
        for k in range(j,j+5):
                tsuperp2.append(k)

        #isi waktu
        for i in range(len(tsuperp2)):
                a=tk.Entry(wonframe)
                a.grid(row=i+3,column=0)
                a.insert(tk.INSERT,tsuperp2[i])

        #isi hidrograf total
        global qsuperp2
        qsuperp2=[]
        for i in range (len(koloma)):
                m=tk.Entry(wonframe)
                m.grid(row=i+3,column=8)
                voltabb=koloma[i]+kolomb[i]+kolomc[i]+kolomd[i]+kolome[i]+kolomf[i]
                qsuperp2.append(voltabb)
                m.insert(tk.INSERT,qsuperp2[i])

        vsuperp2=[0]
        for a in range(1,len(kolomc)):
                rumus=0.5*3600*(tsuperp2[a]-tsuperp2[a-1])*(qsuperp2[a]+qsuperp2[a-1])
                vsuperp2.append(rumus)

        for b in range(len(vsuperp2)):
                n=tk.Entry(wonframe)
                n.grid(row=b+3,column=9)
                n.insert(tk.INSERT,vsuperp2[b])



        total=sum(vsuperp2)
        tot=tk.Entry(wonframe)
        tot.grid(row=len(vsuperp2)+4,column=9)
        tot.insert(tk.INSERT,total)
        total_teks=tk.Label(wonframe,text="Vol(m3) =")
        total_teks.grid(row=len(vsuperp2)+4,column=8)

        A_teks=tk.Label(wonframe,text="A (km2) =")
        A_teks.grid(row=len(vsuperp2)+5,column=8)
        A_entry=tk.Entry(wonframe)
        A_entry.grid(row=len(vsuperp2)+5,column=9)
        A_entry.insert(tk.INSERT,A)

        Rb=tk.DoubleVar(wonframe,value=(total/A/1000))
        Rb_teks=tk.Label(wonframe,text="R (mm) =")
        Rb_teks.grid(row=len(vsuperp2)+6,column=8)
        Rb_entry=tk.Entry(wonframe,textvariable=Rb)
        Rb_entry.grid(row=len(vsuperp2)+6,column=9)

        persen_teks=tk.Label(wonframe,text="%HDRO")
        persen_teks.grid(row=len(vsuperp2)+7,column=8)
        persen_entry=tk.Entry(wonframe)
        persen_entry.grid(row=len(vsuperp2)+7,column=9)
        persen_entry.insert(tk.INSERT,Rb.get()/sum(R)*100)


#GRAFIK SNYDER
    def grafik_snyder():

        fig=plt.figure("SNYDER")
        ax12=fig.add_subplot(111)
        ax12.plot(t_tab3,qt_snyder_koreksi)#,marker='o', linestyle='-')
        ax12.grid(True)
        ax12.set_xlabel("t (jam)")
        ax12.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
        ax12.set_title("GRAFIK HSS METODE SNYDER")
#-------------
        ax12.set_ylim(0,qp_var_tab3.get()+2)
        ax22=ax12.twinx()
        ax22.set_ylabel("R (mm)")
        ax22.bar([1],1,color="b",label="Hujan eff (mm)")
        #ax22.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
        #ax22.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
        ax22.set_ylim((qp_var_tab3.get()*2),0)
        ax22.legend()
        plt.show()

############
    def grafik_snyder_superposisi():
        rtot=(
            rtot_kolom11_var_tab1.get(),rtot_kolom21_var_tab1.get(),
            rtot_kolom31_var_tab1.get(),rtot_kolom41_var_tab1.get(),
            rtot_kolom51_var_tab1.get(),rtot_kolom61_var_tab1.get()
        )
        infiltrasi=(
            infil_kolom12_var_tab1.get(),infil_kolom22_var_tab1.get(),
            infil_kolom32_var_tab1.get(),infil_kolom42_var_tab1.get(),
            infil_kolom52_var_tab1.get(),infil_kolom62_var_tab1.get()
            )
        reff=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
        )

        fig=plt.figure("HIDROGRAF BANJIR SNYDER")
        ax12=fig.add_subplot(111)
        ax12.plot(tsuperp2,qsuperp2)#,marker='o', linestyle='-')
        ax12.grid(True)
        ax12.set_xlabel("t (jam)")
        ax12.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
        ax12.set_title("GRAFIK HIDROGRAF BANJIR SNYDER")
        if (hortonfo1_var.get()!=0 or hortonfo2_var.get()!=0 or hortonfc_var.get()!=0 or hortonk_var.get()!=0):
            ax12.set_ylim(0,max(qsuperp2)*2)
            ax22=ax12.twinx()
            ax22.set_ylabel("R (mm)")
            ax22.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
            ax22.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
            ax22.set_ylim((max(rtot)*2),0)
            ax22.legend()
        plt.show()

#------------------------------------------------------------------------------------
#TOMBOL
    hitung_tab3=ttk.Button(mighty3,width=30,text="HITUNG",command=hitung_snyder)
    hitung_tab3.grid(row=16,columnspan=5,sticky="W",pady=(20,0))
    tabel_tab3=ttk.Button(mighty3,width=30,text="Tampilkan Tabel",command=tabel_snyder)
    tabel_tab3.grid(row=17,columnspan=5,sticky="W")
    grafik_tab3=ttk.Button(mighty3,width=30,text="Tampilkan Grafik HSS",command=grafik_snyder)
    grafik_tab3.grid(row=18,columnspan=5,sticky="W")
    superp2_tab3=ttk.Button(mighty3,width=30,text="Tabel Hidrograf Banjir",command=tabel_snyder_superposisi)
    superp2_tab3.grid(row=19,columnspan=6,sticky="W")
    grafik_superp2_tab3=ttk.Button(mighty3,width=30,text="Grafik Hidrograf Banjir",command=grafik_snyder_superposisi)
    grafik_superp2_tab3.grid(row=20,columnspan=6,sticky="W")
#======================================================================================================================================
#ISI TAB 4(SCS)
    #------------------------------------------------------------------------------------
    judul1_tab4=ttk.Label(mighty4,text="DATA",font=judul)
    judul1_tab4.grid(row=0,column=0,columnspan=8,pady=(0,10),sticky="W")
    #------------------------------------------------------------------------------------
    ct_teks_tab4=ttk.Label(mighty4,text="Ct")
    ct_teks_tab4.grid(row=1,column=0,sticky="W")
    ct_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=1,column=1,sticky="W")
    ct_entry_tab4=ttk.Entry(mighty4,textvariable=ct_var_tab4)
    ct_entry_tab4.grid(row=1,column=2,padx=10,pady=5)
    #------------------------------------------------------------------------------------
    tr_teks_tab4=ttk.Label(mighty4,text="tr")
    tr_teks_tab4.grid(row=2,column=0,sticky="W")
    tr_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=2,column=1,sticky="W")
    tr_entry_tab4=ttk.Entry(mighty4,textvariable=tr_var_tab4)
    tr_entry_tab4.grid(row=2,column=2,padx=10,pady=5)
    tr_satuan_tab4=ttk.Label(mighty4,text="jam")
    tr_satuan_tab4.grid(row=2,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tb_tp_teks_tab4=ttk.Label(mighty4,text="TB/Tp")
    tb_tp_teks_tab4.grid(row=3,column=0,sticky="W")
    tb_tp_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=3,column=1,sticky="W")
    tb_tp_entry_tab4=ttk.Entry(mighty4,textvariable=tb_tp_var_tab4)
    tb_tp_entry_tab4.grid(row=3,column=2,padx=10,pady=5)
    #------------------------------------------------------------------------------------
    judul2_tab4=ttk.Label(mighty4,text="HASIL PERHITUNGAN",font=judul)
    judul2_tab4.grid(row=4,column=0,columnspan=8,pady=(20,10),sticky="W")
    #------------------------------------------------------------------------------------
    lc_teks_tab4=ttk.Label(mighty4,text="Lc")
    lc_teks_tab4.grid(row=5,column=0,sticky="W")
    lc_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=5,column=1,sticky="W")
    lc_entry_tab4=ttk.Entry(mighty4,textvariable=lc_var_tab4,state="readonly")
    lc_entry_tab4.grid(row=5,column=2,padx=10,pady=5)
    lc_satuan_tab4=ttk.Label(mighty4,text="km")
    lc_satuan_tab4.grid(row=5,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tp_teks_tab4=ttk.Label(mighty4,text="tp")
    tp_teks_tab4.grid(row=6,column=0,sticky="W")
    tp_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=6,column=1,sticky="W")
    tp_entry_tab4=ttk.Entry(mighty4,textvariable=tp_var_tab4,state="readonly")
    tp_entry_tab4.grid(row=6,column=2,padx=10,pady=5)
    tp_satuan_tab4=ttk.Label(mighty4,text="jam")
    tp_satuan_tab4.grid(row=6,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tpu_teks_tab4=ttk.Label(mighty4,text="Tp")
    tpu_teks_tab4.grid(row=7,column=0,sticky="W")
    tpu_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=7,column=1,sticky="W")
    tpu_entry_tab4=ttk.Entry(mighty4,textvariable=tpu_var_tab4,state="readonly")
    tpu_entry_tab4.grid(row=7,column=2,padx=10,pady=5)
    tpu_satuan_tab4=ttk.Label(mighty4,text="jam")
    tpu_satuan_tab4.grid(row=7,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    pr_teks_tab4=ttk.Label(mighty4,text="pr")
    pr_teks_tab4.grid(row=8,column=0,sticky="W")
    pr_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=8,column=1,sticky="W")
    pr_entry_tab4=ttk.Entry(mighty4,textvariable=pr_var_tab4,state="readonly")
    pr_entry_tab4.grid(row=8,column=2,padx=10,pady=5)
    pr_satuan_tab4=ttk.Label(mighty4,text="jam")
    pr_satuan_tab4.grid(row=8,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    qp_teks_tab4=ttk.Label(mighty4,text="Qp")
    qp_teks_tab4.grid(row=9,column=0,sticky="W")
    qp_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=9,column=1,sticky="W")
    qp_entry_tab4=ttk.Entry(mighty4,textvariable=qp_var_tab4,state="readonly")
    qp_entry_tab4.grid(row=9,column=2,padx=10,pady=5)
    qp_satuan_tab4=ttk.Label(mighty4,text=u"m\u00B3/s")
    qp_satuan_tab4.grid(row=9,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    tb_teks_tab4=ttk.Label(mighty4,text="TB")
    tb_teks_tab4.grid(row=10,column=0,sticky="W")
    tb_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=10,column=1,sticky="W")
    tb_entry_tab4=ttk.Entry(mighty4,textvariable=tb_var_tab4,state="readonly")
    tb_entry_tab4.grid(row=10,column=2,padx=10,pady=5)
    tb_satuan_tab4=ttk.Label(mighty4,text=u"m\u00B3/s")
    tb_satuan_tab4.grid(row=10,column=3,sticky="W")
    #------------------------------------------------------------------------------------
    volhss_teks_tab4=ttk.Label(mighty4,text="Vol. HSS")
    volhss_teks_tab4.grid(row=5,column=4,sticky="W",padx=20)
    volhss_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=5,column=5,sticky="W")
    volhss_entry_tab4=ttk.Entry(mighty4,textvariable=volhss_var_tab4,state="readonly")
    volhss_entry_tab4.grid(row=5,column=6,padx=10,pady=5)
    volhss_satuan_tab4=ttk.Label(mighty4,text=u"m\u00B3")
    volhss_satuan_tab4.grid(row=5,column=7,sticky="W")
    #------------------------------------------------------------------------------------
    dro_teks_tab4=ttk.Label(mighty4,text="DRO")
    dro_teks_tab4.grid(row=6,column=4,sticky="W",padx=20)
    dro_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=6,column=5,sticky="W")
    dro_entry_tab4=ttk.Entry(mighty4,textvariable=dro_var_tab4,state="readonly")
    dro_entry_tab4.grid(row=6,column=6,padx=10,pady=5)
    #------------------------------------------------------------------------------------
    error_teks_tab4=ttk.Label(mighty4,text="error")
    error_teks_tab4.grid(row=7,column=4,sticky="W",padx=20)
    error_var_tab4=tk.DoubleVar()
    samad_tab4=ttk.Label(mighty4,text="=")
    samad_tab4.grid(row=7,column=5,sticky="W")
    error_entry_tab4=ttk.Entry(mighty4,textvariable=error_var_tab4,state="readonly")
    error_entry_tab4.grid(row=7,column=6,padx=10,pady=5)
    error_satuan_tab4=ttk.Label(mighty4,text="%")
    error_satuan_tab4.grid(row=7,column=7,sticky="W")
#------------------------------------------------------------------------------------
#Hitung SCS
#Hitung SCS Bagian 1 (variabel)
    def hitung_scs():
        lc_entry_tab4.configure(state="normal")
        tp_entry_tab4.configure(state="normal")
        tpu_entry_tab4.configure(state="normal")
        pr_entry_tab4.configure(state="normal")
        qp_entry_tab4.configure(state="normal")
        tb_entry_tab4.configure(state="normal")
        volhss_entry_tab4.configure(state="normal")
        dro_entry_tab4.configure(state="normal")
        error_entry_tab4.configure(state="normal")
        
        #Lc
        lc_entry_tab4.delete(0,"end")
        lc=0.5*lsungai_var.get()
        lc_entry_tab4.insert(tk.INSERT,lc)

        #tp
        tp_entry_tab4.delete(0,"end")
        tp=(ct_var_tab4.get()*((lsungai_var.get()*lc_var_tab4.get())**0.3))
        tp_entry_tab4.insert(tk.INSERT,tp)

        #Tp
        tpu_entry_tab4.delete(0,"end")
        tpu=tp_var_tab4.get()+(0.5*tr_var_tab4.get())
        tpu_entry_tab4.insert(tk.INSERT,tpu)

        #pr
        pr_entry_tab4.delete(0,"end")
        pr=(tr_var_tab4.get()/2)+tp_var_tab4.get()
        pr_entry_tab4.insert(tk.INSERT,pr)
        print(pr)

        #Qp
        qp_entry_tab4.delete(0,"end")
        qp=(0.208*adas_var.get())/pr_var_tab4.get()
        qp_entry_tab4.insert(tk.INSERT,qp)

        #TB
        tb_entry_tab4.delete(0,"end")
        tb=tb_tp_var_tab4.get()*tpu_var_tab4.get()
        tb_entry_tab4.insert(tk.INSERT,tb)

    
        lc_entry_tab4.configure(state="readonly")
        tp_entry_tab4.configure(state="readonly")
        tpu_entry_tab4.configure(state="readonly")
        pr_entry_tab4.configure(state="readonly")
        qp_entry_tab4.configure(state="readonly")
        tb_entry_tab4.configure(state="readonly")
#------------------------------------------------------------------------------------
#Hitung SCS Bagian 2 (t dan Q)
        global t
        global ttp
        global Q
        global qt_scs_koreksi
        global rasio
        global qkecil
        global V
        t=[]
        i=0
        ttp=[]
        qkecil=[]
        rasio=[]
        Q=[]
        qt_scs_koreksi=[]
        V=[0]
        Tp=tpu_var_tab4.get()
        tbtp=tb_tp_var_tab4.get()
        
        if round(Tp)==Tp:
            while (i<Tp+1):
                t.append(i)
                ttp_hitung=i/Tp
                ttp.append(ttp_hitung)
                i+=1
        elif round(Tp)<Tp:
            while (i<Tp):
                t.append(i)
                ttp_hitung=i/Tp
                ttp.append(ttp_hitung)
                i+=1
            t.append(Tp)
            ttp.append(Tp/Tp)
        elif round(Tp)>Tp:
            while (i<Tp):
                t.append(i)
                ttp_hitung=i/Tp
                ttp.append(ttp_hitung)
                i+=1
            t.append(Tp)
            ttp.append(Tp/Tp)

        while ((i/Tp)<tbtp):
            t.append(i)
            ttp.append(i/Tp)
            i+=1

        t.append(tb_var_tab4.get())#agar lebih dari tbtp 1x karena walaupun menghasilkan q dan Q 0 namun V ada
        ttp.append(tb_var_tab4.get()/Tp)
        
        #=====================#
        a=([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.5,4.0,4.5,5.0])
        b=([0,0.015,0.075,0.16,0.28,0.43,0.60,0.77,0.89,0.97,1.0,0.98,0.92,0.84,0.75,0.66,0.56,0.42,0.32,0.24,0.18,0.13,0.098,0.075,0.036,0.018,0.009,0.004])
        c=([0.15,0.6,0.85,1.2,1.5,1.7,1.7,1.2,0.8,0.3,-0.2,-0.6,-0.8,-0.9,-0.9,-1,-0.7,-0.5,-0.4,-0.3,-0.25,-0.16,-0.115,-0.078,-0.036,-0.018,-0.01,0.0008])
        #=====================#
        for p in ttp:
            #for p in ttp: #nilai ttp di perhitungan t awal
            if(p in a): #nilai list a
                q=b[a.index(p)] #q berisi isi di list b yg index sama seperti index p di list a
                qkecil.append(q) #list qkecil bertambah dari index ke 0
                r=c[a.index(p)]#Rasio dicari tanpa rumus (-)/(-) karena udah ada di list
                rasio.append(r)
                Qhitung=q*qp
                Q.append(Qhitung)


            elif(p>a[len(a)-1]): #kondisi saat t/tp lebih besar dari t/Tp di list a index terakhir
                #interpolasi dibawah tidak usah digunakan karena tidak perlu mencari di luar itu
                """    batas_bawah=len(a)-2
                batas_atas=len(a)-1
                x1=a[batas_bawah]
                y1=b[batas_bawah]
                x2=a[batas_atas]
                y2=b[batas_atas]
                q=(y1-(((x1-p)*(y1-y2))/(x1-x2)))"""
                q=0
                r=0
                qkecil.append(q)
                rasio.append(r)
                Qhitung=0
                Q.append(Qhitung)

            else:
                for i in a: #p=0.15
                    if (i<p):#setelah looping didapatkan i = 0.1
                        x1=i
                        y1=b[a.index(x1)]
                        x2=a[a.index(x1)+1]
                        y2=b[a.index(x2)]
                        q=(y1-(((x1-p)*(y1-y2))/(x1-x2))) #q/qp sudah ketemu saat tidak ada di kategori "di dalam" dan "di luar" dengan interpolasi
                        r=c[a.index(i)]
                qkecil.append(q) #Penting
                rasio.append(r)
                Qhitung=(q*qp)
                Q.append(Qhitung)


        #volume
        qtot_scs=sum(Q)
        vll_scs=qtot_scs*60*60


        #DRO
        dro_scs=(vll_scs/(adas_var.get()*10**6))*1000
        
        #qt koreksi
        for i in range(len(t)):
            qt_scs_koreksi.append(Q[i]/dro_scs)
        
        #volume koreksi
        vll_scs_koreksi=sum(qt_scs_koreksi)*60*60

        #dro koreksi
        dro_scs_koreksi=(vll_scs_koreksi/(adas_var.get()*10**6))*1000

        

        #input sum volume hss dan dro
        
        volhss_entry_tab4.delete(0,"end")
        volhss_entry_tab4.insert(tk.INSERT,round(vll_scs_koreksi))

        dro_entry_tab4.delete(0,"end")
        dro_entry_tab4.insert(tk.INSERT,round(dro_scs_koreksi))

        error_entry_tab4.delete(0,"end")
        error_entry_tab4.insert(tk.INSERT,round((abs(dro_scs_koreksi-1)/1)*100))

        volhss_entry_tab4.configure(state="readonly")
        dro_entry_tab4.configure(state="readonly")
        error_entry_tab4.configure(state="readonly")
#------------------------------------------------------------------------------------
#FUNGSI SCS
    def tabel_scs():
        won2=tk.Tk()
        won2.title(u"TABEL SCS")
        won2.geometry("650x500")
        lisjudul=["t (s)","t/Tp","q","Q (m3/s)","Qkoreksi(m2/s)"]
        def fconf(self):
            woncanfas2.configure(scrollregion=woncanfas2.bbox("all"))
        woncanfas2=tk.Canvas(won2)
        wonframe2=tk.Frame(woncanfas2)
        scrolly=tk.Scrollbar(won2,command=woncanfas2.yview)
        woncanfas2.configure(yscrollcommand=scrolly.set)
        woncanfas2.create_window((4,4),window=wonframe2,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas2.pack(side="top",fill="both",expand=True)
        wonframe2.bind("<Configure>",fconf)
        for i in range(5):
            judul=tk.Entry(wonframe2,bg="gray",fg="white",justify="center")
            judul.grid(row=0,column=i)
            judul.insert(tk.INSERT,lisjudul[i])

        for i in range(len(t)):
            a=tk.Entry(wonframe2)
            a.grid(row=i+1,column=0)
            a.insert(tk.INSERT,t[i])
            b=tk.Entry(wonframe2)
            b.grid(row=i+1,column=1)
            b.insert(tk.INSERT,ttp[i])
            c=tk.Entry(wonframe2)
            c.grid(row=i+1,column=2)
            c.insert(tk.INSERT,qkecil[i])
            d=tk.Entry(wonframe2)
            d.grid(row=i+1,column=3)
            d.insert(tk.INSERT,Q[i])
            e=tk.Entry(wonframe2)
            e.grid(row=i+1,column=4)
            e.insert(tk.INSERT,qt_scs_koreksi[i])

    def tabel_scs_superposisi():
        t_scs_superposisi=t[:]
        qt_scs_superposisi=qt_scs_koreksi[:]
        R=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
            )
        A=adas_var.get()
        


        won1=tk.Tk()
        won1.title(u"TABEL HIDROGRAF BANJIR SCS")
        won1.geometry("1300x500")


        def fconf(self):
                woncanfas.configure(scrollregion=woncanfas.bbox("all"))
        woncanfas=tk.Canvas(won1)
        wonframe=tk.Frame(woncanfas)
        scrolly=tk.Scrollbar(won1,command=woncanfas.yview)
        woncanfas.configure(yscrollcommand=scrolly.set)
        woncanfas.create_window((4,4),window=wonframe,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas.pack(side="top",fill="both",expand=True)
        wonframe.bind("<Configure>",fconf)

        list1=["t (jam)","Q HSS (m^3/jam)"]
        list2="Tinggi Hujan (mm/jam)"
        list3="Hydrograf Total"
        list4="Volume Hidrograf"
        #header
        for i in range(len(list1)):
                header1=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
                header1.grid(row=0,column=i,rowspan=3,sticky="nesw")
                header1.insert(tk.INSERT,list1[i])
        #tinggi hujan
        header2=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header2.grid(row=0,column=2,columnspan=6,sticky="nesw")
        header2.insert(tk.INSERT,list2)

        #nomor tinggi hujan jam ke
        for i in range(6):
                header3=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header3.grid(row=1,column=i+2,sticky="nesw")
                header3.insert(tk.INSERT,i+1)

        #Tinggi hujan (dari reff)
        for i in range(len(R)):
                header4=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header4.grid(row=2,column=i+2,sticky="nesw")
                header4.insert(tk.INSERT,R[i])
        #head hidrograf total
        header5=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header5.grid(row=0,column=8,rowspan=2,sticky="nesw")
        header5.insert(tk.INSERT,list3)
        #total reff
        header6=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
        header6.grid(row=2,column=8,sticky="nesw")
        header6.insert(tk.INSERT,sum(R))
        #head volume hidrograf
        header7=tk.Entry(wonframe,bg="gray",fg="white",width=18,justify="center")
        header7.grid(row=0,column=9,rowspan=3,sticky="nesw")
        header7.insert(tk.INSERT,list4)

        #pembuatan superposisi kolom
        kolom1=[]
        kolom2=[0]
        kolom3=[0,0]
        kolom4=[0,0,0]
        kolom5=[0,0,0,0]
        kolom6=[0,0,0,0,0]
        for i in range(len(t_scs_superposisi)):
                kolom1.append(qt_scs_superposisi[i]*R[0])
                kolom2.append(qt_scs_superposisi[i]*R[1])
                kolom3.append(qt_scs_superposisi[i]*R[2])
                kolom4.append(qt_scs_superposisi[i]*R[3])
                kolom5.append(qt_scs_superposisi[i]*R[4])
                kolom6.append(qt_scs_superposisi[i]*R[5])
        koloma=kolom1+[0,0,0,0,0]
        kolomb=kolom2+[0,0,0,0]
        kolomc=kolom3+[0,0,0]
        kolomd=kolom4+[0,0]
        kolome=kolom5+[0]
        kolomf=kolom6
        print(len(koloma),len(kolomb),len(kolomc))
        #----------------------------------------------------------
        #QHSS
        for k in range(len(t_scs_superposisi)):
                b=tk.Entry(wonframe)
                b.grid(row=k+3,column=1)
                b.insert(tk.INSERT,qt_scs_superposisi[k])

        #hasil kali reff ke superposisi
        for i in range(len(koloma)):
                c=tk.Entry(wonframe)
                c.grid(row=i+3,column=2)
                c.insert(tk.INSERT,koloma[i])
                d=tk.Entry(wonframe)
                d.grid(row=i+3,column=3)
                d.insert(tk.INSERT,kolomb[i])
                e=tk.Entry(wonframe)
                e.grid(row=i+3,column=4)
                e.insert(tk.INSERT,kolomc[i])
                f=tk.Entry(wonframe)
                f.grid(row=i+3,column=5)
                f.insert(tk.INSERT,kolomd[i])
                g=tk.Entry(wonframe)
                g.grid(row=i+3,column=6)
                g.insert(tk.INSERT,kolome[i])
                h=tk.Entry(wonframe)
                h.grid(row=i+3,column=7)
                h.insert(tk.INSERT,kolomf[i])

        global tsuperp3
        tsuperp3=t_scs_superposisi
        j=int(t_scs_superposisi[-1])+1 #membuat t index terakhir roundown berapapun
        print(j)
        for k in range(j,j+5):
                tsuperp3.append(k)

        #isi waktu
        for i in range(len(tsuperp3)):
                a=tk.Entry(wonframe)
                a.grid(row=i+3,column=0)
                a.insert(tk.INSERT,tsuperp3[i])

        #isi hidrograf total
        global qsuperp3
        qsuperp3=[]
        for i in range (len(koloma)):
                m=tk.Entry(wonframe)
                m.grid(row=i+3,column=8)
                voltabb=koloma[i]+kolomb[i]+kolomc[i]+kolomd[i]+kolome[i]+kolomf[i]
                qsuperp3.append(voltabb)
                m.insert(tk.INSERT,qsuperp3[i])

        vsuperp3=[0]
        for a in range(1,len(kolomc)):
                rumus=0.5*3600*(tsuperp3[a]-tsuperp3[a-1])*(qsuperp3[a]+qsuperp3[a-1])
                vsuperp3.append(rumus)

        for b in range(len(vsuperp3)):
                n=tk.Entry(wonframe)
                n.grid(row=b+3,column=9)
                n.insert(tk.INSERT,vsuperp3[b])



        total=sum(vsuperp3)
        tot=tk.Entry(wonframe)
        tot.grid(row=len(vsuperp3)+4,column=9)
        tot.insert(tk.INSERT,total)
        total_teks=tk.Label(wonframe,text="Vol(m3) =")
        total_teks.grid(row=len(vsuperp3)+4,column=8)

        A_teks=tk.Label(wonframe,text="A (km2) =")
        A_teks.grid(row=len(vsuperp3)+5,column=8)
        A_entry=tk.Entry(wonframe)
        A_entry.grid(row=len(vsuperp3)+5,column=9)
        A_entry.insert(tk.INSERT,A)

        Rb=tk.DoubleVar(wonframe,value=(total/A/1000))
        Rb_teks=tk.Label(wonframe,text="R (mm) =")
        Rb_teks.grid(row=len(vsuperp3)+6,column=8)
        Rb_entry=tk.Entry(wonframe,textvariable=Rb)
        Rb_entry.grid(row=len(vsuperp3)+6,column=9)

        persen_teks=tk.Label(wonframe,text="%HDRO")
        persen_teks.grid(row=len(vsuperp3)+7,column=8)
        persen_entry=tk.Entry(wonframe)
        persen_entry.grid(row=len(vsuperp3)+7,column=9)
        persen_entry.insert(tk.INSERT,Rb.get()/sum(R)*100)
    
    def grafik_scs():
        fig=plt.figure("SCS")
        ax13=fig.add_subplot(111)
        ax13.plot(t,qt_scs_koreksi)
        ax13.grid(True)
        ax13.set_xlabel("t (jam)")
        ax13.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
        ax13.set_title("GRAFIK HSS METODE SCS")
#-------------    
        ax13.set_ylim(0,qp_var_tab4.get()+2)
        ax23=ax13.twinx()
        ax23.set_ylabel("R (mm)")
        ax23.bar([1],1,color="b",label="Hujan eff (mm)")
        #ax23.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
        #ax23.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
        ax23.set_ylim((qp_var_tab4.get()*2),0)
        ax23.legend()
        plt.show()

    def grafik_scs_superposisi():
        rtot=(
            rtot_kolom11_var_tab1.get(),rtot_kolom21_var_tab1.get(),
            rtot_kolom31_var_tab1.get(),rtot_kolom41_var_tab1.get(),
            rtot_kolom51_var_tab1.get(),rtot_kolom61_var_tab1.get()
        )
        infiltrasi=(
            infil_kolom12_var_tab1.get(),infil_kolom22_var_tab1.get(),
            infil_kolom32_var_tab1.get(),infil_kolom42_var_tab1.get(),
            infil_kolom52_var_tab1.get(),infil_kolom62_var_tab1.get()
            )
        reff=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
        )


        fig=plt.figure("HIDROGRAF BANJIR SCS")
        ax13=fig.add_subplot(111)
        ax13.plot(tsuperp3,qsuperp3)
        ax13.grid(True)
        ax13.set_xlabel("t (jam)")
        ax13.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
        ax13.set_title("GRAFIK HIDROGRAF BANJIR SCS")
        if (hortonfo1_var.get()!=0 or hortonfo2_var.get()!=0 or hortonfc_var.get()!=0 or hortonk_var.get()!=0):
            ax13.set_ylim(0,max(qsuperp3)*2)
            ax23=ax13.twinx()
            ax23.set_ylabel("R (mm)")
            ax23.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
            ax23.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
            ax23.set_ylim((max(rtot)*3),0)
            ax23.legend()
        plt.show()
#------------------------------------------------------------------------------------
#TOMBOL SCS
    hitung_tab4=ttk.Button(mighty4,width=30,text="HITUNG",command=hitung_scs)
    hitung_tab4.grid(row=15,columnspan=5,sticky="W",pady=(20,0))
    tabel_tab4=ttk.Button(mighty4,width=30,text="Tampilkan Tabel",command=tabel_scs)
    tabel_tab4.grid(row=16,columnspan=5,sticky="W")
    grafik_tab4=ttk.Button(mighty4,width=30,text="Tampilkan Grafik HSS",command=grafik_scs)
    grafik_tab4.grid(row=17,columnspan=5,sticky="W")
    tabel_tab4_superposisi=ttk.Button(mighty4,width=30,text="Tabel Hidrograf Banjir",command=tabel_scs_superposisi)
    tabel_tab4_superposisi.grid(row=18,columnspan=5,sticky="W")
    grafik_tab4_superposisi=ttk.Button(mighty4,width=30,text="Grafik Hidrograf Banjir",command=grafik_scs_superposisi)
    grafik_tab4_superposisi.grid(row=19,columnspan=5,sticky="W")
#======================================================================================================================================
#ISI TAB 5(GAMA - 1)
    judul1_tab5=ttk.Label(mighty5,text="DATA",font=judul)
    judul1_tab5.grid(row=0,column=0,columnspan=8,pady=(0,10),sticky="W")
    #-------------------------------------------------------------------------------------
    l1_teks_tab5=ttk.Label(mighty5,text=u"\u2211 Panjang sungai 1")
    l1_teks_tab5.grid(row=1,column=0,sticky="W")
    l1_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=1,column=1,sticky="W")
    l1_entry_tab5=ttk.Entry(mighty5,textvariable=l1_var_tab5)
    l1_entry_tab5.grid(row=1,column=2)
    l1_satuan_tab5=ttk.Label(mighty5,text="km")
    l1_satuan_tab5.grid(row=1,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    l2_teks_tab5=ttk.Label(mighty5,text=u"\u2211 Panjang sungai semua")
    l2_teks_tab5.grid(row=2,column=0,sticky="W")
    l2_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=2,column=1,sticky="W")
    l2_entry_tab5=ttk.Entry(mighty5,textvariable=l2_var_tab5)
    l2_entry_tab5.grid(row=2,column=2)
    l2_satuan_tab5=ttk.Label(mighty5,text="km")
    l2_satuan_tab5.grid(row=2,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    p1_teks_tab5=ttk.Label(mighty5,text=u"\u2211 Pangsa sungai 1")
    p1_teks_tab5.grid(row=3,column=0,sticky="W")
    p1_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=3,column=1,sticky="W")
    p1_entry_tab5=ttk.Entry(mighty5,textvariable=p1_var_tab5)
    p1_entry_tab5.grid(row=3,column=2)
    #-------------------------------------------------------------------------------------
    p2_teks_tab5=ttk.Label(mighty5,text=u"\u2211 Pangsa sungai semua")
    p2_teks_tab5.grid(row=4,column=0,sticky="W")
    p2_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=4,column=1,sticky="W")
    p2_entry_tab5=ttk.Entry(mighty5,textvariable=p2_var_tab5)
    p2_entry_tab5.grid(row=4,column=2)
    #-------------------------------------------------------------------------------------
    jn_teks_tab5=ttk.Label(mighty5,text=u"\u2211 Pertemuan sungai (JN)")
    jn_teks_tab5.grid(row=5,column=0,sticky="W")
    jn_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=5,column=1,sticky="W")
    jn_entry_tab5=ttk.Entry(mighty5,textvariable=jn_var_tab5)
    jn_entry_tab5.grid(row=5,column=2)
    #-------------------------------------------------------------------------------------
    wl_teks_tab5=ttk.Label(mighty5,text="WL")
    wl_teks_tab5.grid(row=1,column=4,sticky="W",padx=(20,0))
    wl_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=1,column=5,sticky="W")
    wl_entry_tab5=ttk.Entry(mighty5,textvariable=wl_var_tab5)
    wl_entry_tab5.grid(row=1,column=6)
    wl_satuan_tab5=ttk.Label(mighty5,text="km")
    wl_satuan_tab5.grid(row=1,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    wu_teks_tab5=ttk.Label(mighty5,text="Wu")
    wu_teks_tab5.grid(row=2,column=4,sticky="W",padx=(20,0))
    wu_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=2,column=5,sticky="W")
    wu_entry_tab5=ttk.Entry(mighty5,textvariable=wu_var_tab5)
    wu_entry_tab5.grid(row=2,column=6)
    wu_satuan_tab5=ttk.Label(mighty5,text="km")
    wu_satuan_tab5.grid(row=2,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    au_teks_tab5=ttk.Label(mighty5,text="AU")
    au_teks_tab5.grid(row=3,column=4,sticky="W",padx=(20,0))
    au_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=3,column=5,sticky="W")
    au_entry_tab5=ttk.Entry(mighty5,textvariable=au_var_tab5)
    au_entry_tab5.grid(row=3,column=6)
    au_satuan_tab5=ttk.Label(mighty5,text=u"km\u00B2")
    au_satuan_tab5.grid(row=3,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    s_teks_tab5=ttk.Label(mighty5,text="S")
    s_teks_tab5.grid(row=4,column=4,sticky="W",padx=(20,0))
    s_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=4,column=5,sticky="W")
    s_entry_tab5=ttk.Entry(mighty5,textvariable=s_var_tab5)
    s_entry_tab5.grid(row=4,column=6)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #===========================================================================================
    judul2_tab5=ttk.Label(mighty5,text="HASIL PERHITUNGAN",font=judul)
    judul2_tab5.grid(row=10,column=0,columnspan=8,pady=(20,10),sticky="W")
    #-------------------------------------------------------------------------------------
    d_teks_tab5=ttk.Label(mighty5,text="D")
    d_teks_tab5.grid(row=11,column=0,sticky="W")
    d_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=11,column=1,sticky="W")
    d_entry_tab5=ttk.Entry(mighty5,textvariable=d_var_tab5,state="readonly")
    d_entry_tab5.grid(row=11,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    sf_teks_tab5=ttk.Label(mighty5,text="SF")
    sf_teks_tab5.grid(row=12,column=0,sticky="W")
    sf_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=12,column=1,sticky="W")
    sf_entry_tab5=ttk.Entry(mighty5,textvariable=sf_var_tab5,state="readonly")
    sf_entry_tab5.grid(row=12,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    sn_teks_tab5=ttk.Label(mighty5,text="SN")
    sn_teks_tab5.grid(row=13,column=0,sticky="W")
    sn_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=13,column=1,sticky="W")
    sn_entry_tab5=ttk.Entry(mighty5,textvariable=sn_var_tab5,state="readonly")
    sn_entry_tab5.grid(row=13,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    wf_teks_tab5=ttk.Label(mighty5,text="WF")
    wf_teks_tab5.grid(row=14,column=0,sticky="W")
    wf_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=14,column=1,sticky="W")
    wf_entry_tab5=ttk.Entry(mighty5,textvariable=wf_var_tab5,state="readonly")
    wf_entry_tab5.grid(row=14,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    rua_teks_tab5=ttk.Label(mighty5,text="RUA")
    rua_teks_tab5.grid(row=15,column=0,sticky="W")
    rua_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=15,column=1,sticky="W")
    rua_entry_tab5=ttk.Entry(mighty5,textvariable=rua_var_tab5,state="readonly")
    rua_entry_tab5.grid(row=15,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    sim_teks_tab5=ttk.Label(mighty5,text="SIM")
    sim_teks_tab5.grid(row=16,column=0,sticky="W")
    sim_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=16,column=1,sticky="W")
    sim_entry_tab5=ttk.Entry(mighty5,textvariable=sim_var_tab5,state="readonly")
    sim_entry_tab5.grid(row=16,column=2)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    tr_teks_tab5=ttk.Label(mighty5,text="TR")
    tr_teks_tab5.grid(row=17,column=0,sticky="W")
    tr_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=17,column=1,sticky="W")
    tr_entry_tab5=ttk.Entry(mighty5,textvariable=tr_var_tab5,state="readonly")
    tr_entry_tab5.grid(row=17,column=2)
    tr_satuan_tab5=ttk.Label(mighty5,text="jam")
    tr_satuan_tab5.grid(row=17,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    qp_teks_tab5=ttk.Label(mighty5,text="QP")
    qp_teks_tab5.grid(row=18,column=0,sticky="W")
    qp_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=18,column=1,sticky="W")
    qp_entry_tab5=ttk.Entry(mighty5,textvariable=qp_var_tab5,state="readonly")
    qp_entry_tab5.grid(row=18,column=2)
    qp_satuan_tab5=ttk.Label(mighty5,text=u"m\u00B3/s")
    qp_satuan_tab5.grid(row=18,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    tb_teks_tab5=ttk.Label(mighty5,text="TB")
    tb_teks_tab5.grid(row=11,column=4,sticky="W",padx=(20,0))
    tb_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=11,column=5,sticky="W")
    tb_entry_tab5=ttk.Entry(mighty5,textvariable=tb_var_tab5,state="readonly")
    tb_entry_tab5.grid(row=11,column=6)
    tb_satuan_tab5=ttk.Label(mighty5,text="jam")
    tb_satuan_tab5.grid(row=11,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    k_teks_tab5=ttk.Label(mighty5,text="K")
    k_teks_tab5.grid(row=12,column=4,sticky="W",padx=(20,0))
    k_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=12,column=5,sticky="W")
    k_entry_tab5=ttk.Entry(mighty5,textvariable=k_var_tab5,state="readonly")
    k_entry_tab5.grid(row=12,column=6)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W")
    #-------------------------------------------------------------------------------------
    qb_teks_tab5=ttk.Label(mighty5,text="QB")
    qb_teks_tab5.grid(row=13,column=4,sticky="W",padx=(20,0))
    qb_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=13,column=5,sticky="W")
    qb_entry_tab5=ttk.Entry(mighty5,textvariable=qb_var_tab5,state="readonly")
    qb_entry_tab5.grid(row=13,column=6)
    qb_satuan_tab5=ttk.Label(mighty5,text=u"m\u00B3/s")
    qb_satuan_tab5.grid(row=13,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    phi_teks_tab5=ttk.Label(mighty5,text=u"\u03A6")
    phi_teks_tab5.grid(row=14,column=4,sticky="W",padx=(20,0))
    phi_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=14,column=5,sticky="W")
    phi_entry_tab5=ttk.Entry(mighty5,textvariable=phi_var_tab5,state="readonly")
    phi_entry_tab5.grid(row=14,column=6)
    phi_satuan_tab5=ttk.Label(mighty5,text="mm/jam")
    phi_satuan_tab5.grid(row=14,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    V_teks_tab5=ttk.Label(mighty5,text="V.HSS")
    V_teks_tab5.grid(row=15,column=4,sticky="W",padx=(20,0))
    V_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=15,column=5,sticky="W")
    V_entry_tab5=ttk.Entry(mighty5,textvariable=V_var_tab5,state="readonly")
    V_entry_tab5.grid(row=15,column=6)
    V_satuan_tab5=ttk.Label(mighty5,text=u"m\u00B3")
    V_satuan_tab5.grid(row=15,column=7,sticky="W")
    #-------------------------------------------------------------------------------------
    dro_teks_tab5=ttk.Label(mighty5,text="DRO")
    dro_teks_tab5.grid(row=16,column=4,sticky="W",padx=(20,0))
    dro_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=16,column=5,sticky="W")
    dro_entry_tab5=ttk.Entry(mighty5,textvariable=dro_var_tab5,state="readonly")
    dro_entry_tab5.grid(row=16,column=6)
    #tetha_satuan_tab5=ttk.Label(mighty5,text="km^2")
    #tetha_satuan_tab5.grid(row=9,column=3,sticky="W)
    #-------------------------------------------------------------------------------------
    error_teks_tab5=ttk.Label(mighty5,text="error")
    error_teks_tab5.grid(row=17,column=4,sticky="W",padx=(20,0))
    error_var_tab5=tk.DoubleVar()
    samad_tab5=ttk.Label(mighty5,text="=")
    samad_tab5.grid(row=17,column=5,sticky="W")
    error_entry_tab5=ttk.Entry(mighty5,textvariable=error_var_tab5,state="readonly")
    error_entry_tab5.grid(row=17,column=6)
    error_satuan_tab5=ttk.Label(mighty5,text="%")
    error_satuan_tab5.grid(row=17,column=7,sticky="W")
#-------------------------------------------------------------------------------------
#FUNGSI
#Hitung Bagian 1
    def hitung_gama():
        d_entry_tab5.configure(state="normal")
        sf_entry_tab5.configure(state="normal")
        sn_entry_tab5.configure(state="normal")
        wf_entry_tab5.configure(state="normal")
        rua_entry_tab5.configure(state="normal")
        sim_entry_tab5.configure(state="normal")
        tr_entry_tab5.configure(state="normal")
        qp_entry_tab5.configure(state="normal")
        tb_entry_tab5.configure(state="normal")
        k_entry_tab5.configure(state="normal")
        qb_entry_tab5.configure(state="normal")
        phi_entry_tab5.configure(state="normal")
        V_entry_tab5.configure(state="normal")
        dro_entry_tab5.configure(state="normal")
        error_entry_tab5.configure(state="normal")

        #D
        d_entry_tab5.delete(0,"end")
        d_tab5=l2_var_tab5.get()/adas_var.get()
        d_entry_tab5.insert(tk.INSERT,d_tab5)
        #SF
        sf_entry_tab5.delete(0,"end")
        sf_tab5=l1_var_tab5.get()/l2_var_tab5.get()
        sf_entry_tab5.insert(tk.INSERT,sf_tab5)
        #SN
        sn_entry_tab5.delete(0,"end")
        sn_tab5=p1_var_tab5.get()/p2_var_tab5.get()
        sn_entry_tab5.insert(tk.INSERT,sn_tab5)
        #WF
        wf_entry_tab5.delete(0,"end")
        wf_tab5=wu_var_tab5.get()/wl_var_tab5.get()
        wf_entry_tab5.insert(tk.INSERT,wf_tab5)
        #RUA
        rua_entry_tab5.delete(0,"end")
        rua_tab5=au_var_tab5.get()/adas_var.get()
        rua_entry_tab5.insert(tk.INSERT,rua_tab5)
        #SIM
        sim_entry_tab5.delete(0,"end")
        sim_tab5=wf_var_tab5.get()*rua_var_tab5.get()
        sim_entry_tab5.insert(tk.INSERT,sim_tab5)
        #TR
        tr_entry_tab5.delete(0,"end")
        tr_tab5=(0.43*((lsungai_var.get()/(100*sf_var_tab5.get()))**3))+(1.0665*sim_var_tab5.get())+1.2775
        tr_entry_tab5.insert(tk.INSERT,tr_tab5)
        #QP
        qp_entry_tab5.delete(0,"end")
        qp_tab5=0.1836*((adas_var.get())**0.5886)*((tr_var_tab5.get())**(-0.4008))*((jn_var_tab5.get())**0.2381)
        qp_entry_tab5.insert(tk.INSERT,qp_tab5)
        #TB
        tb_entry_tab5.delete(0,"end")
        tb_tab5=27.4132*((tr_var_tab5.get())**0.1457)*((s_var_tab5.get())**(-0.0986))*((sn_var_tab5.get())**0.7344)*((rua_var_tab5.get())**0.2574)
        tb_entry_tab5.insert(tk.INSERT,tb_tab5)
        #K
        k_entry_tab5.delete(0,"end")
        k_tab5=0.5617*((adas_var.get())**0.1798)*((s_var_tab5.get())**(-0.1446))*((sf_var_tab5.get())**(-1.0897))*(d_var_tab5.get()**(0.0452))
        k_entry_tab5.insert(tk.INSERT,k_tab5)
        #QB
        qb_entry_tab5.delete(0,"end")
        qb_tab5=0.4715*((adas_var.get())**0.6444)*((d_var_tab5.get())**0.9430)
        qb_entry_tab5.insert(tk.INSERT,qb_tab5)
        #PHI
        phi_entry_tab5.delete(0,"end")
        phi_tab5=10.4903-((3.859*((10)**(-6)))*((adas_var.get())**2))+((1.6985*(10**(-13)))*((adas_var.get()/sn_var_tab5.get())**4))
        phi_entry_tab5.insert(tk.INSERT,phi_tab5)

        d_entry_tab5.configure(state="readonly")
        sf_entry_tab5.configure(state="readonly")
        sn_entry_tab5.configure(state="readonly")
        wf_entry_tab5.configure(state="readonly")
        rua_entry_tab5.configure(state="readonly")
        sim_entry_tab5.configure(state="readonly")
        tr_entry_tab5.configure(state="readonly")
        qp_entry_tab5.configure(state="readonly")
        tb_entry_tab5.configure(state="readonly")
        k_entry_tab5.configure(state="readonly")
        qb_entry_tab5.configure(state="readonly")
        phi_entry_tab5.configure(state="readonly")
#
#Hitung Bagian2(Qt)
        global qt_tab5
        global qt_gama_koreksi
        global t_tab5
        global v_tab5
        adas5=adas_var.get()
        qt_tab5=[0]
        qt_gama_koreksi=[]
        v_tab5=[0]

        tr_tab5=tr_var_tab5.get()
        qp5=qp_var_tab5.get()
        k_tab5=k_var_tab5.get()
        tb_tab5=tb_var_tab5.get()

        awal_tab5=1
        akhir_tab5=tr_tab5

        if round(akhir_tab5)==akhir_tab5:
            for x in range(awal_tab5,round(akhir_tab5)+1,1):
                #qt
                a=(x/tr_tab5)*qp5
                qt_tab5.append(a)
                #t
                t_tab5=list(range(len(qt_tab5)))


        elif round(akhir_tab5)<akhir_tab5:
            for x in range(awal_tab5,round(akhir_tab5)+1):
                #qt
                a=(x/tr_tab5)*qp5
                qt_tab5.append(a)
            b=(tr_tab5/tr_tab5)*qp5
            qt_tab5.append(b)
            #t
            t_tab5=list(range(len(qt_tab5)-1))
            t_tab5.append(tr_tab5)


        elif round(akhir_tab5)>akhir_tab5:
            for x in range(awal_tab5,round(akhir_tab5)):
                #qt
                a=(x/tr_tab5)*qp5
                qt_tab5.append(a)
            b=(tr_tab5/tr_tab5)*qp5
            qt_tab5.append(b)
            #t
            t_tab5=list(range(len(qt_tab5)-1))
            t_tab5.append(tr_tab5)



        if round(tr_tab5)>tr_tab5:
            awal=round(tr_tab5)
        elif round(tr_tab5)<tr_tab5:
            awal=round(tr_tab5)+1
        #----------------------------
        x=awal
        while (x<tb_tab5):
            a=(math.exp((-x)/k_tab5))*qp5
            qt_tab5.append(a)
            t_tab5.append(x)
            x+=1
        qt_tab5.append((math.exp((-tb_tab5)/k_tab5))*qp5)
        t_tab5.append(tb_tab5)

        #volume
        qtot_gama=sum(qt_tab5)
        vll_gama=qtot_gama*60*60

        #dro
        dro_gama=(vll_gama/(adas_var.get()*10**6))*1000

        #qt koreksi
        for i in range(len(t_tab5)):
            qt_gama_koreksi.append(qt_tab5[i]/dro_gama)

        #volume koreksi
        vll_gama_koreksi=sum(qt_gama_koreksi)*60*60

        #dro koreksi
        dro_gama_koreksi=(vll_gama_koreksi/(adas_var.get()*10**6))*1000

        V_entry_tab5.delete(0,"end")
        V_entry_tab5.insert(tk.INSERT,round(vll_gama_koreksi))

        dro_entry_tab5.delete(0,"end")
        dro_entry_tab5.insert(tk.INSERT,round(dro_gama_koreksi))

        error_entry_tab5.delete(0,"end")
        error_entry_tab5.insert(tk.INSERT,(round(abs(dro_gama_koreksi-1)/1))*100)

        V_entry_tab5.configure(state="readonly")
        dro_entry_tab5.configure(state="readonly")
        error_entry_tab5.configure(state="readonly")
#

    def tabel_gama():
        won5=tk.Tk()
        won5.title(u"TABEL GAMA - 1")
        won5.geometry("400x500")
        lisjudul=["t (s)","Qt (m^3/s)","Qkoreksi (m^3)"]
        def fconf5(self):
            woncanfas5.configure(scrollregion=woncanfas5.bbox("all"))
        woncanfas5=tk.Canvas(won5)
        wonframe5=tk.Frame(woncanfas5)
        scrolly=tk.Scrollbar(won5,command=woncanfas5.yview)
        woncanfas5.configure(yscrollcommand=scrolly.set)
        woncanfas5.create_window((4,4),window=wonframe5,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas5.pack(side="top",fill="both",expand=True)
        wonframe5.bind("<Configure>",fconf5)
        for i in range(3):
            judul=tk.Entry(wonframe5,bg="gray",fg="white",justify="center")
            judul.grid(row=0,column=i)
            judul.insert(tk.INSERT,lisjudul[i])

        for i in range(len(t_tab5)):
            a=tk.Entry(wonframe5)
            a.grid(row=i+1,column=0)
            a.insert(tk.INSERT,t_tab5[i])
            b=tk.Entry(wonframe5)
            b.grid(row=i+1,column=1)
            b.insert(tk.INSERT,qt_tab5[i])
            c=tk.Entry(wonframe5)
            c.grid(row=i+1,column=2)
            c.insert(tk.INSERT,qt_gama_koreksi[i])
            
    def tabel_gama_superposisi():
        t_gama_superposisi=t_tab5[:]
        qt_gama_superposisi=qt_gama_koreksi[:]

        R=(
            reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
            reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
            reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
            )
        A=adas_var.get()


        won1=tk.Tk()
        won1.title(u"TABEL HIDROGRAF BANJIR GAMA 1")
        won1.geometry("1300x500")


        def fconf(self):
                woncanfas.configure(scrollregion=woncanfas.bbox("all"))
        woncanfas=tk.Canvas(won1)
        wonframe=tk.Frame(woncanfas)
        scrolly=tk.Scrollbar(won1,command=woncanfas.yview)
        woncanfas.configure(yscrollcommand=scrolly.set)
        woncanfas.create_window((4,4),window=wonframe,anchor="nw")
        scrolly.pack(side="left",fill="y")
        woncanfas.pack(side="top",fill="both",expand=True)
        wonframe.bind("<Configure>",fconf)

        list1=["t (jam)","Q HSS (m^3/jam)"]
        list2="Tinggi Hujan (mm/jam)"
        list3="Hydrograf Total"
        list4="Volume Hidrograf"
        #header
        for i in range(len(list1)):
                header1=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
                header1.grid(row=0,column=i,rowspan=3,sticky="nesw")
                header1.insert(tk.INSERT,list1[i])
        #tinggi hujan
        header2=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header2.grid(row=0,column=2,columnspan=6,sticky="nesw")
        header2.insert(tk.INSERT,list2)

        #nomor tinggi hujan jam ke
        for i in range(6):
                header3=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header3.grid(row=1,column=i+2,sticky="nesw")
                header3.insert(tk.INSERT,i+1)

        #Tinggi hujan (dari reff)
        for i in range(len(R)):
                header4=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
                header4.grid(row=2,column=i+2,sticky="nesw")
                header4.insert(tk.INSERT,R[i])
        #head hidrograf total
        header5=tk.Entry(wonframe,bg="gray",fg="white",justify="center")
        header5.grid(row=0,column=8,rowspan=2,sticky="nesw")
        header5.insert(tk.INSERT,list3)
        #total reff
        header6=tk.Entry(wonframe,bg="gray",fg="white",width=10,justify="center")
        header6.grid(row=2,column=8,sticky="nesw")
        header6.insert(tk.INSERT,sum(R))
        #head volume hidrograf
        header7=tk.Entry(wonframe,bg="gray",fg="white",width=18,justify="center")
        header7.grid(row=0,column=9,rowspan=3,sticky="nesw")
        header7.insert(tk.INSERT,list4)

        #pembuatan superposisi kolom
        kolom1=[]
        kolom2=[0]
        kolom3=[0,0]
        kolom4=[0,0,0]
        kolom5=[0,0,0,0]
        kolom6=[0,0,0,0,0]
        for i in range(len(t_gama_superposisi)):
                kolom1.append(qt_gama_superposisi[i]*R[0])
                kolom2.append(qt_gama_superposisi[i]*R[1])
                kolom3.append(qt_gama_superposisi[i]*R[2])
                kolom4.append(qt_gama_superposisi[i]*R[3])
                kolom5.append(qt_gama_superposisi[i]*R[4])
                kolom6.append(qt_gama_superposisi[i]*R[5])
        koloma=kolom1+[0,0,0,0,0]
        kolomb=kolom2+[0,0,0,0]
        kolomc=kolom3+[0,0,0]
        kolomd=kolom4+[0,0]
        kolome=kolom5+[0]
        kolomf=kolom6
        print(len(koloma),len(kolomb),len(kolomc))
        #----------------------------------------------------------
        #QHSS
        for k in range(len(t_gama_superposisi)):
                b=tk.Entry(wonframe)
                b.grid(row=k+3,column=1)
                b.insert(tk.INSERT,qt_gama_superposisi[k])

        #hasil kali reff ke superposisi
        for i in range(len(koloma)):
                c=tk.Entry(wonframe)
                c.grid(row=i+3,column=2)
                c.insert(tk.INSERT,koloma[i])
                d=tk.Entry(wonframe)
                d.grid(row=i+3,column=3)
                d.insert(tk.INSERT,kolomb[i])
                e=tk.Entry(wonframe)
                e.grid(row=i+3,column=4)
                e.insert(tk.INSERT,kolomc[i])
                f=tk.Entry(wonframe)
                f.grid(row=i+3,column=5)
                f.insert(tk.INSERT,kolomd[i])
                g=tk.Entry(wonframe)
                g.grid(row=i+3,column=6)
                g.insert(tk.INSERT,kolome[i])
                h=tk.Entry(wonframe)
                h.grid(row=i+3,column=7)
                h.insert(tk.INSERT,kolomf[i])
        
        global tsuperp4
        tsuperp4=t_gama_superposisi
        j=int(t_gama_superposisi[-1])+1
        for k in range(j,j+5):
                tsuperp4.append(k)

        #isi waktu
        for i in range(len(tsuperp4)):
                a=tk.Entry(wonframe)
                a.grid(row=i+3,column=0)
                a.insert(tk.INSERT,tsuperp4[i])

        #isi hidrograf total
        global qsuperp4
        qsuperp4=[]
        for i in range (len(koloma)):
                m=tk.Entry(wonframe)
                m.grid(row=i+3,column=8)
                voltabb=koloma[i]+kolomb[i]+kolomc[i]+kolomd[i]+kolome[i]+kolomf[i]
                qsuperp4.append(voltabb)
                m.insert(tk.INSERT,qsuperp4[i])

        vsuperp4=[0]
        for a in range(1,len(kolomc)):
                rumus=0.5*3600*(tsuperp4[a]-tsuperp4[a-1])*(qsuperp4[a]+qsuperp4[a-1])
                vsuperp4.append(rumus)

        for b in range(len(vsuperp4)):
                n=tk.Entry(wonframe)
                n.grid(row=b+3,column=9)
                n.insert(tk.INSERT,vsuperp4[b])



        total=sum(vsuperp4)
        tot=tk.Entry(wonframe)
        tot.grid(row=len(vsuperp4)+4,column=9)
        tot.insert(tk.INSERT,total)
        total_teks=tk.Label(wonframe,text="Vol(m3) =")
        total_teks.grid(row=len(vsuperp4)+4,column=8)

        A_teks=tk.Label(wonframe,text="A (km2) =")
        A_teks.grid(row=len(vsuperp4)+5,column=8)
        A_entry=tk.Entry(wonframe)
        A_entry.grid(row=len(vsuperp4)+5,column=9)
        A_entry.insert(tk.INSERT,A)

        Rb=tk.DoubleVar(wonframe,value=(total/A/1000))
        Rb_teks=tk.Label(wonframe,text="R (mm) =")
        Rb_teks.grid(row=len(vsuperp4)+6,column=8)
        Rb_entry=tk.Entry(wonframe,textvariable=Rb)
        Rb_entry.grid(row=len(vsuperp4)+6,column=9)

        persen_teks=tk.Label(wonframe,text="%HDRO")
        persen_teks.grid(row=len(vsuperp4)+7,column=8)
        persen_entry=tk.Entry(wonframe)
        persen_entry.grid(row=len(vsuperp4)+7,column=9)
        persen_entry.insert(tk.INSERT,Rb.get()/sum(R)*100)
    
    def grafik_gama():
        fig=plt.figure("GAMA - 1")
        ax14=fig.add_subplot(111)
        ax14.plot(t_tab5,qt_gama_koreksi)
        ax14.grid(True)
        ax14.set_xlabel("t (jam)")
        ax14.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
        ax14.set_title("GRAFIK HSS METODE GAMA - 1")
#----------
        ax14.set_ylim(0,qp_var_tab5.get()+2)
        ax24=ax14.twinx()
        ax24.set_ylabel("R (mm)")
        ax24.bar([1],1,color="b",label="Hujan eff (mm)")
        #ax24.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
        #ax24.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
        ax24.set_ylim((qp_var_tab5.get()*2),0)
        ax24.legend()
        plt.show()

    def grafik_gama_superposisi():

            rtot=(
                rtot_kolom11_var_tab1.get(),rtot_kolom21_var_tab1.get(),
                rtot_kolom31_var_tab1.get(),rtot_kolom41_var_tab1.get(),
                rtot_kolom51_var_tab1.get(),rtot_kolom61_var_tab1.get()
            )
            infiltrasi=(
                infil_kolom12_var_tab1.get(),infil_kolom22_var_tab1.get(),
                infil_kolom32_var_tab1.get(),infil_kolom42_var_tab1.get(),
                infil_kolom52_var_tab1.get(),infil_kolom62_var_tab1.get()
                )
            reff=(
                reff_kolom13_var_tab1.get(),reff_kolom23_var_tab1.get(),
                reff_kolom33_var_tab1.get(),reff_kolom43_var_tab1.get(),
                reff_kolom53_var_tab1.get(),reff_kolom63_var_tab1.get()
            )

            fig=plt.figure("HIDROGRAF BANJIR GAMA - 1")
            ax14=fig.add_subplot(111)
            ax14.plot(tsuperp4,qsuperp4)
            ax14.grid(True)
            ax14.set_xlabel("t (jam)")
            ax14.set_ylabel(r"$\mathrm {Q\/(m^3/s)}$")
            ax14.set_title("GRAFIK HIDROGRAF BANJIR GAMA - 1")
            if (hortonfo1_var.get()!=0 or hortonfo2_var.get()!=0 or hortonfc_var.get()!=0 or hortonk_var.get()!=0):
                ax14.set_ylim(0,max(qsuperp4)*2)
                ax24=ax14.twinx()
                ax24.set_ylabel("R (mm)")
                ax24.bar([1,2,3,4,5,6],rtot,color="r",label="Hujan eff (mm)")
                ax24.bar([1,2,3,4,5,6],infiltrasi,color="b",label="infiltrasi (mm)")
                ax24.set_ylim((max(rtot)*3),0)
                ax24.legend()
            plt.show()

#TOMBOL GAMA
    hitung_tab5=ttk.Button(mighty5,width=30,text="HITUNG",command=hitung_gama)
    hitung_tab5.grid(row=22,columnspan=5,sticky="W",pady=(20,0))
    tabel_tab5=ttk.Button(mighty5,width=30,text="Tampilkan Tabel",command=tabel_gama)
    tabel_tab5.grid(row=23,columnspan=5,sticky="W")
    grafik_tab5=ttk.Button(mighty5,width=30,text="Tampilkan Grafik HSS",command=grafik_gama)
    grafik_tab5.grid(row=24,columnspan=5,sticky="W")
    tabel_tab5_superposisi=ttk.Button(mighty5,width=30,text="Tabel Hidrograf Banjir",command=tabel_gama_superposisi)
    tabel_tab5_superposisi.grid(row=25,columnspan=5,sticky="W")
    grafik_tab5_superposisi=ttk.Button(mighty5,width=30,text="Grafik Hidrograf Banjir",command=grafik_gama_superposisi)
    grafik_tab5_superposisi.grid(row=26,columnspan=5,sticky="W")
#===========================================================================================
    #MULAI GUI PROGRAM
    win.mainloop()
#program kalau ditaruh disini dengan splash aktif bakal LOOPING
#===========================================================================================

cover=("Helvetica",20,("underline","bold"))
splash=tk.Tk()
gaya=tk.Frame(splash,height=200, bd=2,relief="solid")
gaya.pack(anchor="sw",fill="both",expand=True, padx=5, pady=5,side="top")
label1=tk.Label(gaya,text="\n\n\n\nHISITERA",font=cover)
label1.pack(side="top",anchor="n")
label2=tk.Label(gaya,text="KK Rek. Sumber Daya Air\nInstitut Teknologi Sumatera",justify=tk.RIGHT)
label2.pack(side="bottom",anchor="e")
w=300
h=300
ws=splash.winfo_screenwidth()
hs=splash.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
splash.geometry("%dx%d+%d+%d"%(w,h,x,y))
splash.resizable(0,0)
splash.overrideredirect(True)
splash.after(1000,destroyed)
splash.mainloop()