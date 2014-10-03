import bpy
import mathutils
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodePropertyChanged

class VectorLengthNode(Node, AnimationNode):
	bl_idname = "VectorLengthNode"
	bl_label = "Vector Length"
	
	def init(self, context):
		self.inputs.new("VectorSocket", "Vector")
		self.outputs.new("FloatSocket", "Length")
		
	def execute(self, input):
		vector = mathutils.Vector(input["Vector"])
		output = {}
		output["Length"] = vector.length
		return output
		
# register
################################
		
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)