import wx
import os
from PIL import Image
class MyMainApp(wx.Frame):
	def __init__(self,parent,ID,title):
		wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(640,480),style=wx.FRAME_SHAPED|wx.SIMPLE_BORDER|wx.STAY_ON_TOP);
		self.pt = wx.Point(0,0);
		img = wx.Image(os.path.sep.join([os.path.curdir,'bg.png']));
		img.SetMask(True);
		img.SetMaskColour(255,255,255);
		self.bg = wx.BitmapFromImage(img);
		self.SetSize(wx.Size(self.bg.GetWidth(),self.bg.GetHeight()));
		self.hasShape = False;
		self.OnWindowCreate();
		self.Bind(wx.EVT_RIGHT_UP,self.OnRightClickEvent);
		self.Bind(wx.EVT_WINDOW_CREATE,self.OnWindowCreate);
		self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftClickDown);
		self.Bind(wx.EVT_LEFT_UP,self.OnLeftClickUp);
		self.Bind(wx.EVT_MOTION,self.OnMouseMotion);
		self.Bind(wx.EVT_PAINT,self.OnPaint);	
		modList=[];
		dst=os.getcwd();
		global modpath;
		modpath=dst+"\\Modules\\";
		templist=os.listdir(modpath)
		for i in templist:
			ini_file=modpath+i+"\\module.ini"
			if os.path.exists(ini_file):
				modList.append(i)
		btn1_bmp=wx.Bitmap(dst+"\\res\\btn1.bmp",wx.BITMAP_TYPE_BMP)
		btn1_click_bmp=wx.Bitmap(dst+"\\res\\btn1_click.bmp",wx.BITMAP_TYPE_BMP)
		btn2_bmp=wx.Bitmap(dst+"\\res\\btn2.bmp",wx.BITMAP_TYPE_BMP)
		btn2_click_bmp=wx.Bitmap(dst+"\\res\\btn2_click.bmp",wx.BITMAP_TYPE_BMP)
		btn3_bmp=wx.Bitmap(dst+"\\res\\btn3.bmp",wx.BITMAP_TYPE_BMP)
		btn3_click_bmp=wx.Bitmap(dst+"\\res\\btn3_click.bmp",wx.BITMAP_TYPE_BMP)
		vbox = wx.BoxSizer( wx.VERTICAL);
		btn1=wx.BitmapButton(self,22,btn1_bmp,pos=(50,200),style=0)
		btn2=wx.BitmapButton(self,22,btn2_bmp,pos=(60,240),style=0)
		btn3=wx.BitmapButton(self,22,btn3_bmp,pos=(70,280),style=0)
		global Choice1
		Choice1=wx.Choice(self,-1,(190,105),(420,60),choices=modList)
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
	def OnRightClickEvent(self,event):
		if wx.MessageBox("xx?","xx",wx.YES_NO,self) == 2:
		    wx.Exit();

	def OnLeftClickDown(self,event):
		self.CaptureMouse();
		pos =  event.GetPosition();
		self.pt = wx.Point(pos.x,pos.y);

	def OnMouseMotion(self,event):
		if event.Dragging() and event.LeftIsDown():
			pos = self.ClientToScreen(event.GetPosition());
			self.Move((pos.x-self.pt.x,pos.y-self.pt.y));

	def OnLeftClickUp(self,event):
		if self.HasCapture():
			self.ReleaseMouse();

	def OnWindowCreate(self,event=None):
		r = wx.RegionFromBitmap(self.bg);
		self.SetShape(r);

	def OnPaint(self,event):
		dc = wx.PaintDC(self);
		dc.DrawBitmap(self.bg,0,0,True);
		
class MyApp(wx.App):
	def OnInit(self):
		frame=MyMainApp(None,-1,"myapp")
		frame.Show(True)
		return True

app=MyApp(0)
app.MainLoop()
