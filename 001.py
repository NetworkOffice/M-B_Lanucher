import wx
import os
from PIL import Image
class MyMainApp(wx.Frame):
	def __init__(self,parent,ID,title):
		wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(655,520))
		modList=[]
		dst=os.getcwd()
		global modpath
		modpath=dst+"\\Modules\\"
		templist=os.listdir(modpath)
		for i in templist:
			ini_file=modpath+i+"\\module.ini"
			if os.path.exists(ini_file):
				modList.append(i)
		vbox = wx.BoxSizer( wx.VERTICAL)
		panel=wx.Panel(self)
		panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		vbox.Add(wx.Button(panel,22,"Start Game",(50,200),(200,35)),1)
		vbox.Add(wx.Button(panel,22,"Configure",(50,240),(200,35)),1)
		vbox.Add(wx.Button(panel,22,"Exit",(50,280),(200,35)),1)
		global Choice1
		Choice1=wx.Choice(panel,-1,(190,105),(420,60),choices=modList)
		self.Bind(wx.EVT_CHOICE,self.OnChoice,Choice1)
		self.Centre()

	def OnChoice(self, event):
		currMod=Choice1.GetStringSelection()
		currModpath=modpath+currMod
		currModImage=currModpath+"\\main.bmp"
		image=wx.Bitmap(currModImage,wx.BITMAP_TYPE_BMP)
		image1=wx.StaticBitmap(self,-1,image,pos=(250,150), size=(image.GetWidth(),image.GetHeight()))
	def OnEraseBackground(self, event):
		dc=event.GetDC()
		if not dc:
		     dc = wx.ClientDC(self)
		     rect = self.GetUpdateRegion().GetBox()
		     dc.SetClippingRect(rect)
		bmp = wx.Bitmap("bg.bmp")
		dc.DrawBitmap(bmp, 0, 0)
		
class MyApp(wx.App):
	def OnInit(self):
		frame=MyMainApp(None,-1,"myapp")
		frame.Show(True)
		return True

app=MyApp(0)
app.MainLoop()
