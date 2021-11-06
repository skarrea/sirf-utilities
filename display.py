import sirf.STIR as pet
from scipy.spatial.transform import Rotation as R
import numpy as np

def printGeoInfo(image : pet.ImageData) -> None:
    """Print geometrical data for image object.

    Args:
        image (pet.ImageData): Input image.
    """
    print(image.get_geometrical_info().get_info())

def printAffineMatrixAsEulerAngles(affineMatrix : np.array, round = 4, seq = 'zxy', degrees = True) -> None:
    """prints an affine transformation matrix as euler angles. The affine matrix
    can be 4x4 or 3x3.

    Args:
        affineMatrix (np.array): 4x4 or 3x3 affine transformation matrix
        round (int, optional): Round to a certain number of decimals. Defaults to 4.
        seq (str, optional): Output axis sequence. Defaults to 'zxy'.
        degrees (bool, optional): Output degrees or radians. Defaults to True.

    """
    if affineMatrix.shape == (4,4):
        r = R.from_matrix(affineMatrix[:3, :3])
    elif affineMatrix.shape == (3,3):
        r = R.from_matrix(affineMatrix)

    print(r.as_euler(seq=seq, degrees=degrees).round(round))
