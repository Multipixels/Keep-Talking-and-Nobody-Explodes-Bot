from ctypes import windll
from tkinter import *
from tkinter import ttk
from pynput.mouse import Controller
from voiceInterpreter import toggleActive

GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

z = 0
thisObject = 0

VirtualEvents=["<<SPEECH>>", "<<INPUT>>"]

def set_appwindow(mainWindow):
        # Honestly forgot what most of this stuff does. I think it's so that you can see
        # the program in the task bar while using overridedirect. Most of it is taken
        # from a post I found on stackoverflow.
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        # re-assert the new window style
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())


class Window:
    def __init__(self):
        global thisObject
        thisObject = self
        self.window = Tk()
        self.makeVirtualEvents()
        self.window.title("Keep Talking and Nobody Explodes Assistant")
        self.window.iconbitmap("Logo.ico")

        self.windowWidth = 800
        self.windowHeight = 800
        self.globalMouseX = 0
        self.globalMouseY = 0


        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHeight = self.window.winfo_screenheight()

        centerX = int(self.screenWidth/2 - self.windowWidth/2)
        centerY = int(self.screenHeight/2 - self.windowHeight/2)

        self.window.geometry(f'{self.windowWidth}x{self.windowHeight}+{centerX}+{centerY}')
        self.window.resizable(False, False)
        self.window.overrideredirect(True)
        self.window.configure(bg='#252526')
        self.window.after(10, lambda: set_appwindow(self.window))

        self.makeWidgets()

        self.window.bind("<Map>", self.frameMapped)
        self.window.geometry()

        self.window.mainloop()

    def makeWidgets(self):
        self.titleBar = Frame(self.window, bg="#3c3c3c", relief="groove")
        self.titleBar.pack(side=TOP, fill=X)

        self.titleLabel = Label(self.titleBar, padx=6, pady=4, bg="#3c3c3c", fg="white", text="KTANE Assistant")
        self.titleLabel.pack(side=LEFT)

        self.exitButton = Button(self.titleBar, text='✖', width=5, bg='#3c3c3c', fg='#35DAFF', relief="flat", command=self.exitGUI)
        self.exitButton.pack(side=RIGHT, fill=Y)

        self.minimizeButton = Button(self.titleBar, text='🗕', width=5, bg="#3c3c3c", fg='#35DAFF', relief="flat", command=self.minimizeGUI)
        self.minimizeButton.pack(side=RIGHT, fill=Y)

        self.textFrame = Frame(self.window, bg="#252526", highlightthickness=1, highlightbackground="#393939")
        self.textFrame.pack(fill=X, padx=30, pady=25)

        self.scrollBarStyle = ttk.Style(self.window)
        self.scrollBarStyle.theme_use("alt")
        self.scrollBarStyle.layout('arrowless.Vertical.TScrollbar', 
                    [('Vertical.Scrollbar.trough',
                    {'children': [('Vertical.Scrollbar.thumb', 
                                    {'expand': '1', 'sticky': 'nswe'})],
                    'sticky': 'ns'})])
        self.scrollBarStyle.configure("arrowless.Vertical.TScrollbar", troughborderwidth=1, troughcolor="#252526", background="#424242", bordercolor="#393939")
        self.scrollBarStyle.map('arrowless.Vertical.TScrollbar', background=[('disabled', "#252526"), ('pressed', '!disabled', '#5e5e5e'), ('active', '#4f4f4f')])

        self.scrollbar = ttk.Scrollbar(self.textFrame, style="arrowless.Vertical.TScrollbar")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.speechText = Text(self.textFrame, wrap=WORD, border=0, background="#252526", foreground="white", yscrollcommand=self.scrollbar.set, font=("Arial", 14))
        self.speechText.insert('end' , f">> Loading voice modules, please wait.\n")
        self.speechText.config(spacing3=4, state='disabled')
        self.speechText.pack(expand=YES, fill=BOTH)

        self.scrollbar.config(command=self.speechText.yview)

        self.contentFrame = Frame(self.window, bg="#252526")
        self.contentFrame.pack(fill=BOTH, expand=TRUE)
        self.contentFrame.grid_rowconfigure(0, weight = 1)
        self.contentFrame.grid_columnconfigure(0, weight = 1)

        self.activateButton = Button(self.contentFrame, text="Activate", padx=30, pady=15, font=("Arial", 12))
        self.activateButton.bind("<Button>", lambda e: toggleActive())
        self.activateButton.grid(row = 0, column = 0, sticky = "")

        self.titleLabel.bind("<ButtonPress-1>", self.setRelativePosition)
        self.titleBar.bind("<ButtonPress-1>", self.setRelativePosition)
        self.titleLabel.bind("<B1-Motion>", self.moveGUI)
        self.titleBar.bind("<B1-Motion>", self.moveGUI)

    def minimizeGUI(self):
        global z
        self.window.state('withdrawn')
        self.window.overrideredirect(False)
        self.window.state('iconic')
        z = 1

    def frameMapped(self, event=None):
        global z
        self.window.overrideredirect(True)
        if z == 1:
            set_appwindow(self.window)
            z = 0

    def exitGUI(self):
        raise SystemExit(0)

    def setRelativePosition(self, e): 
        mouse = Controller()
        currentMouseX = mouse.position[0]
        currentMouseY = mouse.position[1]

        self.globalMouseX = currentMouseX
        self.globalMouseY = currentMouseY

    def moveGUI(self, e):
        mouse = Controller()
        currentMouseX = mouse.position[0]
        currentMouseY = mouse.position[1]

        x = self.window.winfo_x() + (-self.globalMouseX + currentMouseX)
        y = self.window.winfo_y() + (-self.globalMouseY + currentMouseY)

        self.window.geometry(f'{self.windowWidth}x{self.windowHeight}+{x}+{y}')

        self.globalMouseX = currentMouseX
        self.globalMouseY = currentMouseY

    def makeVirtualEvents(self):
        for e in VirtualEvents:
            self.window.event_add(e,'None')
            self.window.bind(e, self.onVirtualEvent,"%d")

    def FireVirtualEvent(self,vEvent,data):
        Event.VirtualEventData=[vEvent, data]
        self.window.event_generate(vEvent)

    def onVirtualEvent(self,event):
        #print("Virtual Event Data: {}".format(event.VirtualEventData))
        if event.VirtualEventData[0] == VirtualEvents[0]:
            self.speechText.config(state=NORMAL)
            self.speechText.insert('end' , f">> {event.VirtualEventData[1]}\n")
            self.speechText.config(state=DISABLED)
        else:
            self.speechText.config(state=NORMAL)
            self.speechText.insert('end' , f"Bot heard: {event.VirtualEventData[1]}\n")
            self.speechText.config(state=DISABLED)

        if self.scrollbar.get()[1] == 1:
            self.speechText.see("end")


def ttsText(content):
    thisObject.FireVirtualEvent(VirtualEvents[0], content)

def inputText(content):
    thisObject.FireVirtualEvent(VirtualEvents[1], content)