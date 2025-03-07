# SPDX-FileCopyrightText: 2021 Division of Intelligent Medical Systems, DKFZ
# SPDX-FileCopyrightText: 2021 Janek Groehl
# SPDX-License-Identifier: MIT

from abc import abstractmethod
from simpa.utils.settings import Settings
from simpa.utils import Tags
from simpa.utils.tissue_properties import TissueProperties
import numpy as np
import torch
from simpa.core import SimulationModule
from simpa.utils.dict_path_manager import generate_dict_path
from simpa.io_handling import save_data_field
from simpa.utils.quality_assurance.data_sanity_testing import assert_equal_shapes, assert_array_well_defined
from simpa.utils.processing_device import get_processing_device


class VolumeCreatorModuleBase(SimulationModule):
    """
    Use this class to define your own volume creation adapter.

    """

    def __init__(self, global_settings: Settings):
        super(VolumeCreatorModuleBase, self).__init__(global_settings=global_settings)
        self.component_settings = global_settings.get_volume_creation_settings()
        self.torch_device = get_processing_device(self.global_settings)

    def create_empty_volumes(self):
        volumes = dict()
        volume_x_dim, volume_y_dim, volume_z_dim = self.global_settings.get_volume_dimensions_voxels()
        sizes = (volume_x_dim, volume_y_dim, volume_z_dim)

        wavelength = self.global_settings[Tags.WAVELENGTH]
        first_wavelength = self.global_settings[Tags.WAVELENGTHS][0]

        for key in TissueProperties.property_tags:
            # Create wavelength-independent properties only in the first wavelength run
            if key in TissueProperties.wavelength_independent_properties and wavelength != first_wavelength:
                continue
            volumes[key] = torch.zeros(sizes, dtype=torch.float, device=self.torch_device)

        return volumes, volume_x_dim, volume_y_dim, volume_z_dim

    @abstractmethod
    def create_simulation_volume(self) -> dict:
        """
        This method creates an in silico representation of a tissue as described in the settings file that is given.

        :return: A dictionary containing optical and acoustic properties as well as other characteristics of the
            simulated volume such as oxygenation, and a segmentation mask. All of these are given as 3d numpy arrays.
        :rtype: dict
        """
        pass

    def run(self, device):
        self.logger.info("VOLUME CREATION")

        volumes = self.create_simulation_volume()
        # explicitly empty cache to free reserved GPU memory after volume creation
        torch.cuda.empty_cache()

        if not (Tags.IGNORE_QA_ASSERTIONS in self.global_settings and self.global_settings[Tags.IGNORE_QA_ASSERTIONS]):
            assert_equal_shapes(list(volumes.values()))
            for _volume_name in volumes.keys():
                if _volume_name == Tags.DATA_FIELD_OXYGENATION:
                    # oxygenation can have NaN by definition
                    continue
                assert_array_well_defined(volumes[_volume_name], array_name=_volume_name)

        for key, value in volumes.items():
            save_data_field(value, self.global_settings[Tags.SIMPA_OUTPUT_PATH],
                            data_field=key, wavelength=self.global_settings[Tags.WAVELENGTH])
