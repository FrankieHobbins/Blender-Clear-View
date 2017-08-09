import bpy

bl_info = {
    "name": "Object Clear View",
    "author": "Frankie",
    "version": (0, 1),
    "blender": (2, 79, 0),
    #"location": "View3D > Add > Mesh > New Object",
    "description": "shows objects with name containing string clearly, assign bpy.ops.object.clear_view('INVOKE_DEFAULT') to a key",
    "warning": "",
    "wiki_url": "",
    "category": "3D view",
    }

class ClearView(bpy.types.Operator):
    bl_idname = "object.clear_view"
    bl_label = "Object Clear View"

    my_string = bpy.props.StringProperty(name="String to isolate")

    def execute(self, context):
        s = self.my_string        
        i = 0

        for sl in bpy.context.scene.layers:
            bpy.context.scene.layers[i] = False
            i += 1

        for o in bpy.context.scene.objects:
            o.hide = True
            if (s in o.name):
                o.hide = False
                i = 0
                for l in o.layers:
                    if (l == True):
                        bpy.context.scene.layers[i] = True
                    i += 1
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(ClearView)
    
def unregister():
    bpy.utils.unregister_class(ClearView)

if __name__ == '__main__':
    register()

# test call
# bpy.ops.object.clear_view('INVOKE_DEFAULT')