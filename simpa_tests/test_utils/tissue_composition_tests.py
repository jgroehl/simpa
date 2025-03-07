# SPDX-FileCopyrightText: 2021 Division of Intelligent Medical Systems, DKFZ
# SPDX-FileCopyrightText: 2021 Janek Groehl
# SPDX-License-Identifier: MIT

from simpa.utils import Tags, Settings, SegmentationClasses, calculate_gruneisen_parameter_from_temperature
from simpa.utils.libraries.molecule_library import MolecularComposition
from simpa.utils.tissue_properties import TissueProperties
from simpa.utils.libraries.tissue_library import TissueLibrary
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

TEST_SETTINGS = Settings({
    # These parameters set the general properties of the simulated volume
    Tags.SPACING_MM: 1,
    Tags.DIM_VOLUME_Z_MM: 1,
    Tags.DIM_VOLUME_X_MM: 1,
    Tags.DIM_VOLUME_Y_MM: 1
})

def validate_expected_values_dictionary(expected_values: dict):

    if len(expected_values.keys()) < 1:
        raise ValueError("The expected_values dictionary must have at least one entry.")

    for key in expected_values.keys():
        if not isinstance(key, (float, int)):
            raise KeyError("The keys of the expected_values dictionary must be numbers.")

        if not isinstance(expected_values[key], TissueProperties):
            raise ValueError("The expected_values dictionary values must be TissueProperty instances.")


def compare_molecular_composition_against_expected_values(molecular_composition: MolecularComposition,
                                                          expected_values: dict,
                                                          tolerated_margin_in_percent: float = 0.1,
                                                          visualise_values: bool = False,
                                                          title="Tissue Composition Comparison"):
    """

    """

    validate_expected_values_dictionary(expected_values)
    if visualise_values:
        plt.figure(figsize=(12, 8))
        plt.suptitle(title + f" [green=expected, blue=actual, red={tolerated_margin_in_percent*100}% margin]")
        num_subplots = len(TissueProperties.property_tags)

    for wavelength in expected_values.keys():
        molecular_composition.update_internal_properties(TEST_SETTINGS)
        composition_properties = molecular_composition.get_properties_for_wavelength(TEST_SETTINGS, wavelength=wavelength)
        expected_properties = expected_values[wavelength]

        if visualise_values:
            for tag_idx, tag in enumerate(TissueProperties.property_tags):
                ax = plt.subplot(3, int(np.ceil(num_subplots/3)), (tag_idx+1))
                ax.set_title(tag)
                ax.set_xlabel("wavelength [nm]")
                ax.set_ylabel("value [units]")
                if expected_properties[tag] is not None:
                    ax.add_patch(patches.Rectangle((wavelength-10, expected_properties[tag] * (1-tolerated_margin_in_percent)),
                                                   20, expected_properties[tag] * 2 * tolerated_margin_in_percent,
                                                   color="red", alpha=0.2))
                ax.scatter(x=wavelength, y=composition_properties[tag], c="blue")
                ax.scatter(x=wavelength, y=expected_properties[tag], c="green")
        else:
            for tag in TissueProperties.property_tags:
                if expected_properties[tag] is not None:
                    if (not (composition_properties[tag] is None and expected_properties[tag] is None)) and \
                        ((np.abs(composition_properties[tag] - expected_properties[tag]) /
                          expected_properties[tag]) > tolerated_margin_in_percent):
                        raise AssertionError(f"The calculated value for {tag} at "
                                             f"wavelength {wavelength}nm was different from the"
                                             f" expected value by a margin greater than {tolerated_margin_in_percent*100}%"
                                             f" (was {composition_properties[tag]} but was "
                                             f"expected to be {expected_properties[tag]})")

    if visualise_values:
        plt.tight_layout()
        plt.show()
        plt.close()


