from winreg import REG_FULL_RESOURCE_DESCRIPTOR
from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 256
height = 256

# Materiales

snow = Material(diffuse = (0.6, 0.6, 0.6), spec = 16, matType= OPAQUE)
wood = Material(diffuse = (0.5, 0.2, 0), spec = 8, matType= OPAQUE)
grass = Material(diffuse = (0, 0.5, 0), spec = 8, matType= OPAQUE)
marble = Material(diffuse = (0.95, 0.95, 0.95), spec = 8, matType= REFLECTIVE)

mirror = Material(diffuse = (0.9, 0, 0.9), spec = 64, matType = REFLECTIVE)
# mirror2 = Material(diffuse = (0.5, 0.8, 0.9), spec = 64, matType = REFLECTIVE)

water = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.01, matType = OPAQUE)
yellowSubmarine = Material(diffuse = (0, 0.9, 0.9), spec = 64, ior = 2.45, matType = REFLECTIVE)
earth = Material(texture = Texture('earthDay.bmp'), matType = OPAQUE)

rtx = Raytracer(width, height)

rtx.envMap = Texture("map.bmp")

# rtx.lights.append( AmbientLight(intensity = 0.1 ))
# rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))

rtx.lights.append( PointLight(point = (0, 0, 0)))
rtx.scene.append(Plane(position= (0,-13,0), normal= (0,1,0), material= yellowSubmarine))
rtx.scene.append(Plane(position= (0,13,0), normal= (0,1,0), material= yellowSubmarine))
rtx.scene.append(Plane(position= (50,0,0), normal= (1,0,0), material= wood))
rtx.scene.append(Plane(position= (-50,0,0), normal= (1,0,0), material= snow))
rtx.scene.append(Plane(position= (0,0,50), normal= (0,0,1), material= grass))

#cajas
rtx.scene.append(AABB(position=(2,1,-10), size=(2,2,2), material= grass))
rtx.scene.append(AABB(position=(-2,1,-10), size=(2,2,2), material= mirror))


rtx.glRender()

rtx.glFinish("output.bmp")