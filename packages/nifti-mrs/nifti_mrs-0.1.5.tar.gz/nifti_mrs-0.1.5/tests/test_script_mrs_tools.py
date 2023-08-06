'''FSL-MRS test script

Test the tools script

Copyright Will Clarke, University of Oxford, 2021'''

# Imports
import subprocess
from pathlib import Path

import nibabel as nib
import pytest

# Files
testsPath = Path(__file__).parent

# Testing vis option
svs = testsPath / 'test_data' / 'metab.nii.gz'
svs_raw = testsPath / 'test_data' / 'metab_raw.nii.gz'


def test_vis_error(tmp_path):
    try:
        import fsl_mrs  # noqa: F401
    except ImportError:
        import mrs_tools
        with pytest.raises(
                ImportError,
                match="mrs_tools vis requires FSL-MRS tools to be installed. "
                      "See fsl-mrs.com for installation instructions."):
            mrs_tools.main(['vis', str(svs)])
    else:
        pytest.skip("fsl-mrs present, skipping test")


@pytest.mark.with_fsl_mrs
def test_vis_svs(tmp_path):
    pytest.importorskip("fsl_mrs")
    subprocess.check_call(['mrs_tools', 'vis',
                           '--ppmlim', '0.2', '4.2',
                           '--save', str(tmp_path / 'svs.png'),
                           svs])

    assert (tmp_path / 'svs.png').exists()

    subprocess.check_call(['mrs_tools', 'vis',
                           '--ppmlim', '0.2', '4.2',
                           '--save', str(tmp_path / 'svs2.png'),
                           svs.with_suffix('').with_suffix('')])

    assert (tmp_path / 'svs2.png').exists()

    subprocess.check_call(['mrs_tools', 'vis',
                           '--ppmlim', '0.2', '4.2',
                           '--display_dim', 'DIM_DYN',
                           '--save', str(tmp_path / 'svs3.png'),
                           svs_raw])

    assert (tmp_path / 'svs3.png').exists()

    subprocess.check_call(['mrs_tools', 'vis',
                           '--ppmlim', '0.2', '4.2',
                           '--display_dim', 'DIM_COIL',
                           '--no_mean',
                           '--save', str(tmp_path / 'svs4.png'),
                           svs_raw])

    assert (tmp_path / 'svs4.png').exists()


# def test_vis_basis(tmp_path):
#     subprocess.check_call(['mrs_tools', 'vis',
#                            '--ppmlim', '0.2', '4.2',
#                            '--save', str(tmp_path / 'basis.png'),
#                            basis])

#     assert (tmp_path / 'basis.png').exists()


# Testing info option
processed = testsPath / 'test_data' / 'metab.nii.gz'
unprocessed = testsPath / 'test_data' / 'metab_raw.nii.gz'


def test_single_info(tmp_path):
    subprocess.check_call(['mrs_tools', 'info', str(processed)])


def test_multi_info(tmp_path):
    subprocess.check_call(['mrs_tools', 'info', str(processed), str(unprocessed)])


# Testing merge option
test_data_merge_1 = testsPath / 'test_data' / 'wref_raw.nii.gz'
test_data_merge_2 = testsPath / 'test_data'  / 'quant_raw.nii.gz'


def test_merge(tmp_path):
    """The tests here only check that the expected files are created.
    I rely on the much more detailed tests in test_utils_nifti_mrs_tools_split_merge.py
    to check that the merge is carried out correctly.
    """
    subprocess.check_call(['mrs_tools', 'merge',
                           '--dim', 'DIM_DYN',
                           '--output', str(tmp_path),
                           '--filename', 'test_2_merge',
                           '--files', str(test_data_merge_1), str(test_data_merge_2)])

    assert (tmp_path / 'test_2_merge.nii.gz').exists()

    subprocess.check_call(['mrs_tools', 'merge',
                           '--dim', 'DIM_DYN',
                           '--output', str(tmp_path),
                           '--filename', 'test_3_merge',
                           '--files', str(test_data_merge_1), str(test_data_merge_2), str(test_data_merge_2)])

    assert (tmp_path / 'test_3_merge.nii.gz').exists()

    subprocess.check_call(['mrs_tools', 'merge',
                           '--dim', 'DIM_DYN',
                           '--output', str(tmp_path),
                           '--files', str(test_data_merge_1), str(test_data_merge_2)])

    assert (tmp_path / 'wref_raw_quant_raw_merged.nii.gz').exists()


