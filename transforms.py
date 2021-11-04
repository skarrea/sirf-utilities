import numpy as np
import sirf.STIR as pet
from typing import Callable

def scaleCT(imageArray:np.array) -> np.array:
    """Scales a numpy array with HU/10000 to 511 keV attenuation correction coefficients.
    Made to use on CT images converted directly with nm_mrac2mu.

    Parameters
    ----------
    imageArray : np.array
        np.array in units HU/10000

    Returns
    -------
    np.array
        imageArray containing linear attenuation coefficients at 511 KeV.

    References:
    Burger, C., Goerres, G., Schoenes, S. et al. PET attenuation
    coefficients from CT images: experimental evaluation of the
    transformation of CT into PET 511-keV attenuation coefficients. Eur
    J Nucl Med 29, 922–927 (2002).
    https://doi.org/10.1007/s00259-002-0796-3
    """

    imageArrayScaled = imageArray*1e4

    muH20PET = 0.096 * 1e4
    muBonePET = 0.172 * 1e4
    muH20CT = 0.184 * 1e4
    muBoneCT = 0.428 * 1e4

    resImArr = np.where(
        imageArrayScaled > 0,
        muH20PET
        + imageArrayScaled
        * (muH20CT / 1000)
        * ((muBonePET - muH20PET) / (muBoneCT - muH20CT)),
        muH20PET * (imageArrayScaled + 1000) / (1000),
    )
    return resImArr/1e4

def scaleImageData(inputImageData : pet.ImageData, scaler : Callable[[np.array], np.array]) -> pet.ImageData:
    """Scales imput sirf.STIR.ImageData using the a defined scaler function. 

    Parameters
    ----------
    inputImageData : pet.ImageData
        input pet.ImageData
    scaler : callable[[np.array], np.array]
        Any scaler function that takes np.array as input and output. Input and
        output must be of the same size.

    Returns
    -------
    pet.ImageData
        Scaled pet.ImageData
    """
    inputArray = inputImageData.as_array()
    outputArray = scaler(inputArray)
    outputImageData = inputImageData.copy()
    outputImageData.fill(outputArray)
    return outputImageData