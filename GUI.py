from tkinter import*
from tkinter import messagebox
import tkinter.font
import tkinter.ttk as ttk
import configparser
import os
import KIMS3DPLearningset
import pathlib
config=configparser.ConfigParser(strict=False) #설정저장

root=Tk()
root.title("Random")
root.geometry("350x240")
#root.wm_iconbitmap("kims.ico")
root.configure(background="#120043")

titleFont=tkinter.font.Font(family="나눔고딕", size=20, weight="bold",slant="roman")
titleLabel=Label(root,text="KIMS Random Generator",font=titleFont, bg='#120043',fg="#eaeaee",pady="5")
titleLabel.grid(row=0,column=0,columnspan=2)
#titleLabel.pack()

mainFont=tkinter.font.Font(family="나눔고딕", size=12,weight="bold")


#Size, Pattern 종류 Label, 입력창
Label_size=Label(root, text="Size X Size",pady="5",bg='#120043',fg="#eaeaee",font=mainFont,width=12)
Label_size.grid(row=1,column=0)
#Label_size.pack()



Label_pattern=Label(root, text="Pattern 종류",pady="5",bg='#120043',fg="#eaeaee",font=mainFont,width=12)
Label_pattern.grid(row=2,column=0)
#Label_pattern.pack()



Label_RandomSeed=Label(root, text="Random Seed",pady="5",bg='#120043',fg="#eaeaee",font=mainFont,width=12)
Label_RandomSeed.grid(row=3,column=0)



entry_size=Entry(root, width=10, borderwidth=1)
entry_size.grid(row=1,column=1,columnspan=2,pady=15)#,sticky="w")
#entry_size.pack()



entry_Random=Entry(root, width=10, borderwidth=1)
entry_Random.grid(row=3,column=1,columnspan=2,pady=15)
entry_Random.insert(END, "5000")



pattern_strs=StringVar()
entry_pattern=ttk.Combobox(textvariable=pattern_strs, height=0, width=20, state='readonly')
entry_pattern['value']=("원","원+삼각", "원+삼각+사각", "원+삼각+사각+오각", "원+삼각+사각+오각+육각")
print(entry_pattern.get())
entry_pattern.current(4)
entry_pattern.grid(row=2,column=1,columnspan=2) #,sticky="w")
#entry_pattern.pack()



stl_ge=IntVar()
stl_show=IntVar()


def stl_act():
    if stl_ge.get()==1:
        stl_showbox.config(state='normal')
    else:
        stl_showbox.config(state='disabled')
        stl_showbox.deselect()



stl_gebox=Checkbutton(root, text="Stl Generate", variable=stl_ge, command=stl_act, bg='#120043',fg="#eaeaee", selectcolor='#120043')
stl_gebox.grid(row=4, column=0, columnspan=1)

stl_showbox=Checkbutton(root, text="Stl Show", state='disabled', variable=stl_show, bg='#120043',fg="#eaeaee", selectcolor='#120043')
stl_showbox.grid(row=4, column=1, columnspan=1)

def btncmd():
    while True:
        try:
             nSize = int(entry_size.get())
             nSeed = int(entry_Random.get())
             nType = int(entry_pattern.current())+ 1
             bSTL  = int(stl_ge.get())
             if nSize<=0 or nSeed<=0:
                 messagebox.showwarning("경고","Size X Size, Random Seed는 1 이상의 정수만 입력 가능합니다.")
             else:
                print("========On Going======")
                print("========On Going2=====")
                execute_LearningSet_Ver(nSize, nType, nSeed)
                if (bSTL == 1):
                    execute_Viewfile(entry_size.get(), nType, nSeed)
             break
        except ValueError:
             messagebox.showwarning("경고","Size X Size, Random Seed는 1 이상의 정수만 입력 가능합니다.")
             break


def execute_LearningSet_Ver( nSize, nPattern, nSeed):
    testSet = KIMS3DPLearningset.Randomset(nSize, nSize, nPattern, nSeed)
    testSet.generate()

#    os.system( "python3 LearningSet_Ver.py {Size} {Pattern} {Seed} {Show}".format(Size=nSize, Pattern=nPattern, Seed=nSeed, Show=bSTL))
def execute_Viewfile(nSize, nPattern, nSeed):
    strname = "S{size}_T{type}_R{seed}.scad".format(size=nSize, type=nPattern, seed=nSeed)
    print(strname)
    spath = os.getcwd()
    os.system('"C:\Program Files\OpenSCAD\openscad.exe" {strname}'.format(spath=spath, strname=strname))

btn= Button(root, text="선택", command=btncmd, bg='#20074f',fg="#eaeaee")
#btn.pack()
btn.grid(row=5,column=0, columnspan=2)


root.mainloop()
