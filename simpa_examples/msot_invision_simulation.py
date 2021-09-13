"""
SPDX-FileCopyrightText: 2021 Computer Assisted Medical Interventions Group, DKFZ
SPDX-FileCopyrightText: 2021 VISION Lab, Cancer Research UK Cambridge Institute (CRUK CI)
SPDX-License-Identifier: MIT
"""

from simpa.utils import Tags

from simpa.core.simulation import simulate
from simpa.utils.settings import Settings
from simpa.utils.libraries.molecule_library import Molecule, MolecularCompositionGenerator
from simpa.utils.libraries.spectra_library import AbsorptionSpectrumLibrary, AnisotropySpectrumLibrary, \
    ScatteringSpectrumLibrary
from simpa.visualisation.matplotlib_data_visualisation import visualise_data
import numpy as np
from simpa.utils.path_manager import PathManager
from simpa.core import ImageReconstructionModuleDelayAndSumAdapter, \
    OpticalForwardModelMcxAdapter, AcousticForwardModelKWaveAdapter, VolumeCreationModelModelBasedAdapter, \
    FieldOfViewCroppingProcessingComponent, ReconstructionModuleTimeReversalAdapter
from simpa.core.device_digital_twins import *

path_manager = PathManager()

SPEED_OF_SOUND = 1500
SPACING = 0.5
XZ_DIM = 90
Y_DIM = 40


def create_pipeline(_settings: Settings):
    return [
        VolumeCreationModelModelBasedAdapter(settings),
        OpticalForwardModelMcxAdapter(settings),
        AcousticForwardModelKWaveAdapter(settings),
        FieldOfViewCroppingProcessingComponent(settings),
        ReconstructionModuleTimeReversalAdapter(settings)
    ]


def get_device():
    pa_device = InVision256TF(device_position_mm=np.asarray([XZ_DIM/2, Y_DIM/2, XZ_DIM/2]))
    return pa_device


def create_volume():
    inclusion_material = Molecule(volume_fraction=1.0,
                                  anisotropy_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(0.9),
                                  scattering_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(100.0),
                                  absorption_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(4.0),
                                  speed_of_sound=SPEED_OF_SOUND,
                                  alpha_coefficient=1e-4,
                                  density=1000,
                                  gruneisen_parameter=1.0,
                                  name="Inclusion")

    phantom_material = Molecule(volume_fraction=1.0,
                                anisotropy_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(0.9),
                                scattering_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(100.0),
                                absorption_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(0.05),
                                speed_of_sound=SPEED_OF_SOUND,
                                alpha_coefficient=1e-4,
                                density=1000,
                                gruneisen_parameter=1.0,
                                name="Phantom")

    heavy_water = Molecule(volume_fraction=1.0,
                           anisotropy_spectrum=AnisotropySpectrumLibrary.CONSTANT_ANISOTROPY_ARBITRARY(1.0),
                           scattering_spectrum=ScatteringSpectrumLibrary.CONSTANT_SCATTERING_ARBITRARY(0.1),
                           absorption_spectrum=AbsorptionSpectrumLibrary.CONSTANT_ABSORBER_ARBITRARY(1e-30),
                           speed_of_sound=SPEED_OF_SOUND,
                           alpha_coefficient=1e-4,
                           density=1000,
                           gruneisen_parameter=1.0,
                           name="background_water")

    background_dictionary = Settings()
    background_dictionary[Tags.MOLECULE_COMPOSITION] = (MolecularCompositionGenerator()
                                                        .append(heavy_water)
                                                        .get_molecular_composition(segmentation_type=-1))
    background_dictionary[Tags.STRUCTURE_TYPE] = Tags.BACKGROUND

    phantom_material_dictionary = Settings()
    phantom_material_dictionary[Tags.PRIORITY] = 3
    phantom_material_dictionary[Tags.STRUCTURE_START_MM] = [31, 0, 38]
    phantom_material_dictionary[Tags.STRUCTURE_X_EXTENT_MM] = 28
    phantom_material_dictionary[Tags.STRUCTURE_Y_EXTENT_MM] = 40
    phantom_material_dictionary[Tags.STRUCTURE_Z_EXTENT_MM] = 14
    phantom_material_dictionary[Tags.MOLECULE_COMPOSITION] = (MolecularCompositionGenerator()
                                                              .append(phantom_material)
                                                              .get_molecular_composition(segmentation_type=0))
    phantom_material_dictionary[Tags.CONSIDER_PARTIAL_VOLUME] = False
    phantom_material_dictionary[Tags.STRUCTURE_TYPE] = Tags.RECTANGULAR_CUBOID_STRUCTURE

    inclusion_1_dictionary = Settings()
    inclusion_1_dictionary[Tags.PRIORITY] = 8
    inclusion_1_dictionary[Tags.STRUCTURE_START_MM] = [38, 10, 40]
    inclusion_1_dictionary[Tags.STRUCTURE_X_EXTENT_MM] = 2
    inclusion_1_dictionary[Tags.STRUCTURE_Y_EXTENT_MM] = 20
    inclusion_1_dictionary[Tags.STRUCTURE_Z_EXTENT_MM] = 10
    inclusion_1_dictionary[Tags.MOLECULE_COMPOSITION] = (MolecularCompositionGenerator()
                                                              .append(inclusion_material)
                                                              .get_molecular_composition(segmentation_type=1))
    inclusion_1_dictionary[Tags.CONSIDER_PARTIAL_VOLUME] = False
    inclusion_1_dictionary[Tags.STRUCTURE_TYPE] = Tags.RECTANGULAR_CUBOID_STRUCTURE

    inclusion_2_dictionary = Settings()
    inclusion_2_dictionary[Tags.PRIORITY] = 5
    inclusion_2_dictionary[Tags.STRUCTURE_START_MM] = [50, 0, 43]
    inclusion_2_dictionary[Tags.STRUCTURE_END_MM] = [50, 40, 43]
    inclusion_2_dictionary[Tags.STRUCTURE_RADIUS_MM] = 2
    inclusion_2_dictionary[Tags.MOLECULE_COMPOSITION] = (MolecularCompositionGenerator()
                                                         .append(inclusion_material)
                                                         .get_molecular_composition(segmentation_type=2))
    inclusion_2_dictionary[Tags.CONSIDER_PARTIAL_VOLUME] = False
    inclusion_2_dictionary[Tags.STRUCTURE_TYPE] = Tags.CIRCULAR_TUBULAR_STRUCTURE

    tissue_dict = Settings()
    tissue_dict[Tags.BACKGROUND] = background_dictionary
    tissue_dict["phantom"] = phantom_material_dictionary
    tissue_dict["inclusion_1"] = inclusion_1_dictionary
    tissue_dict["inclusion_2"] = inclusion_2_dictionary
    return {
               Tags.STRUCTURES: tissue_dict,
               Tags.SIMULATE_DEFORMED_LAYERS: False
           }