# Test split option
test_data_split = testsPath / 'test_data' / 'metab_raw.nii.gz'


def test_split(tmp_path):
    """The tests here only check that the expected files are created.
    I rely on the much more detailed tests in test_utils_nifti_mrs_tools_split_merge.py
    to check that the merge is carried out correctly.
    """
    subprocess.check_call(['mrs_tools', 'split',
                           '--dim', 'DIM_DYN',
                           '--index', '7',
                           '--output', str(tmp_path),
                           '--filename', 'split_file',
                           '--file', str(test_data_split)])

    assert (tmp_path / 'split_file_low.nii.gz').exists()
    assert (tmp_path / 'split_file_high.nii.gz').exists()
    f1 = nib.load(tmp_path / 'split_file_low.nii.gz')
    f2 = nib.load(tmp_path / 'split_file_high.nii.gz')
    assert f1.shape[5] == 8
    assert f2.shape[5] == 8

    subprocess.check_call(['mrs_tools', 'split',
                           '--dim', 'DIM_DYN',
                           '--index', '7',
                           '--output', str(tmp_path),
                           '--file', str(test_data_split)])

    assert (tmp_path / 'metab_raw_low.nii.gz').exists()
    assert (tmp_path / 'metab_raw_high.nii.gz').exists()
    f1 = nib.load(tmp_path / 'metab_raw_low.nii.gz')
    f2 = nib.load(tmp_path / 'metab_raw_high.nii.gz')
    assert f1.shape[5] == 8
    assert f2.shape[5] == 8

    subprocess.check_call(['mrs_tools', 'split',
                           '--dim', 'DIM_DYN',
                           '--indices', '1', '4', '15',
                           '--filename', 'indicies_select',
                           '--output', str(tmp_path),
                           '--file', str(test_data_split)])

    assert (tmp_path / 'indicies_select_others.nii.gz').exists()
    assert (tmp_path / 'indicies_select_selected.nii.gz').exists()
    f1 = nib.load(tmp_path / 'indicies_select_others.nii.gz')
    f2 = nib.load(tmp_path / 'indicies_select_selected.nii.gz')
    assert f1.shape[5] == 13
    assert f2.shape[5] == 3


# Test reorder option
def test_reorder(tmp_path):
    subprocess.check_call(['mrs_tools', 'reorder',
                           '--dim_order', 'DIM_DYN', 'DIM_COIL',
                           '--output', str(tmp_path),
                           '--filename', 'reordered_file',
                           '--file', str(test_data_split)])

    assert (tmp_path / 'reordered_file.nii.gz').exists()

    subprocess.check_call(['mrs_tools', 'reorder',
                           '--dim_order', 'DIM_COIL', 'DIM_DYN', 'DIM_EDIT',
                           '--output', str(tmp_path),
                           '--file', str(test_data_split)])

    assert (tmp_path / 'metab_raw_reordered.nii.gz').exists()

    subprocess.check_call(['mrs_tools', 'reorder',
                           '--dim_order', 'DIM_EDIT', 'DIM_COIL', 'DIM_DYN',
                           '--output', str(tmp_path),
                           '--filename', 'reordered_file',
                           '--file', str(test_data_split)])

    assert (tmp_path / 'reordered_file.nii.gz').exists()


# Test conjugate option
def test_conjugate(tmp_path):
    subprocess.check_call(['mrs_tools', 'conjugate',
                           '--output', str(tmp_path),
                           '--filename', 'conj_file',
                           '--file', str(svs)])

    assert (tmp_path / 'conj_file.nii.gz').exists()

    subprocess.check_call(['mrs_tools', 'conjugate',
                           '--output', str(tmp_path),
                           '--file', str(svs)])

    assert (tmp_path / 'metab.nii.gz').exists()
