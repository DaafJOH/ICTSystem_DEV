import tkinter, json, ssl, urllib.request, _thread, time, datetime
ssl._create_default_https_context = ssl._create_unverified_context

class MainWindow():
    def __init__(self, master):
        master.title("ICT System")

        self.CoronaFrame = tkinter.Frame(master, relief="groove", border=2, width=940, height=340)
        self.CoronaFrame.grid_propagate(0)
        self.CoronaFrame.columnconfigure(0, weight=313)
        self.CoronaFrame.columnconfigure(1, weight=313)
        self.CoronaFrame.columnconfigure(2, weight=313)
        self.CoronaFrame.grid(row=0, rowspan=3, column=0, padx=10, pady=10, sticky="NW")
        self.CoronaLabel = tkinter.Label(self.CoronaFrame, text="Coronadashboard:", font=("Comic Sans MS", 30))
        self.CoronaLabel.grid(row=0, columnspan=3, padx=10, pady=10, sticky="EW")
        self.CoronaTestLabel = tkinter.Label(self.CoronaFrame, text="", font=("Comic Sans MS", 50), width=31)
        self.CoronaTestLabel.grid_propagate(False)
        self.CoronaTestLabel.grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        self.CoronaTestLabelEx = tkinter.Label(self.CoronaFrame, text="Peoples that\nTested positive", font=("Comic Sans MS", 25), width=31)
        self.CoronaTestLabelEx.grid(row=2, column=0, padx=10, pady=10, sticky="EW")
        self.CoronaICLabel = tkinter.Label(self.CoronaFrame, text="", font=("Comic Sans MS", 50), width=31)
        self.CoronaICLabel.grid_propagate(False)
        self.CoronaICLabel.grid(row=1, column=1, padx=10, pady=10, sticky="EW")
        self.CoronaICLabelEx = tkinter.Label(self.CoronaFrame, text="Peoples in\nIntensive Care", font=("Comic Sans MS", 25), width=31)
        self.CoronaICLabelEx.grid(row=2, column=1, padx=10, pady=10, sticky="EW")
        self.CoronaRLabel = tkinter.Label(self.CoronaFrame, text="", font=("Comic Sans MS", 50), width=31)
        self.CoronaRLabel.grid_propagate(False)
        self.CoronaRLabel.grid(row=1, column=2, padx=10, pady=10, sticky="EW")
        self.CoronaRLabelEx = tkinter.Label(self.CoronaFrame, text="Reproduction rate\n(R number)", font=("Comic Sans MS", 25), width=31)
        self.CoronaRLabelEx.grid(row=2, column=2, padx=10, pady=10, sticky="EW")

        self.TimeFrame = tkinter.Frame(master, relief="groove", border=2, width=940, height=250)
        self.TimeFrame.grid_propagate(0)
        self.TimeFrame.columnconfigure(0, weight=470)
        self.TimeFrame.columnconfigure(1, weight=470)
        self.TimeFrame.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky="NE")
        self.TimeLabel = tkinter.Label(self.TimeFrame, text="Da time of da day", font=("Comic Sans MS", 30))
        self.TimeLabel.grid(row=0, columnspan=2, padx=10, pady=10, sticky="EW")
        self.DateLabel = tkinter.Label(self.TimeFrame, text="2021/11/13", font=("Comic Sans MS", 50))
        self.DateLabel.grid(row=1, column=0, padx=1, pady=1)
        self.LocalTimeLabel = tkinter.Label(self.TimeFrame, text="23:27:10", font=("Comic Sans MS", 50))
        self.LocalTimeLabel.grid(row=1, column=1, padx=1, pady=1)
        self.DayLabel = tkinter.Label(self.TimeFrame, text="Saturday", font=("Comic Sans MS", 25))
        self.DayLabel.grid(row=2, column=0, padx=1, pady=1)
        self.MillisLabel = tkinter.Label(self.TimeFrame, text="234", font=("Comic Sans MS", 25))
        self.MillisLabel.grid(row=2, column=1, padx=1, pady=1)

        self.WetherFrame = tkinter.Frame(master, relief="groove", border=2, width=940, height=625)
        self.WetherFrame.grid_propagate(0)
        self.WetherFrame.grid(row=3, column=0, padx=10, pady=10, sticky="NW")
        self.WetherLabel = tkinter.Label(self.WetherFrame, text="Where's da wetha", font=("Comic Sans MS", 30))
        self.WetherLabel.grid(row=0, columnspan=2, padx=10, pady=10, sticky="EW")

        self.NewsFrame = tkinter.Frame(master, relief="groove", border=2, width=940, height=715)
        self.NewsFrame.grid_propagate(0)
        self.NewsFrame.grid(row=2, rowspan=2, column=1, padx=10, pady=10, sticky="NE")
        self.NewsLabel = tkinter.Label(self.NewsFrame, text="mof")
        self.NewsLabel.grid()

        _thread.start_new_thread(MainLoop, ())
        _thread.start_new_thread(TimeLoop, ())

def MainLoop():
    while True:
        InfectedData = json.loads(urllib.request.urlopen("https://coronadashboard.rijksoverheid.nl/_next/data/ZJJVrSo_5vJac2qihzgeq/nl/landelijk/positief-geteste-mensen.json").read())["pageProps"]["selectedNlData"]["difference"]["tested_overall__infected_moving_average"]
        Window.CoronaTestLabel.config(text=InfectedData["old_value"] + InfectedData["difference"])

        ICData = json.loads(urllib.request.urlopen("https://coronadashboard.rijksoverheid.nl/_next/data/ZJJVrSo_5vJac2qihzgeq/nl.json").read())["pageProps"]["selectedNlData"]["intensive_care_lcps"]["last_value"]["beds_occupied_covid"]
        Window.CoronaICLabel.config(text=ICData)

        RData = json.loads(urllib.request.urlopen("https://coronadashboard.rijksoverheid.nl/_next/data/ZJJVrSo_5vJac2qihzgeq/nl/landelijk/reproductiegetal.json").read())["pageProps"]["selectedNlData"]["reproduction"]["values"][-15]["index_average"]
        Window.CoronaRLabel.config(text=RData)



        Window.DateLabel.config(text=time.strftime(r"%Y/%m/%d"))
        Window.DayLabel.config(text=time.strftime("%A"))

        time.sleep(60*15)

def TimeLoop():
    while True:
        Now = datetime.datetime.now()
        Window.LocalTimeLabel.config(text=Now.strftime("%H:%M:%S"))
        Window.MillisLabel.config(text=Now.strftime("%f"))
        time.sleep(.01)

root = tkinter.Tk()
root.geometry("1920x1080")
Window = MainWindow(root)
root.mainloop()