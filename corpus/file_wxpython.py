import wx

class FitnessTracker(wx.Frame):
    def __init__(self, *args, **kw):
        super(FitnessTracker, self).__init__(*args, **kw)

        self.workouts = []

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.date_input = wx.TextCtrl(panel)
        self.type_input = wx.TextCtrl(panel)
        self.duration_input = wx.TextCtrl(panel)

        vbox.Add(wx.StaticText(panel, label="Date (YYYY-MM-DD):"))
        vbox.Add(self.date_input, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="Workout Type:"))
        vbox.Add(self.type_input, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="Duration (minutes):"))
        vbox.Add(self.duration_input, flag=wx.EXPAND | wx.ALL, border=5)

        log_button = wx.Button(panel, label="Log Workout")
        log_button.Bind(wx.EVT_BUTTON, self.on_log)

        vbox.Add(log_button, flag=wx.EXPAND | wx.ALL, border=5)

        self.history_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.history_text, flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizer(vbox)

    def on_log(self, event):
        date = self.date_input.GetValue()
        workout_type = self.type_input.GetValue()
        duration = self.duration_input.GetValue()

        if date and workout_type and duration:
            self.workouts.append(f"{date}: {workout_type} for {duration} minutes")
            self.history_text.SetValue("\n".join(self.workouts))
            self.date_input.Clear()
            self.type_input.Clear()
            self.duration_input.Clear()

if __name__ == "__main__":
    app = wx.App(False)
    frame = FitnessTracker(None, title="Fitness Tracker")
    frame.Show()
    app.MainLoop()