def get_epidermis_reference_dictionary():
    """
    The
        @article{bashkatov2011optical,
              title={Optical properties of skin, subcutaneous, and muscle tissues: a review},
              author={Bashkatov, Alexey N and Genina, Elina A and Tuchin, Valery V},
              journal={Journal of Innovative Optical Health Sciences},
              volume={4},
              number={01},
              pages={9--38},
              year={2011},
              publisher={World Scientific}
            }

    """
    reference_dict = dict()

    values450nm = TissueProperties(TEST_SETTINGS)
    values450nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 13.5
    values450nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 121.6
    values450nm[Tags.DATA_FIELD_ANISOTROPY] = 0.728
    values450nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values450nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values450nm[Tags.DATA_FIELD_OXYGENATION] = None
    values450nm[Tags.DATA_FIELD_DENSITY] = 1109
    values450nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values450nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values500nm = TissueProperties(TEST_SETTINGS)
    values500nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 9.77
    values500nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 93.01
    values500nm[Tags.DATA_FIELD_ANISOTROPY] = 0.745
    values500nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values500nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values500nm[Tags.DATA_FIELD_OXYGENATION] = None
    values500nm[Tags.DATA_FIELD_DENSITY] = 1109
    values500nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values500nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values550nm = TissueProperties(TEST_SETTINGS)
    values550nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 6.85
    values550nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 74.7
    values550nm[Tags.DATA_FIELD_ANISOTROPY] = 0.759
    values550nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values550nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values550nm[Tags.DATA_FIELD_OXYGENATION] = None
    values550nm[Tags.DATA_FIELD_DENSITY] = 1109
    values550nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values550nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values600nm = TissueProperties(TEST_SETTINGS)
    values600nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 5.22
    values600nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 63.76
    values600nm[Tags.DATA_FIELD_ANISOTROPY] = 0.774
    values600nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values600nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values600nm[Tags.DATA_FIELD_OXYGENATION] = None
    values600nm[Tags.DATA_FIELD_DENSITY] = 1109
    values600nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values600nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 3.68
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 55.48
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = 0.7887
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values650nm[Tags.DATA_FIELD_OXYGENATION] = None
    values650nm[Tags.DATA_FIELD_DENSITY] = 1109
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 3.07
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 54.66
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = 0.804
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.EPIDERMIS
    values700nm[Tags.DATA_FIELD_OXYGENATION] = None
    values700nm[Tags.DATA_FIELD_DENSITY] = 1109
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624.0
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    reference_dict[450] = values450nm
    reference_dict[500] = values500nm
    reference_dict[550] = values550nm
    reference_dict[600] = values600nm
    reference_dict[650] = values650nm
    reference_dict[700] = values700nm

    return reference_dict


def get_dermis_reference_dictionary():
    """
    The values were compiled from the following ressources:

        https://omlc.org/news/jan98/skinoptics.html

        @article{bashkatov2011optical,
                  title={Optical properties of skin, subcutaneous, and muscle tissues: a review},
                  author={Bashkatov, Alexey N and Genina, Elina A and Tuchin, Valery V},
                  journal={Journal of Innovative Optical Health Sciences},
                  volume={4},
                  number={01},
                  pages={9--38},
                  year={2011},
                  publisher={World Scientific}
                }


    """
    reference_dict = dict()

    values450nm = TissueProperties(TEST_SETTINGS)
    values450nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 2.105749981
    values450nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 244.6
    values450nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values450nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values450nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values450nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values450nm[Tags.DATA_FIELD_DENSITY] = 1109
    values450nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values450nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values500nm = TissueProperties(TEST_SETTINGS)
    values500nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.924812913
    values500nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 175.0
    values500nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values500nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values500nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values500nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values500nm[Tags.DATA_FIELD_DENSITY] = 1109
    values500nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values500nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values550nm = TissueProperties(TEST_SETTINGS)
    values550nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.974386604
    values550nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 131.1
    values550nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values550nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values550nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values550nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values550nm[Tags.DATA_FIELD_DENSITY] = 1109
    values550nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values550nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values600nm = TissueProperties(TEST_SETTINGS)
    values600nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.440476363
    values600nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 101.9
    values600nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values600nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values600nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values600nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values600nm[Tags.DATA_FIELD_DENSITY] = 1109
    values600nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values600nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.313052704
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 81.7
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values650nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values650nm[Tags.DATA_FIELD_DENSITY] = 1109
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.277003236
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 67.1
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values700nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values700nm[Tags.DATA_FIELD_DENSITY] = 1109
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values750nm = TissueProperties(TEST_SETTINGS)
    values750nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.264286111
    values750nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 56.3
    values750nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values750nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values750nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values750nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values750nm[Tags.DATA_FIELD_DENSITY] = 1109
    values750nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values750nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values800nm = TissueProperties(TEST_SETTINGS)
    values800nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.256933531
    values800nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 48.1
    values800nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values800nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values800nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values800nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values800nm[Tags.DATA_FIELD_DENSITY] = 1109
    values800nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values800nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values850nm = TissueProperties(TEST_SETTINGS)
    values850nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.255224508
    values850nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 41.8
    values850nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values850nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values850nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values850nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values850nm[Tags.DATA_FIELD_DENSITY] = 1109
    values850nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values850nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values900nm = TissueProperties(TEST_SETTINGS)
    values900nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.254198591
    values900nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 36.7
    values900nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values900nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values900nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values900nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values900nm[Tags.DATA_FIELD_DENSITY] = 1109
    values900nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values900nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    values950nm = TissueProperties(TEST_SETTINGS)
    values950nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.254522563
    values950nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 32.6
    values950nm[Tags.DATA_FIELD_ANISOTROPY] = 0.715
    values950nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values950nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.DERMIS
    values950nm[Tags.DATA_FIELD_OXYGENATION] = 0.5
    values950nm[Tags.DATA_FIELD_DENSITY] = 1109
    values950nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1624
    values950nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.35

    reference_dict[450] = values450nm
    reference_dict[500] = values500nm
    reference_dict[550] = values550nm
    reference_dict[600] = values600nm
    reference_dict[650] = values650nm
    reference_dict[700] = values700nm
    reference_dict[750] = values750nm
    reference_dict[800] = values800nm
    reference_dict[850] = values850nm
    reference_dict[900] = values900nm
    reference_dict[950] = values950nm

    return reference_dict


