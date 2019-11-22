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

"""

import c4d

#global ids
color_custom=c4d.Vector(1,0.545,0.094) # layer Color in float values
name_customd="_custom divider_" #change only the text inside of ""
 
def add_custom(name, color):

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
           layer[c4d.ID_LAYER_GENERATORS]=False
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       #prevent copies in obj manager
       objectsList = doc.GetObjects()
       for obj in objectsList:
          if obj[c4d.ID_BASELIST_NAME] == name:
            return

       #divider ops
       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = name #name of null
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(null)
       doc.AddUndo(c4d.UNDOTYPE_NEW, null)

       #end undo action
       doc.EndUndo()
       
       #update scene
       c4d.EventAdd()

if __name__=='__main__':
  add_custom(name_customd,color_custom)