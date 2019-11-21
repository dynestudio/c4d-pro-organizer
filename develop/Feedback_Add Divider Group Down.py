import c4d
 
def add_divider(name, color):


       root = doc.GetLayerObjectRoot()
       LayersList = root.GetChildren() 

       names=[]    
       layers=[]
       for l in LayersList:
           n=l.GetName()
           names.append(n)
           layers.append((n,l))


       if not name in names:


           c4d.CallCommand(100004738) # New Layer
           LayersList = root.GetChildren() 
           layer=LayersList[-1]
           layer.SetName(name)  
 
           layer[c4d.ID_LAYER_COLOR] =color 

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       Null = c4d.BaseObject(5140)
       Null[c4d.ID_BASELIST_NAME] = "______________________________Group Name" #Name of null
       Null[c4d.ID_LAYER_LINK] = layer
       Null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(Null)
       
       c4d.EventAdd()


color_divider=c4d.Vector(1,1,1) # Layer Color
add_divider("_dividers_",color_divider)

def move_divider_down():
    

    ActiveDocument = doc.GetDocument()
    ObjectsList = doc.GetObjects()
    FirstObject = doc.GetFirstObject()
    ActiveObject = doc.GetActiveObject()
    FirstObject.InsertAfter(ActiveObject)
    c4d.EventAdd()
    
if __name__=='__main__':
    move_divider_down()