def get_muscle_reference_dictionary():
    """
    The
        @article{bashkatov2011optical,
              title={Optical properties of skin, subcutaneous, and muscle tissues: a review},
              author={Bashkatov, Alexey N and Genina, Elina A and Tuchin, Valery V},
              journal={Journal of Innovative Optical Health Sciences},
              volume={4},
              number={01},
              pages={9--38},
              year={2011},
              publisher={World Scientific}
            }

    """
    reference_dict = dict()

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 1.04
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 87.5
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values650nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values650nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.48
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 81.8
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values700nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values700nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values750nm = TissueProperties(TEST_SETTINGS)
    values750nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.41
    values750nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 77.1
    values750nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values750nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values750nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values750nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values750nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values750nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values750nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values800nm = TissueProperties(TEST_SETTINGS)
    values800nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.28
    values800nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 70.4
    values800nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values800nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values800nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values800nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values800nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values800nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values800nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values850nm = TissueProperties(TEST_SETTINGS)
    values850nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.3
    values850nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 66.7
    values850nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values850nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values850nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values850nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values850nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values850nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values850nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values900nm = TissueProperties(TEST_SETTINGS)
    values900nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.32
    values900nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 62.1
    values900nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values900nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values900nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values900nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values900nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values900nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values900nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    values950nm = TissueProperties(TEST_SETTINGS)
    values950nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 0.46
    values950nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 59.0
    values950nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9
    values950nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values950nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.MUSCLE
    values950nm[Tags.DATA_FIELD_OXYGENATION] = 0.175
    values950nm[Tags.DATA_FIELD_DENSITY] = 1090.4
    values950nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1588.4
    values950nm[Tags.DATA_FIELD_ALPHA_COEFF] = 1.09

    reference_dict[650] = values650nm
    reference_dict[700] = values700nm
    reference_dict[750] = values750nm
    reference_dict[800] = values800nm
    reference_dict[850] = values850nm
    reference_dict[900] = values900nm
    reference_dict[950] = values950nm

    return reference_dict


def get_fully_oxygenated_blood_reference_dictionary(only_use_NIR_values=False):
    """
    The values were compiled from the following resources:

        https://omlc.org/news/jan98/skinoptics.html

        @article{bashkatov2011optical,
                  title={Optical properties of skin, subcutaneous, and muscle tissues: a review},
                  author={Bashkatov, Alexey N and Genina, Elina A and Tuchin, Valery V},
                  journal={Journal of Innovative Optical Health Sciences},
                  volume={4},
                  number={01},
                  pages={9--38},
                  year={2011},
                  publisher={World Scientific}
                }


    """
    reference_dict = dict()

    values450nm = TissueProperties(TEST_SETTINGS)
    values450nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 336
    values450nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 772
    values450nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9447
    values450nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values450nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values450nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values450nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values450nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values450nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values500nm = TissueProperties(TEST_SETTINGS)
    values500nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 112
    values500nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 868.3
    values500nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9761
    values500nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values500nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values500nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values500nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values500nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values500nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values550nm = TissueProperties(TEST_SETTINGS)
    values550nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 230
    values550nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 714.9
    values550nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9642
    values550nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values550nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values550nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values550nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values550nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values550nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values600nm = TissueProperties(TEST_SETTINGS)
    values600nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 17
    values600nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 868.8
    values600nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9794
    values600nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values600nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values600nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values600nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values600nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values600nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 2
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 880.1
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9825
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values650nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values650nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 1.6
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 857.0
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9836
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values700nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values700nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values750nm = TissueProperties(TEST_SETTINGS)
    values750nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 2.8
    values750nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 802.2
    values750nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9837
    values750nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values750nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values750nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values750nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values750nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values750nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values800nm = TissueProperties(TEST_SETTINGS)
    values800nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 4.4
    values800nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 767.3
    values800nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9833
    values800nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values800nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values800nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values800nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values800nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values800nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values850nm = TissueProperties(TEST_SETTINGS)
    values850nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 5.7
    values850nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 742.0
    values850nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9832
    values850nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values850nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values850nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values850nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values850nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values850nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values900nm = TissueProperties(TEST_SETTINGS)
    values900nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 6.4
    values900nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 688.6
    values900nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9824
    values900nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values900nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values900nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values900nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values900nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values900nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values950nm = TissueProperties(TEST_SETTINGS)
    values950nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 6.4
    values950nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 652.1
    values950nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9808
    values950nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values950nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values950nm[Tags.DATA_FIELD_OXYGENATION] = 1.0
    values950nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values950nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values950nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    if not only_use_NIR_values:
        reference_dict[450] = values450nm
        reference_dict[500] = values500nm
        reference_dict[550] = values550nm
        reference_dict[600] = values600nm
    reference_dict[650] = values650nm
    reference_dict[700] = values700nm
    reference_dict[750] = values750nm
    reference_dict[800] = values800nm
    reference_dict[850] = values850nm
    reference_dict[900] = values900nm
    reference_dict[950] = values950nm

    return reference_dict


