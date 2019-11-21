"""
Pro Organizer - Scripts Package v0.9
Thanks for download - for commercial and personal uses.
The Pro Organizer v1.0 granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Improve your scene organization and your projects workflow with a better way.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers and group dividers)
Version: 1.0
Date: 19/08/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

Pro Organizer - Scripts Package v0.9 belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui
 
#global ids
color_divider=c4d.Vector(1,1,1) # layer divider
name_null="___________________________________" #name of divider
name_gnull="__________________________" #name of divider group
 
#dialog of divider group
class OptionsDialog(gui.GeDialog):

    IDC_LABELNAME = 1000
    IDC_EDITNAME = 1001

    def CreateLayout(self):

        self.SetTitle('Add Divider Group')

        self.AddStaticText(self.IDC_LABELNAME, c4d.BFH_LEFT, name='Group Name:') 
        self.AddEditText(self.IDC_EDITNAME, c4d.BFH_SCALEFIT)
        self.SetString(self.IDC_EDITNAME, 'Write Group Name')

        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False
        return True

    def Command(self, id, msg):

        if id == c4d.IDC_OK:
            self.ok = True
            self.findGName = self.GetString(self.IDC_EDITNAME)
            self.Close()

        elif id == c4d.IDC_CANCEL:
            self.Close()
            gui.MessageDialog('Please select a name for the divider group.')

        return True
 
def add_divider(name, color):

       # Open the options dialogue to let users choose their options.
       dlg = OptionsDialog()
       dlg.Open(c4d.DLG_TYPE_MODAL, defaultw=300, defaulth=50)
       if not dlg.ok:
         return

       #layers ops
       root = doc.GetLayerObjectRoot()
       LayersList = root.GetChildren() 

       names=[]    
       layers=[]

       #start undo action
       doc.StartUndo()

       for l in LayersList:
           n=l.GetName()
           names.append(n)
           layers.append((n,l))

       if not name in names:
           layer = c4d.documents.LayerObject() #new Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] =color
           layer_settings = {'solo': False, 'view': False, 'render': True, 'manager': True, 'locked': False, 'generators': False, 'deformers': False, 'expressions': False, 'animation': False}
           layer.SetLayerData(doc, layer_settings)
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       #divider ops
       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = name_gnull+dlg.findGName #name of null / divider group
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(null)
       doc.AddUndo(c4d.UNDOTYPE_NEW, null)

       #end undo action
       doc.EndUndo()
       
       #update scene
       c4d.EventAdd()
  
#obj pos functions       
def f_obj():
      firstObj = doc.GetFirstObject()
      return firstObj

def a_obj(pos):
      actvObj = doc.GetActiveObject()
      if not actvObj:
          actvObj = doc.GetActiveObjects(1)
          if not actvObj: return
          actvObj = actvObj[pos]
      return actvObj
      
#obj insert ops
def insert_up():
      firstObj = f_obj()
      actvObj = a_obj(0)
      if not actvObj: return
      firstObj.InsertBefore(actvObj)

def insert_down():
      firstObj = f_obj()
      actvObj = a_obj(-1)
      if not actvObj: return
      firstObj.InsertAfter(actvObj)

def insert_child():
      firstObj = f_obj()
      actvObj = a_obj(0)
      if not actvObj: return
      firstObj.InsertUnder(actvObj)

#shortcuts actions
def d_shortcuts_functions():
    bc = c4d.BaseContainer()

    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
        if  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT: 
            add_divider("_dividers_",color_divider)
            insert_up()
             
        elif  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: 
            add_divider("_dividers_",color_divider)
            insert_down()
            
        elif  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL: 
            add_divider("_dividers_",color_divider)
            insert_child()
             
        else:
            add_divider("_dividers_",color_divider)

    #update scene
    c4d.EventAdd()

if __name__=='__main__':
    d_shortcuts_functions()