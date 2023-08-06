from syned.beamline.shape import Sphere, SphericalCylinder, Convexity, Direction
from shadow4.beam.s4_beam import S4Beam
from shadow4.beamline.s4_optical_element import SurfaceCalculation, S4SphereOpticalElementDecorator
from shadow4.beamline.optical_elements.mirrors.s4_mirror import S4MirrorElement, S4Mirror, ElementCoordinates

class S4SphereMirror(S4Mirror, S4SphereOpticalElementDecorator):
    def __init__(self,
                 name="Sphere Mirror",
                 boundary_shape=None,
                 surface_calculation=SurfaceCalculation.EXTERNAL,
                 is_cylinder=False,
                 cylinder_direction=Direction.TANGENTIAL,
                 convexity=Convexity.UPWARD,
                 radius=1.0,
                 p_focus=0.0,
                 q_focus=0.0,
                 grazing_angle=0.0,
                 # inputs related to mirror reflectivity
                 f_reflec=0,  # reflectivity of surface: 0=no reflectivity, 1=full polarization
                 f_refl=0,  # 0=prerefl file
                 # 1=electric susceptibility
                 # 2=user defined file (1D reflectivity vs angle)
                 # 3=user defined file (1D reflectivity vs energy)
                 # 4=user defined file (2D reflectivity vs energy and angle)
                 file_refl="",  # preprocessor file fir f_refl=0,2,3,4
                 refraction_index=1.0  # refraction index (complex) for f_refl=1
                 ):
        S4SphereOpticalElementDecorator.__init__(self, surface_calculation, is_cylinder, cylinder_direction, convexity,
                                                 radius, p_focus, q_focus, grazing_angle)
        S4Mirror.__init__(self, name, boundary_shape, self.get_surface_shape_instance(),
                          f_reflec, f_refl, file_refl, refraction_index)

        self.__inputs = {
            "name": name,
            "boundary_shape": boundary_shape,
            "surface_calculation": surface_calculation,
            "is_cylinder": is_cylinder,
            "cylinder_direction": cylinder_direction,
            "convexity": convexity,
            "radius": radius,
            "p_focus": p_focus,
            "q_focus": q_focus,
            "grazing_angle": grazing_angle,
            "f_reflec": f_reflec,
            "f_refl": f_refl,
            "file_refl": file_refl,
            "refraction_index": refraction_index,
        }

    def to_python_code(self, data=None):
        txt = "\nfrom shadow4.beamline.optical_elements.mirrors.s4_sphere_mirror import S4SphereMirror"
        txt_pre = """
optical_element = S4SphereMirror(name='{name:s}',boundary_shape=None,
    surface_calculation={surface_calculation:d},is_cylinder={is_cylinder:d},cylinder_direction={cylinder_direction:d},
    convexity={convexity:d},radius={radius:f},p_focus={p_focus:f},q_focus={q_focus:f},
    grazing_angle={grazing_angle:f},
    f_reflec={f_reflec:d},f_refl={f_refl:d},file_refl='{file_refl:s}',refraction_index={refraction_index:g})
    """
        txt += txt_pre.format(**self.__inputs)
        return txt

    def apply_geometrical_model(self, beam):
        ccc = self.get_optical_surface_instance()
        footprint, normal = ccc.apply_specular_reflection_on_beam(beam)
        return footprint, normal

class S4SphereMirrorElement(S4MirrorElement):
    def __init__(self,
                 optical_element: S4SphereMirror = None,
                 coordinates: ElementCoordinates = None,
                 input_beam: S4Beam = None):
        super().__init__(optical_element=optical_element if optical_element is not None else S4SphereMirror(),
                         coordinates=coordinates if coordinates is not None else ElementCoordinates(),
                         input_beam=input_beam)
        if not (isinstance(self.get_optical_element().get_surface_shape(), SphericalCylinder) or
                isinstance(self.get_optical_element().get_surface_shape(), Sphere)):
            raise ValueError("Wrong Optical Element: only Sphere or Spherical Cylinder shape is accepted")

    def to_python_code(self, data=None):
        txt = "\n\n# optical element number XX"
        txt += self.get_optical_element().to_python_code()
        coordinates = self.get_coordinates()
        txt += "\nfrom syned.beamline.element_coordinates import ElementCoordinates"
        txt += "\ncoordinates=ElementCoordinates(p=%g,q=%g,angle_radial=%g)" % \
               (coordinates.p(), coordinates.q(), coordinates.angle_radial())
        txt += "\nfrom shadow4.beamline.optical_elements.mirrors.s4_sphere_mirror import S4SphereMirrorElement"
        txt += "\nbeamline_element = S4SphereMirrorElement(optical_element=optical_element,coordinates=coordinates,input_beam=beam)"
        txt += "\n\nbeam, mirr = beamline_element.trace_beam()"
        return txt

    def duplicate(self):
        return S4SphereMirrorElement(optical_element=self.duplicate_coordinates(),
                                coordinates=self.duplicate_coordinates(),
                                input_beam=self.duplicate_input_beam())