def get_fully_deoxygenated_blood_reference_dictionary(only_use_NIR_values=False):
    """
    The values were compiled from the following resources:

        https://omlc.org/news/jan98/skinoptics.html

        @article{bashkatov2011optical,
                  title={Optical properties of skin, subcutaneous, and muscle tissues: a review},
                  author={Bashkatov, Alexey N and Genina, Elina A and Tuchin, Valery V},
                  journal={Journal of Innovative Optical Health Sciences},
                  volume={4},
                  number={01},
                  pages={9--38},
                  year={2011},
                  publisher={World Scientific}
                }


    """
    reference_dict = dict()

    values450nm = TissueProperties(TEST_SETTINGS)
    values450nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 553
    values450nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 772
    values450nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9447
    values450nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values450nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values450nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values450nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values450nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values450nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values500nm = TissueProperties(TEST_SETTINGS)
    values500nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 112
    values500nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 868.3
    values500nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9761
    values500nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values500nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values500nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values500nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values500nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values500nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values550nm = TissueProperties(TEST_SETTINGS)
    values550nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 286
    values550nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 714.9
    values550nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9642
    values550nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values550nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values550nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values550nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values550nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values550nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values600nm = TissueProperties(TEST_SETTINGS)
    values600nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 79
    values600nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 868.8
    values600nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9794
    values600nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values600nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values600nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values600nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values600nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values600nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 20.1
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 880.1
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9825
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values650nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values650nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 9.6
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 857.0
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9836
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values700nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values700nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values750nm = TissueProperties(TEST_SETTINGS)
    values750nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 7.5
    values750nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 802.2
    values750nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9837
    values750nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values750nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values750nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values750nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values750nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values750nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values800nm = TissueProperties(TEST_SETTINGS)
    values800nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 4.1
    values800nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 767.3
    values800nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9833
    values800nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values800nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values800nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values800nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values800nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values800nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values850nm = TissueProperties(TEST_SETTINGS)
    values850nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 3.7
    values850nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 742.0
    values850nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9832
    values850nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values850nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values850nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values850nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values850nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values850nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values900nm = TissueProperties(TEST_SETTINGS)
    values900nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 4.1
    values900nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 688.6
    values900nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9824
    values900nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values900nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values900nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values900nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values900nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values900nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    values950nm = TissueProperties(TEST_SETTINGS)
    values950nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = 3.2
    values950nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = 652.1
    values950nm[Tags.DATA_FIELD_ANISOTROPY] = 0.9808
    values950nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values950nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.BLOOD
    values950nm[Tags.DATA_FIELD_OXYGENATION] = 0.0
    values950nm[Tags.DATA_FIELD_DENSITY] = 1049.75
    values950nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1578.2
    values950nm[Tags.DATA_FIELD_ALPHA_COEFF] = 0.2

    if not only_use_NIR_values:
        reference_dict[450] = values450nm
        reference_dict[500] = values500nm
        reference_dict[550] = values550nm
        reference_dict[600] = values600nm
    reference_dict[650] = values650nm
    reference_dict[700] = values700nm
    reference_dict[750] = values750nm
    reference_dict[800] = values800nm
    reference_dict[850] = values850nm
    reference_dict[900] = values900nm
    reference_dict[950] = values950nm

    return reference_dict


