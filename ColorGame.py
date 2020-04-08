import tkinter as tk
import random
root=tk.Tk()
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown'] 
score=0
timeleft=30

def countdown():
    global timeleft
    if(timeleft>0):
        timeleft-=1
        timeLabel.config(text = "Time left : "  + str(timeleft)) 
        timeLabel.after(1000, countdown) 
    else:
        Label.config(text="Final Score = "+str(score),fg="#964B00")
        ent.destroy()
    

def nextColor(): 
    global score 
    global timeleft 
    if timeleft > 0: 
        ent.focus_set() 

        if ent.get().lower() == colours[1].lower(): 
            score += 1
        ent.delete(0, tk.END) 
        random.shuffle(colours) 
        Label.config(fg = str(colours[1]), text = str(colours[0])) 
        scoreLabel.config(text = "Score: " + str(score))
          



def startGame(event): 
    ent.place(relx=0.3,rely=0.8,relwidth=0.4,relheight=0.1)
    
    if timeleft==30:
        countdown()
    
    nextColor()



    
    







root.title("Color Game")
root.geometry("500x400")
canvas=tk.Canvas(root,height=300,width=400,bg="#ebbf52")
back=tk.Frame(root,bg="#ebbf52")
back.place(relwidth=1,relheight=1)
topf=tk.Frame(root,bg="#f0d38b")
topf.place(relx=0.5,rely=0.1,relwidth=1,relheight=0.17,anchor="n")
nameLabel=tk.Label(topf,text="COLOR GAME",font=("Helvetica Bold",27),bg="#f0d38b",fg="#964B00")
nameLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
instruc=tk.Label(root,text="Type in the color you see, not the color you read!",font=("Helvetica Bold",14),bg="#ebbf52",fg="#964B00")
instruc.place(relx=0,rely=0.27,relwidth=1,relheight=0.1)
start=tk.Label(root,text="Hit ENTER to Begin!!",font=("Helvetica Bold",16),bg="#ebbf52",fg="#964B00")
start.place(relx=0,rely=0.35,relwidth=1,relheight=0.1)
timeLabel = tk.Label(root, text = "Time left : " + str(timeleft), font = ('Helvetica', 12),bg="#f0d38b",fg="#964B00")
timeLabel.place(relx=0,rely=0.55,relwidth=1,relheight=0.07)
scoreLabel = tk.Label(root, text = "Score : "+str(score), font = ('Helvetica', 12),bg="#f0d38b",fg="#964B00")
scoreLabel.place(relx=0,rely=0.45,relwidth=1,relheight=0.07)
Label = tk.Label(root, font = ('Helvetica', 30),bg="#ebbf52")
Label.place(relx=0,rely=0.65,relwidth=1,relheight=0.13)


ent=tk.Entry(root)


root.bind("<Return>",startGame)














root.mainloop()

