"""
Pro Organizer Scripts Package
Thanks for purchasing - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Organize your everyday objects workflow with a better way in your projects.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers and group dividers)
Version: 1.0
Date: 22/05/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
 
def add_custom(name, color):


       root = doc.GetLayerObjectRoot()
       LayersList = root.GetChildren() 

       names=[]    
       layers=[]
       for l in LayersList:
           n=l.GetName()
           names.append(n)
           layers.append((n,l))


       if not name in names:


           layer = c4d.documents.LayerObject() #New Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] =color
           layer[c4d.ID_LAYER_GENERATORS]=False
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = name #Name of null
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(null)
       
       c4d.EventAdd()


color_custom=c4d.Vector(1,0.545,0.094) # Layer Color
name_customd="_custom divider_" #change only the text inside of ""

if __name__=='__main__':
  add_custom(name_customd,color_custom)