def get_lymph_node_reference_dictionary(only_use_NIR_values=False):
    """
    The values were compiled from the following resources:

    """
    reference_dict = dict()

    values450nm = TissueProperties(TEST_SETTINGS)
    values450nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values450nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values450nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values450nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values450nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values450nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values450nm[Tags.DATA_FIELD_DENSITY] = 1035
    values450nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values450nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values500nm = TissueProperties(TEST_SETTINGS)
    values500nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values500nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values500nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values500nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values500nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values500nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values500nm[Tags.DATA_FIELD_DENSITY] = 1035
    values500nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values500nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values550nm = TissueProperties(TEST_SETTINGS)
    values550nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values550nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values550nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values550nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values550nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values550nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values550nm[Tags.DATA_FIELD_DENSITY] = 1035
    values550nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values550nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values600nm = TissueProperties(TEST_SETTINGS)
    values600nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values600nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values600nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values600nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values600nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values600nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values600nm[Tags.DATA_FIELD_DENSITY] = 1035
    values600nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values600nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values650nm = TissueProperties(TEST_SETTINGS)
    values650nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values650nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values650nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values650nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values650nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values650nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values650nm[Tags.DATA_FIELD_DENSITY] = 1035
    values650nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values650nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values700nm = TissueProperties(TEST_SETTINGS)
    values700nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values700nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values700nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values700nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values700nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values700nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values700nm[Tags.DATA_FIELD_DENSITY] = 1035
    values700nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values700nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values750nm = TissueProperties(TEST_SETTINGS)
    values750nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values750nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values750nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values750nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values750nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values750nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values750nm[Tags.DATA_FIELD_DENSITY] = 1035
    values750nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values750nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values800nm = TissueProperties(TEST_SETTINGS)
    values800nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values800nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values800nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values800nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values800nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values800nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values800nm[Tags.DATA_FIELD_DENSITY] = 1035
    values800nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values800nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values850nm = TissueProperties(TEST_SETTINGS)
    values850nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values850nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values850nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values850nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values850nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values850nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values850nm[Tags.DATA_FIELD_DENSITY] = 1035
    values850nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values850nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values900nm = TissueProperties(TEST_SETTINGS)
    values900nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values900nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values900nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values900nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values900nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values900nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values900nm[Tags.DATA_FIELD_DENSITY] = 1035
    values900nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values900nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    values950nm = TissueProperties(TEST_SETTINGS)
    values950nm[Tags.DATA_FIELD_ABSORPTION_PER_CM] = None
    values950nm[Tags.DATA_FIELD_SCATTERING_PER_CM] = None
    values950nm[Tags.DATA_FIELD_ANISOTROPY] = None
    values950nm[Tags.DATA_FIELD_GRUNEISEN_PARAMETER] = calculate_gruneisen_parameter_from_temperature(37.0)
    values950nm[Tags.DATA_FIELD_SEGMENTATION] = SegmentationClasses.LYMPH_NODE
    values950nm[Tags.DATA_FIELD_OXYGENATION] = 0.73
    values950nm[Tags.DATA_FIELD_DENSITY] = 1035
    values950nm[Tags.DATA_FIELD_SPEED_OF_SOUND] = 1586
    values950nm[Tags.DATA_FIELD_ALPHA_COEFF] = 2.50

    if not only_use_NIR_values:
        reference_dict[450] = values450nm
        reference_dict[500] = values500nm
        reference_dict[550] = values550nm
        reference_dict[600] = values600nm
    reference_dict[650] = values650nm
    reference_dict[700] = values700nm
    reference_dict[750] = values750nm
    reference_dict[800] = values800nm
    reference_dict[850] = values850nm
    reference_dict[900] = values900nm
    reference_dict[950] = values950nm

    return reference_dict


if __name__ == "__main__":

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().epidermis(),
                                                          expected_values=get_epidermis_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="Epidermis ")

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().blood(1.0),
                                                          expected_values=get_fully_oxygenated_blood_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="100% sO2 Blood ")

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().blood(0.0),
                                                          expected_values=get_fully_deoxygenated_blood_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="0% sO2 Blood ")

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().dermis(),
                                                          expected_values=get_dermis_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="Dermis ")

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().muscle(),
                                                          expected_values=get_muscle_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="Muscle ")

    compare_molecular_composition_against_expected_values(molecular_composition=TissueLibrary().lymph_node(),
                                                          expected_values=get_lymph_node_reference_dictionary(),
                                                          visualise_values=True,
                                                          title="LymphNode ")
