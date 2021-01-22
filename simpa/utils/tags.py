# The MIT License (MIT)
#
# Copyright (c) 2018 Computer Assisted Medical Interventions Group, DKFZ
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated simpa_documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np


class Tags:
    """
    This class contains all 'Tags' for the use in the settings dictionary as well as strings that are used in SIMPA
    as naming conventions.
    Every Tag that is intended to be used as a key in the settings dictionary is represented by a tuple.
    The first element of the tuple is a string that corresponds to the name of the Tag.
    The second element of the tuple is a data type or a tuple of data types.
    The values that are assigned to the keys in the settings should match these data types.
    Their usage within the SIMPA package is divided in "SIMPA package", "module X", "adapter Y", "class Z" and
    "naming convention".
    """

    """
    General settings
    """

    SIMULATION_PATH = ("simulation_path", str)
    """
    Absolute path to the folder where the SIMPA output is saved.\n
    Usage: SIMPA package
    """

    VOLUME_NAME = ("volume_name", str)
    """
    Name of the SIMPA output file.\n
    Usage: SIMPA package
    """

    WAVELENGTHS = ("wavelengths", (list, range, tuple, np.ndarray))
    """
    Iterable of all the wavelengths used for the simulation.\n
    Usage: SIMPA package
    """

    WAVELENGTH = ("wavelength", (int, np.integer))
    """
    Single wavelength used for the current simulation.\n
    Usage: SIMPA package
    """

    RANDOM_SEED = ("random_seed", (int, np.integer))
    """
    Random seed for numpy and torch.\n
    Usage: SIMPA package
    """

    TISSUE_PROPERTIES_OUPUT_NAME = "properties"
    """
    Location of the simulation properties in the SIMPA output file\n
    Usage: naming convention
    """

    SIMULATION_EXTRACT_FIELD_OF_VIEW = ("extract_field_of_view", bool)
    """
    If True, converts a 3D volume to a 2D volume by extracting the middle slice along the y-axis.\n
    Usage: SIMPA package
    """

    GPU = ("gpu", (bool, np.bool, np.bool_))
    """
    If True, uses all available gpu options of the used modules.\n
    Usage: SIMPA package 
    """

    ACOUSTIC_SIMULATION_3D = ("acoustic_simulation_3d", bool)
    """
    If True, simulates the acoustic forward model in 3D.\n
    Usage: SIMPA package
    """

    MEDIUM_TEMPERATURE_CELCIUS = ("medium_temperature", (int, np.integer, float, np.float))
    """
    Temperature of the simulated volume.\n
    Usage: module noise_simulation
    """

    """
    Volume Creation Settings
    """

    VOLUME_CREATOR = ("volume_creator", str)
    """
    Choice of the volume creator adapter.\n 
    Usage: module volume_creation, module device_digital_twins
    """

    VOLUME_CREATOR_VERSATILE = "volume_creator_versatile"
    """
    Corresponds to the ModelBasedVolumeCreator.\n
    Usage: module volume_creation, naming convention
    """

    VOLUME_CREATOR_SEGMENTATION_BASED = "volume_creator_segmentation_based"
    """
    Corresponds to the SegmentationBasedVolumeCreator.\n
    Usage: module volume_creation, naming convention
    """

    INPUT_SEGMENTATION_VOLUME = ("input_segmentation_volume", np.ndarray)
    """
    Array that defines a segmented volume.\n
    Usage: adapter segmentation_based_volume_creator
    """

    SEGMENTATION_CLASS_MAPPING = ("segmentation_class_mapping", dict)
    """
    Mapping that assigns every class in the INPUT_SEGMENTATION_VOLUME a MOLECULE_COMPOSITION.\n
    Usage: adapter segmentation_based_volume_creator
    """

    PRIORITY = ("priority", (int, np.integer, float, np.float))
    """
    Number that corresponds to a priority of the assigned structure. If another structure occupies the same voxel 
    in a volume, the structure with a higher priority will be preferred.\n
    Usage: adapter versatile_volume_creator
    """

    MOLECULE_COMPOSITION = ("molecule_composition", list)
    """
    List that contains all the molecules within a structure.\n
    Usage: module volume_creation
    """

    SIMULATE_DEFORMED_LAYERS = ("simulate_deformed_layers", bool)
    """
    If True, the horizontal layers are deformed according to the DEFORMED_LAYERS_SETTINGS.\n
    Usage: adapter versatile_volume_creation
    """

    DEFORMED_LAYERS_SETTINGS = ("deformed_layers_settings", dict)
    """
    Settings that contain the functional which defines the deformation of the layers.\n
    Usage: adapter versatile_volume_creation
    """

    BACKGROUND = "Background"
    """
    Corresponds to the name of a structure.\n
    Usage: adapter versatile_volume_creation, naming convention
    """

    ADHERE_TO_DEFORMATION = ("adhere_to_deformation", bool)
    """
    If True, a structure will be shifted according to the deformation.\n
    Usage: adapter versatile_volume_creation
    """

    DEFORMATION_X_COORDINATES_MM = "deformation_x_coordinates"
    """
    Mesh that defines the x coordinates of the deformation.\n
    Usage: adapter versatile_volume_creation, naming convention
    """

    DEFORMATION_Y_COORDINATES_MM = "deformation_y_coordinates"
    """
    Mesh that defines the y coordinates of the deformation.\n
    Usage: adapter versatile_volume_creation, naming convention
    """

    DEFORMATION_Z_ELEVATIONS_MM = "deformation_z_elevation"
    """
    Mesh that defines the z coordinates of the deformation.\n
    Usage: adapter versatile_volume_creation, naming convention
    """

    MAX_DEFORMATION_MM = "max_deformation"
    """
    Maximum deformation in z-direction.\n
    Usage: adapter versatile_volume_creation, naming convention
    """

    """
    Structure Settings
    """

    CONSIDER_PARTIAL_VOLUME = ("consider_partial_volume", bool)
    """
    If True, the structure will be generated with its edges only occupying a partial volume of the voxel.\n
    Usage: adapter versatile_volume_creation
    """

    STRUCTURE_START_MM = ("structure_start", (list, tuple, np.ndarray))
    """
    Beginning of the structure as [x, y, z] coordinates in the generated volume.\n
    Usage: adapter versatile_volume_creation, class GeometricalStructure
    """

    STRUCTURE_END_MM = ("structure_end", (list, tuple, np.ndarray))
    """
    Ending of the structure as [x, y, z] coordinates in the generated volume.\n
    Usage: adapter versatile_volume_creation, class GeometricalStructure
    """

    STRUCTURE_RADIUS_MM = ("structure_radius", (int, np.integer, float, np.float, np.ndarray))
    """
    Radius of the structure.\n
    Usage: adapter versatile_volume_creation, class GeometricalStructure
    """

    STRUCTURE_ECCENTRICITY = ("structure_excentricity", (int, np.integer, float, np.float, np.ndarray))
    """
    Eccentricity of the structure.\n
    Usage: adapter versatile_volume_creation, class EllipticalTubularStructure
    """

    STRUCTURE_FIRST_EDGE_MM = ("structure_first_edge_mm", (list, tuple, np.ndarray))
    """
    Edge of the structure as [x, y, z] vector starting from STRUCTURE_START_MM in the generated volume.\n
    Usage: adapter versatile_volume_creation, class ParallelepipedStructure
    """

    STRUCTURE_SECOND_EDGE_MM = ("structure_second_edge_mm", (list, tuple, np.ndarray))
    """
    Edge of the structure as [x, y, z] vector starting from STRUCTURE_START_MM in the generated volume.\n
    Usage: adapter versatile_volume_creation, class ParallelepipedStructure
    """

    STRUCTURE_THIRD_EDGE_MM = ("structure_third_edge_mm", (list, tuple, np.ndarray))
    """
    Edge of the structure as [x, y, z] vector starting from STRUCTURE_START_MM in the generated volume.\n
    Usage: adapter versatile_volume_creation, class ParallelepipedStructure
    """

    STRUCTURE_X_EXTENT_MM = ("structure_x_extent_mm", (int, np.integer, float, np.float))
    """
    X-extent of the structure in the generated volume.\n
    Usage: adapter versatile_volume_creation, class RectangularCuboidStructure
    """

    STRUCTURE_Y_EXTENT_MM = ("structure_y_extent_mm", (int, np.integer, float, np.float))
    """
    Y-extent of the structure in the generated volume.\n
    Usage: adapter versatile_volume_creation, class RectangularCuboidStructure
    """

    STRUCTURE_Z_EXTENT_MM = ("structure_z_extent_mm", (int, np.integer, float, np.float))
    """
    Z-extent of the structure in the generated volume.\n
    Usage: adapter versatile_volume_creation, class RectangularCuboidStructure
    """

    STRUCTURE_BIFURCATION_LENGTH_MM = ("structure_bifurcation_length_mm", (int, np.integer, float, np.float))
    """
    Length after which a VesselStructure will bifurcate.\n
    Usage: adapter versatile_volume_creation, class VesselStructure
    """

    STRUCTURE_CURVATURE_FACTOR = ("structure_curvature_factor", (int, np.integer, float, np.float))
    """
    Factor that determines how strongly a vessel tree is curved.\n
    Usage: adapter versatile_volume_creation, class VesselStructure
    """

    STRUCTURE_RADIUS_VARIATION_FACTOR = ("structure_radius_variation_factor", (int, np.integer, float, np.float))
    """
    Factor that determines how strongly a the radius of vessel tree varies.\n
    Usage: adapter versatile_volume_creation, class VesselStructure
    """

    STRUCTURE_DIRECTION = ("structure_direction", (list, tuple, np.ndarray))
    """
    Direction as [x, y, z] vector starting from STRUCTURE_START_MM in which the vessel will grow.\n
    Usage: adapter versatile_volume_creation, class VesselStructure
    """

    """
    Digital Device Twin Settings
    """

    DIGITAL_DEVICE = ("digital_device", str)
    """
    Digital device that is chosen as illumination source and detector for the simulation.\n
    Usage: SIMPA package
    """

    DIGITAL_DEVICE_MSOT = "digital_device_msot"
    """
    Corresponds to the MSOTAcuityEcho device.\n
    Usage: SIMPA package, naming convention
    """

    DIGITAL_DEVICE_RSOM = "digital_device_rsom"
    """
    Corresponds to the RSOMExplorerP50 device.\n
    Usage: SIMPA package, naming convention
    """

    DIGITAL_DEVICE_POSITION = ("digital_device_position", (list, tuple, np.ndarray))
    """
    Position in [x, y, z] coordinates of the device in the generated volume.\n
    Usage: SIMPA package
    """

    """
    Optical model settings
    """

    RUN_OPTICAL_MODEL = ("run_optical_forward_model", bool)
    """
    If True, the simulation will run the optical forward model.\n
    Usage: module core (simulate.py)
    """

    OPTICAL_MODEL_OUTPUT_NAME = "optical_forward_model_output"
    """
    Location of the optical forward model output in the SIMPA output file.\n
    Usage: naming convention
    """

    OPTICAL_MODEL_BINARY_PATH = ("optical_model_binary_path", str)
    """
    Absolute path of the location of the optical forward model binary.\n
    Usage: module optical_simulation
    """

    OPTICAL_MODEL_NUMBER_PHOTONS = ("optical_model_number_of_photons", (int, np.integer, float, np.float))
    """
    Number of photons used in the optical simulation.\n
    Usage: module optical_simulation
    """

    OPTICAL_MODEL_ILLUMINATION_GEOMETRY_XML_FILE = ("optical_model_illumination_geometry_xml_file", str)
    """
    Absolute path of the location of the optical forward model illumination geometry.\n
    Usage: module optical_simulation
    """

    LASER_PULSE_ENERGY_IN_MILLIJOULE = ("laser_pulse_energy_in_millijoule", (int, np.integer, float, np.float, list,
                                                                             range, tuple, np.ndarray))
    """
    Laser pulse energy used in the optical simulation.\n
    Usage: module optical_simulation
    """

    OPTICAL_MODEL_FLUENCE = "fluence"
    """
    Location of the optical forward model output fluence in the SIMPA output file.\n
    Usage: naming convention
    """

    OPTICAL_MODEL_INITIAL_PRESSURE = "initial_pressure"
    """
    Location of the optical forward model output initial pressure in the SIMPA output file.\n
    Usage: naming convention
    """

    OPTICAL_MODEL_UNITS = "units"
    """
    Location of the optical forward model output units in the SIMPA output file.\n
    Usage: naming convention
    """

    ILLUMINATION_TYPE = ("optical_model_illumination_type", str)
    """
    Type of the illumination geometry used in mcx.\n
    Usage: module optical_modelling, adapter mcx_adapter
    """

    # Illumination parameters
    ILLUMINATION_POSITION = ("illumination_position", (list, tuple, np.ndarray))
    """
    Position of the photon source in [x, y, z] coordinates used in mcx.\n
    Usage: module optical_modelling, adapter mcx_adapter
    """

    ILLUMINATION_DIRECTION = ("illumination_direction", (list, tuple, np.ndarray))
    """
    Direction of the photon source as [x, y, z] vector used in mcx.\n
    Usage: module optical_modelling, adapter mcx_adapter
    """

    ILLUMINATION_PARAM1 = ("illumination_param1", (list, tuple, np.ndarray))
    """
    First parameter group of the specified illumination type as [x, y, z, w] vector used in mcx.\n
    Usage: module optical_modelling, adapter mcx_adapter
    """

    ILLUMINATION_PARAM2 = ("illumination_param2", (list, tuple, np.ndarray))
    """
    Second parameter group of the specified illumination type as [x, y, z, w] vector used in mcx.\n
    Usage: module optical_modelling, adapter mcx_adapter
    """

    TIME_STEP = ("time_step", (int, np.integer, float, np.float))
    """
    Temporal resolution of mcx.\n
    Usage: adapter mcx_adapter
    """

    TOTAL_TIME = ("total_time", (int, np.integer, float, np.float))
    """
    Total simulated time in mcx.\n
    Usage: adapter mcx_adapter
    """

    # Supported illumination types - implemented in mcx
    ILLUMINATION_TYPE_PENCIL = "pencil"
    """
    Corresponds to pencil source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_PENCILARRAY = "pencilarray"
    """
    Corresponds to pencilarray source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_DISK = "disk"
    """
    Corresponds to disk source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_SLIT = "slit"
    """
    Corresponds to slit source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_GAUSSIAN = "gaussian"
    """
    Corresponds to gaussian source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_PATTERN = "pattern"
    """
    Corresponds to pattern source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_PATTERN_3D = "pattern3d"
    """
    Corresponds to pattern3d source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_PLANAR = "planar"
    """
    Corresponds to planar source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_FOURIER = "fourier"
    """
    Corresponds to fourier source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_FOURIER_X = "fourierx"
    """
    Corresponds to fourierx source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_FOURIER_X_2D = "fourierx2d"
    """
    Corresponds to fourierx2d source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_DKFZ_PAUS = "pasetup"  # TODO more explanatory rename of pasetup
    """
    Corresponds to pasetup source in mcx. The geometrical definition is described in:\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_MSOT_ACUITY_ECHO = "msot_acuity_echo"
    """
    Corresponds to msot_acuity_echo source in mcx. The device is manufactured by iThera Medical, Munich, Germany
    (https: // www.ithera-medical.com / products / msot-acuity /).\n
    Usage: adapter mcx_adapter, naming convention
    """

    ILLUMINATION_TYPE_RING = "ring"
    """
    Corresponds to ring source in mcx.\n
    Usage: adapter mcx_adapter, naming convention
    """

    # Supported optical models
    OPTICAL_MODEL = ("optical_model", str)
    """
    Choice of the used optical model.\n
    Usage: module optical_simulation
    """

    OPTICAL_MODEL_MCXYZ = "mcxyz"
    """
    Corresponds to the mcxyz simulation.\n
    Usage: module optical_simulation, naming convention
    """

    OPTICAL_MODEL_MCX = "mcx"
    """
    Corresponds to the mcx simulation.\n
    Usage: module optical_simulation, naming convention
    """

    OPTICAL_MODEL_TEST = "simpa_tests"
    """
    Corresponds to an adapter for testing purposes only.\n
    Usage: module optical_simulation, naming convention
    """

    # Supported acoustic models
    ACOUSTIC_MODEL = ("acoustic_model", str)
    """
    Choice of the used acoustic model.\n
    Usage: module acoustic_simulation
    """

    ACOUSTIC_MODEL_K_WAVE = "kwave"
    """
    Corresponds to the kwave simulaiton.\n
    Usage: module acoustic_simulation, naming convention
    """

    K_WAVE_SPECIFIC_DT = ("dt_acoustic_sim", (int, np.integer, float, np.float))
    """
    Temporal resolution of kwave.\n
    Usage: adapter KwaveAcousticForwardModel, adapter TimeReversalAdapter
    """

    K_WAVE_SPECIFIC_NT = ("Nt_acoustic_sim", (int, np.integer, float, np.float))
    """
    Total time steps simulated by kwave.\n
    Usage: adapter KwaveAcousticForwardModel, adapter TimeReversalAdapter
    """

    ACOUSTIC_MODEL_TEST = "simpa_tests"
    """
    Corresponds to an adapter for testing purposes only.\n
    Usage: module acoustic_simulation, naming convention
    """

    ACOUSTIC_MODEL_SCRIPT_LOCATION = ("acoustic_model_script_location", str)
    """
    Absolute path of the location of the acoustic_simulation folder in the SIMPA core module.\n
    Usage: module acoustic_simulation
    """

    TIME_REVEARSAL_SCRIPT_LOCATION = ("time_revearsal_script_location", str)
    """
    Absolute path of the location of the image_reconstruction folder in the SIMPA core module.\n
    Usage: adapter TimeReversalAdapter
    """

    """
    Acoustic model settings
    """

    RUN_ACOUSTIC_MODEL = ("run_acoustic_forward_model", (bool, np.bool, np.bool_))
    """
    If True, the simulation will run the acoustic forward model.\n
    Usage: module core (simulate.py)
    """

    ACOUSTIC_MODEL_BINARY_PATH = ("acoustic_model_binary_path", str)
    """
    Absolute path of the location of the acoustic forward model binary.\n
    Usage: module optical_simulation
    """

    ACOUSTIC_MODEL_OUTPUT_NAME = "acoustic_forward_model_output"
    """
    Location of the acoustic forward model output in the SIMPA output file.\n
    Usage: naming convention
    """

    RECORDMOVIE = ("record_movie", (bool, np.bool, np.bool_))
    """
    If True, a movie of the kwave simulation will be recorded.\n
    Usage: adapter KwaveAcousticForwardModel
    """

    MOVIENAME = ("movie_name", str)
    """
    Name of the movie recorded by kwave.\n
    Usage: adapter KwaveAcousticForwardModel
    """

    ACOUSTIC_LOG_SCALE = ("acoustic_log_scale", (bool, np.bool, np.bool_))
    """
    If True, the movie of the kwave simulation will be recorded in a log scale.\n
    Usage: adapter KwaveAcousticForwardModel
    """

    TIME_SERIES_DATA = "time_series_data"
    """
    Location of the time series data in the SIMPA output file.\n
    Usage: naming convention
    """

    TIME_SERIES_DATA_NOISE = "time_series_data_noise"
    """
    Location of the time series data with applied noise in the SIMPA output file.\n
    Usage: naming convention
    """

    # Reconstruction settings
    PERFORM_IMAGE_RECONSTRUCTION = ("perform_image_reconstruction", (bool, np.bool, np.bool_))
    """
    If True, the simulation will run the image reconstruction.\n
    Usage: module core (simulate.py)
    """

    RECONSTRUCTION_OUTPUT_NAME = ("reconstruction_result", str)
    """
    Absolute path of the image reconstruction result.\n
    Usage: adapter MitkBeamformingAdapter
    """

    RECONSTRUCTION_ALGORITHM = ("reconstruction_algorithm", str)
    """
    Choice of the used reconstruction algorithm.\n
    Usage: module image_reconstruction
    """

    RECONSTRUCTION_ALGORITHM_DAS = "DAS"
    """
    Corresponds to the reconstruction algorithm DAS with the MitkBeamformingAdapter.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_ALGORITHM_DMAS = "DMAS"
    """
    Corresponds to the reconstruction algorithm DMAS with the MitkBeamformingAdapter.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_ALGORITHM_SDMAS = "sDMAS"
    """
    Corresponds to the reconstruction algorithm sDMAS with the MitkBeamformingAdapter.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_ALGORITHM_TIME_REVERSAL = "time_reversal"
    """
    Corresponds to the reconstruction algorithm Time Reversal with TimeReversalAdapter.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_ALGORITHM_TEST = "TEST"
    """
    Corresponds to an adapter for testing purposes only.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_ALGORITHM_BACKPROJECTION = "backprojection"
    """
    Corresponds to the reconstruction algorithm Backprojection with BackprojectionAdapter.\n
    Usage: module image_reconstruction, naming convention
    """

    RECONSTRUCTION_INVERSE_CRIME = ("reconstruction_inverse_crime", (bool, np.bool, np.bool_))
    """
    If True, the Time Reversal reconstruction will commit the "inverse crime".\n
    Usage: TimeReversalAdapter
    """

    RECONSTRUCTION_MITK_BINARY_PATH = ("reconstruction_mitk_binary_path", str)
    """
    Absolute path to the Mitk Beamforming script.\n
    Usage: adapter MitkBeamformingAdapter
    """

    RECONSTRUCTION_MITK_SETTINGS_XML = ("reconstruction_mitk_settings_xml", str)
    """
    Absolute path to the Mitk Beamforming script settings.\n
    Usage: adapter MitkBeamformingAdapter
    """

    RECONSTRUCTION_BMODE_METHOD = ("reconstruction_bmode_method", str)
    """
    Choice of the B-Mode method used in the Mitk Beamforming.\n
    Usage: adapter MitkBeamformingAdapter
    """

    RECONSTRUCTION_BMODE_METHOD_ABS = "Abs"
    """
    Corresponds to the absolute value as the B-Mode method used in the Mitk Beamforming.\n
    Usage: adapter MitkBeamformingAdapter, naming convention
    """

    RECONSTRUCTION_BMODE_METHOD_HILBERT_TRANSFORM = "EnvelopeDetection"
    """
    Corresponds to the Hilbert transform as the B-Mode method used in the Mitk Beamforming.\n
    Usage: adapter MitkBeamformingAdapter, naming convention
    """

    RECONSTRUCTED_DATA = "reconstructed_data"
    """
    Location of the reconstructed data in the SIMPA output file.\n
    Usage: naming convention
    """

    RECONSTRUCTED_DATA_NOISE = "reconstructed_data_noise"
    """
    Location of the reconstructed data with applied noise in the SIMPA output file.\n
    Usage: naming convention
    """

    RECONSTRUCTION_MODE = ("reconstruction_mode", str)
    """
    Choice of the reconstruction mode used in the Backprojection.\n
    Usage: adapter BackprojectionAdapter
    """

    RECONSTRUCTION_MODE_DIFFERENTIAL = "differential"
    """
    Corresponds to the differential mode used in the Backprojection.\n
    Usage: adapter BackprojectionAdapter, naming_convention
    """

    RECONSTRUCTION_MODE_PRESSURE = "pressure"
    """
    Corresponds to the pressure mode used in the Backprojection.\n
    Usage: adapter BackprojectionAdapter, naming_convention
    """

    RECONSTRUCTION_MODE_FULL = "full"
    """
    Corresponds to the full mode used in the Backprojection.\n
    Usage: adapter BackprojectionAdapter, naming_convention
    """

    """
    Upsampling settings
    """

    CROP_IMAGE = ("crop_image", bool)
    """
    If True, the PA image cropped in the image processing.\n
    Usage: module process
    """

    CROP_POWER_OF_TWO = ("crop_power_of_two", bool)
    """
    If True, the PA image cropped to the shape as the nearest power of two in the image processing.\n
    Usage: module process
    """

    PERFORM_UPSAMPLING = ("sample", bool)
    """
    If True, the PA image upsampled in the image processing.\n
    Usage: module process
    """

    UPSAMPLING_METHOD = ("upsampling_method", str)
    """
    Choice of the upsampling method used in the image processing.\n
    Usage: module process
    """

    UPSAMPLING_METHOD_DEEP_LEARNING = "deeplearning"
    """
    Corresponds to deep learning as the upsampling method used in the image processing.\n
    Usage: module process, naming concention
    """

    UPSAMPLING_METHOD_NEAREST_NEIGHBOUR = "nearestneighbour"
    """
    Corresponds to nearest neighbour as the upsampling method used in the image processing.\n
    Usage: module process, naming concention
    """

    UPSAMPLING_METHOD_BILINEAR = "bilinear"
    """
    Corresponds to the bilinear upsampling method used in the image processing.\n
    Usage: module process, naming concention
    """

    UPSAMPLING_METHOD_LANCZOS2 = "lanczos2"
    """
    Corresponds to lanczos with kernel size 2 as the upsampling method used in the image processing.\n
    Usage: module process, naming concention
    """

    UPSAMPLING_METHOD_LANCZOS3 = "lanczos3"
    """
    Corresponds to lanczos with kernel size 3 as the upsampling method used in the image processing.\n
    Usage: module process, naming concention
    """

    UPSAMPLING_SCRIPT = ("upsampling_script", str)
    """
    Name of the upsampling script used for the lanczos upsampling.\n
    Usage: module process
    """

    UPSAMPLING_SCRIPT_LOCATION = ("upsampling_script_location", str)
    """
    Absolute path to the upsampling script used for the lanczos upsampling.\n
    Usage: module process
    """

    UPSCALE_FACTOR = ("upscale_factor", (int, float, np.int_, np.float_))
    """
    Upscale factor of the upsampling in the image processing.\n
    Usage: module process
    """

    DL_MODEL_PATH = ("dl_model_path", str)
    """
    Absolute path to the deep learning model used for the deep learning upsampling.\n
    Usage: module process
    """

    # physical property volume types
    PROPERTY_ABSORPTION_PER_CM = "mua"
    PROPERTY_SCATTERING_PER_CM = "mus"
    PROPERTY_ANISOTROPY = "g"
    PROPERTY_OXYGENATION = "oxy"
    PROPERTY_SEGMENTATION = "seg"
    """
    We define PROPERTY_GRUNEISEN_PARAMETER to contain all wavelength-independent constituents of the PA signal.
    This means that it contains the percentage of absorbed light converted into heat.
    Naturally, one could make an argument that this should not be the case, however, it simplifies the usage of 
    this tool.
    """
    PROPERTY_GRUNEISEN_PARAMETER = "gamma"
    PROPERTY_SPEED_OF_SOUND = "sos"
    PROPERTY_DENSITY = "density"
    PROPERTY_ALPHA_COEFF = "alpha_coeff"
    PROPERTY_SENSOR_MASK = "sensor_mask"
    PROPERTY_DIRECTIVITY_ANGLE = "directivity_angle"

    # Air layer
    AIR_LAYER = ("airlayer", bool)
    AIR_LAYER_HEIGHT_MM = ("air_layer_height", (int, np.integer, float, np.float))

    # Gel Pad Layer
    GELPAD_LAYER = ("gelpad", bool)
    GELPAD_LAYER_HEIGHT_MM = ("gelpad_layer_height_mm", (int, np.integer, float, np.float))

    # Volume geometry settings
    SPACING_MM = ("voxel_spacing_mm", (int, np.integer, float, np.float))
    DIM_VOLUME_X_MM = ("volume_x_dim_mm", (int, np.integer, float, np.float))
    DIM_VOLUME_Y_MM = ("volume_y_dim_mm", (int, np.integer, float, np.float))
    DIM_VOLUME_Z_MM = ("volume_z_dim_mm", (int, np.integer, float, np.float))

    # 2D Acoustic Medium Properties
    MEDIUM_SOUND_SPEED_HOMOGENEOUS = ("medium_sound_speed_homogeneous", bool)
    MEDIUM_SOUND_SPEED = "medium_sound_speed"
    MEDIUM_DENSITY_HOMOGENEOUS = "medium_density_homogeneous"
    MEDIUM_DENSITY = "medium_density"
    MEDIUM_ALPHA_COEFF_HOMOGENEOUS = "medium_alpha_coeff_homogeneous"
    MEDIUM_ALPHA_COEFF = "medium_alpha_coeff"
    MEDIUM_ALPHA_POWER = ("medium_alpha_power", (int, np.integer, float, np.float))
    MEDIUM_NONLINEARITY = "medium_nonlinearity"

    # PML parameters

    PMLSize = ("pml_size", (list, tuple, np.ndarray))
    PMLAlpha = ("pml_alpha", (int, np.integer, float, np.float))
    PMLInside = ("pml_inside", (bool, np.bool, np.bool_))
    PlotPML = ("plot_pml", (bool, np.bool, np.bool_))

    # Acoustic Sensor Properties
    SENSOR_MASK = "sensor_mask"
    SENSOR_RECORD = ("sensor_record", str)
    SENSOR_CENTER_FREQUENCY_HZ = ("sensor_center_frequency", (int, np.integer, float, np.float))
    SENSOR_BANDWIDTH_PERCENT = ("sensor_bandwidth", (int, np.integer, float, np.float))
    SENSOR_DIRECTIVITY_HOMOGENEOUS = "sensor_directivity_homogeneous"
    SENSOR_DIRECTIVITY_ANGLE = "sensor_directivity_angle"
    SENSOR_DIRECTIVITY_SIZE_M = ("sensor_directivity_size", (int, np.integer, float, np.float))
    SENSOR_DIRECTIVITY_PATTERN = "sensor_directivity_pattern"
    SENSOR_ELEMENT_PITCH_MM = "sensor_element_pitch"
    SENSOR_SAMPLING_RATE_MHZ = ("sensor_sampling_rate_mhz", (int, np.integer, float, np.float))
    SENSOR_NUM_ELEMENTS = ("sensor_num_elements", (int, np.integer))
    SENSOR_NUM_USED_ELEMENTS = "sensor_num_used_elements"
    SENSOR_CONCAVE = "concave"
    SENSOR_RADIUS_MM = "sensor_radius_mm"
    SENSOR_LINEAR = "linear"

    # Noise properties
    APPLY_NOISE_MODEL = ("apply_noise_model", bool)
    NOISE_MODEL = "noise_model"
    NOISE_MODEL_GAUSSIAN = "noise_model_gaussian"
    NOISE_MEAN = "noise_mean"
    NOISE_STD = "noise_std"
    NOISE_MODEL_OUTPUT_NAME = "noise_model_output"
    NOISE_MODEL_PATH = "noise_model_path"

    # Constant Tissue Properties
    KEY_CONSTANT_PROPERTIES = "constant_properties"
    KEY_MUA = "mua"
    KEY_MUS = "mus"
    KEY_G = "g"

    # Tissue Properties Settings
    KEY_B = "B"
    KEY_B_MIN = "B_min"
    KEY_B_MAX = "B_max"
    KEY_W = "W"
    KEY_W_MAX = "w_max"
    KEY_W_MIN = "w_min"
    KEY_F = "F"
    KEY_F_MAX = "f_max"
    KEY_F_MIN = "f_min"
    KEY_M = "M"
    KEY_M_MAX = "m_max"
    KEY_M_MIN = "m_min"
    KEY_OXY = "OXY"
    KEY_OXY_MAX = "oxy_max"
    KEY_OXY_MIN = "oxy_min"
    KEY_MUSP500 = "musp500"
    KEY_F_RAY = "f_ray"
    KEY_B_MIE = "b_mie"
    KEY_ANISOTROPY = "anisotropy"

    # Structures
    STRUCTURES = ("structures", dict)
    HORIZONTAL_LAYER_STRUCTURE = "HorizontalLayerStructure"
    CIRCULAR_TUBULAR_STRUCTURE = "CircularTubularStructure"
    ELLIPTICAL_TUBULAR_STRUCTURE = "EllipticalTubularStructure"
    SPHERICAL_STRUCTURE = "SphericalStructure"
    PARALLELEPIPED_STRUCTURE = "ParallelepipedStructure"
    RECTANGULAR_CUBOID_STRUCTURE = "RectangularCuboidStructure"

    CHILD_STRUCTURES = "child_structures"
    STRUCTURE_TYPE = ("structure_type", str)
    STRUCTURE_SEGMENTATION_TYPE = "structure_segmentation_type"
    STRUCTURE_TISSUE_PROPERTIES = "structure_tissue_properties"

    STRUCTURE_CENTER_DEPTH_MIN_MM = "structure_depth_min_mm"
    STRUCTURE_CENTER_DEPTH_MAX_MM = "structure_depth_max_mm"

    STRUCTURE_BACKGROUND = "structure_background"

    STRUCTURE_LAYER = "structure_layer"
    STRUCTURE_THICKNESS_MIN_MM = "structure_thickness_min_mm"
    STRUCTURE_THICKNESS_MAX_MM = "structure_thickness_max_mm"

    STRUCTURE_TUBE = "structure_tube"
    STRUCTURE_RADIUS_MIN_MM = "structure_radius_min_mm"
    STRUCTURE_RADIUS_MAX_MM = "structure_radius_max_mm"
    STRUCTURE_FORCE_ORTHOGONAL_TO_PLANE = "structure_force_orthogonal_to_plane"
    STRUCTURE_TUBE_CENTER_X_MIN_MM = "structure_tube_start_x_min_mm"
    STRUCTURE_TUBE_CENTER_X_MAX_MM = "structure_tube_start_x_max_mm"

    STRUCTURE_ELLIPSE = "structure_ellipse"
    STRUCTURE_MIN_ECCENTRICITY = "structure_eccentricity_min"
    STRUCTURE_MAX_ECCENTRICITY = "structure_eccentricity_max"

    STRUCTURE_DISTORTED_LAYERS = "distorted_layers"
    STRUCTURE_DISTORTED_LAYERS_ELEVATION = "distorted_layers_elevation"

    UNITS_ARBITRARY = "arbitrary_unity"
    UNITS_PRESSURE = "newton_per_meters_squared"

    """
    IO settings
    """

    SIMPA_OUTPUT_PATH = ("simpa_output_path", str)
    SIMPA_OUTPUT_NAME = "simpa_output.hdf5"
    SETTINGS_JSON = "settings_json"
    SETTINGS_JSON_PATH = "settings_json_path"
    SETTINGS = "settings"
    SIMULATION_PROPERTIES = "simulation_properties"
    SIMULATIONS = "simulations"
    UPSAMPLED_DATA = "upsampled_data"
    ORIGINAL_DATA = "original_data"
