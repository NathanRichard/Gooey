import wx
from gooey.gui.util import wx_util

class OptionsGroup:
    def __init__(self, parent, groupName, groupDescription, showBorders):
        # determine the type of border , if any, the main sizer will use
        self.parent = parent
        if showBorders:
            boxDetails = wx.StaticBox(parent, -1, groupName)
            self.sizer = wx.StaticBoxSizer(boxDetails, wx.VERTICAL)
        else:
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer.AddSpacer(10)
            if groupName:
                self.sizer.Add(wx_util.h1(parent, groupName), 0, wx.TOP | wx.BOTTOM | wx.LEFT, 8)
        if groupDescription:
            description = wx.StaticText(parent, label=groupDescription)
            self.sizer.Add(description, 0,  wx.EXPAND | wx.LEFT, 10)
        # apply an underline when a grouping border is not specified
        if not showBorders and groupName:
            self.sizer.Add(wx_util.horizontal_rule(parent), 0, wx.EXPAND | wx.LEFT, 10)

    def getSizerForChilds(self):
        return self.sizer

    def getParentForChilds(self):
        return self.parent