def get_settings():
    general_settings = {
        # These parameters set the general properties of the simulated volume
        Tags.RANDOM_SEED: 4711,
        Tags.VOLUME_NAME: "InVision Simulation Example",
        Tags.SIMULATION_PATH: path_manager.get_hdf5_file_save_path(),
        Tags.SPACING_MM: SPACING,
        Tags.DIM_VOLUME_Z_MM: XZ_DIM,
        Tags.DIM_VOLUME_X_MM: XZ_DIM,
        Tags.DIM_VOLUME_Y_MM: Y_DIM,
        Tags.VOLUME_CREATOR: Tags.VOLUME_CREATOR_VERSATILE,
        Tags.GPU: True,
        Tags.WAVELENGTHS: [700]
    }

    volume_settings = create_volume()

    optical_settings = {
        Tags.OPTICAL_MODEL_NUMBER_PHOTONS: 1e7,
        Tags.OPTICAL_MODEL_BINARY_PATH: path_manager.get_mcx_binary_path(),
        Tags.ILLUMINATION_TYPE: Tags.ILLUMINATION_TYPE_MSOT_INVISION,
        Tags.LASER_PULSE_ENERGY_IN_MILLIJOULE: 50,
    }

    acoustic_settings = {
        Tags.ACOUSTIC_SIMULATION_3D: True,
        Tags.ACOUSTIC_MODEL_BINARY_PATH: path_manager.get_matlab_binary_path(),
        Tags.PROPERTY_ALPHA_POWER: 0.00,
        Tags.SENSOR_RECORD: "p",
        Tags.PMLInside: False,
        Tags.PMLSize: [31, 32],
        Tags.PMLAlpha: 1.5,
        Tags.PlotPML: False,
        Tags.RECORDMOVIE: False,
        Tags.MOVIENAME: "visualization_log",
        Tags.ACOUSTIC_LOG_SCALE: True
    }

    reconstruction_settings = {
        Tags.RECONSTRUCTION_PERFORM_BANDPASS_FILTERING: False,
        Tags.TUKEY_WINDOW_ALPHA: 0.5,
        Tags.RECONSTRUCTION_BMODE_AFTER_RECONSTRUCTION: False,
        Tags.RECONSTRUCTION_BMODE_METHOD: Tags.RECONSTRUCTION_BMODE_METHOD_HILBERT_TRANSFORM,
        Tags.RECONSTRUCTION_APODIZATION_METHOD: Tags.RECONSTRUCTION_APODIZATION_HAMMING,
        Tags.RECONSTRUCTION_MODE: Tags.RECONSTRUCTION_MODE_PRESSURE,
        Tags.PROPERTY_SPEED_OF_SOUND: SPEED_OF_SOUND,
        Tags.SENSOR_RECORD: "p",
        Tags.PMLInside: False,
        Tags.PMLSize: [31, 32],
        Tags.PMLAlpha: 1.5,
        Tags.PlotPML: False,
        Tags.RECORDMOVIE: False,
        Tags.MOVIENAME: "visualization_log",
        Tags.ACOUSTIC_LOG_SCALE: True,
        Tags.ACOUSTIC_MODEL_BINARY_PATH: path_manager.get_matlab_binary_path(),
        Tags.PROPERTY_ALPHA_POWER: 0.00,
        Tags.SPACING_MM: 0.25,
    }

    _settings = Settings(general_settings)
    _settings.set_volume_creation_settings(volume_settings)
    _settings.set_optical_settings(optical_settings)
    _settings.set_acoustic_settings(acoustic_settings)
    _settings.set_reconstruction_settings(reconstruction_settings)
    return _settings


device = get_device()
settings = get_settings()
pipeline = create_pipeline(settings)

simulate(simulation_pipeline=pipeline, digital_device_twin=device, settings=settings)

visualise_data(settings=settings,
               path_manager=path_manager,
               show_absorption=True,
               show_initial_pressure=True,
               show_reconstructed_data=True,
               show_xz_only=True)