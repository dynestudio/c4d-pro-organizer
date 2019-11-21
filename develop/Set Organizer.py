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

#global ids
color_divider=c4d.Vector(1,1,1) # layer divider
c4d_greyvalue = 0.75294117647
color_layer_divider=c4d.Vector(c4d_greyvalue, c4d_greyvalue, c4d_greyvalue) # layer divider space
color_lights=c4d.Vector(0.898,0.875,0.235) # layer lights
color_cams=c4d.Vector(0.235,0.388,0.898) # layer cams
color_geo=c4d.Vector(0.263,0.286,0.329) # layer geometry
name_null="___________________________________ " #name of divider
name_layerspace = name_null[:20]

def all_organizer(name, color, objname):

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
           layer = c4d.documents.LayerObject() #New Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] = color
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       #prevent copies in obj manager
       objectsList = doc.GetObjects()
       for obj in objectsList:
          if obj[c4d.ID_BASELIST_NAME] == objname:
            return

       #divider ops
       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = objname
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       null[c4d.ID_BASEOBJECT_USECOLOR] = 2
       null[c4d.ID_BASEOBJECT_COLOR] = color
       null[c4d.NULLOBJECT_ICONCOL] = True
       doc.InsertObject(null)
       doc.AddUndo(c4d.UNDOTYPE_NEW, null)

       #end undo action
       doc.EndUndo()

       #update scene
       c4d.EventAdd()

def add_divider(name, color):

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
           layer = c4d.documents.LayerObject() #New Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] = color
           layer_settings = {'solo': False, 'view': False, 'render': True, 'manager': True, 'locked': False, 'generators': False, 'deformers': False, 'expressions': False, 'animation': False}
           layer.SetLayerData(doc, layer_settings)
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       #prevent copies in obj manager
       objectsList = doc.GetObjects()
       objectsListNew=[]
       for obj in objectsList:
           if obj[c4d.ID_BASELIST_NAME] == name_null:
                objectsListNew.append(1)
       if len(objectsListNew) >= 4:
            return

       #divider ops
       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = name_null
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(null)
       doc.AddUndo(c4d.UNDOTYPE_NEW, null)

       #end undo action
       doc.EndUndo()
       
       #update scene
       c4d.EventAdd()

def divider_layer(name, color):

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
           layer = c4d.documents.LayerObject() #New Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] = color
           layer_settings = {'solo': False, 'view': False, 'render': False, 'manager': False, 'locked': False, 'generators': False, 'deformers': False, 'expressions': False, 'animation': False}
           layer.SetLayerData(doc, layer_settings)
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       doc.AddUndo(c4d.UNDOTYPE_NEW, layer)

       #prevent copies in obj manager
       #objectsListNew=[]
       #for l in LayersList:
       #    n=l.GetName()
       #    if n == name:
       #       objectsListNew.append(1)
       #if len(objectsListNew) >= 2:
       #     return

       #end undo action
       doc.EndUndo()

       #update scene
       c4d.EventAdd()

if __name__=='__main__':
  divider_layer(name_null[:20],color_layer_divider)
  add_divider("_dividers_",color_divider)
  all_organizer("_cameras_",color_cams, "_cameras_")
  add_divider("_dividers_",color_divider)
  all_organizer("_lights_",color_lights, "_lights_")
  add_divider("_dividers_",color_divider)
  all_organizer("_geometry_",color_geo, "_geo_")
  add_divider("_dividers_",color_divider)
  divider_layer(name_null[:19],color_layer_divider)