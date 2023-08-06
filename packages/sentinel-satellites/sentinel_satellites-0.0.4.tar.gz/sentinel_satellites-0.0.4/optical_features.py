import ee, pandas as pd


def calculate_ndvi(image, date, polygon):
    """
    Calculates the NDVI index for a given image, date, and polygon.
    
    NDVI (Normalized Difference Vegetation Index), is a remote sensing index used to assess vegetation
    health and density. It is based on the principle that healthy vegetation strongly absorbs visible light 
    (primarily in the blue and red wavelengths) and reflects near-infrared light. 
    The NDVI is calculated as the normalized difference between near-infrared (NIR) and red light, as shown in the 
    formula below:
        NDVI = (NIR - red) / (NIR + red)

    The resulting values range from -1 to 1, with higher values indicating more vegetation and healthier vegetation.
    NDVI is commonly used in applications such as agriculture, forestry, and ecology to monitor vegetation growth and
    health over time.

    Args:
        image (ee.ImageCollection): The Sentinel 2 image collection filtered by date and bounds.
        date (pd.Timestamp): The acquisition date in Pandas Timestamp format.
        polygon (ee.Geometry): The field polygon geometry in Earth Engine format.
        
    Returns:
        float: the calculated NDVI value, for the specified date and polygon.
    """
    # Filter image collection to get the image for the date
    image = ee.Image(image.filterDate(date.strftime('%Y-%m-%d'), (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')).first())

    # Calculate NDVI
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')

    # Mask out clouds and shadows
    ndvi = ndvi.updateMask(image.select('QA60').bitwiseAnd(2).neq(2))

    # Calculate the mean NDVI for the field polygon
    return ndvi.reduceRegion(reducer=ee.Reducer.mean(), geometry=polygon).getInfo()['NDVI']


def calculate_eomi(image, date, polygon, id):
    """
    Calculates the EOMIx (Exogenous Organic Matter Index) index for a given image, date, and polygon.

    The Exogenous Organic Matter Index (EOMI) is a soil quality indicator used to assess the content and quality of
    organic matter in soil. The EOMI is sensitive to the quantity and quality of exogenous organic matter, such as 
    crop residues, manure, and other organic inputs, as well as the presence of mineral and inorganic components in soil.
    For further details read the following paper: https://www.mdpi.com/2072-4292/13/9/1616.

    Args:
        image (ee.ImageCollection): The Sentinel 2 image collection filtered by date and bounds.
        date (pd.Timestamp): The acquisition date in Pandas Timestamp format.
        polygon (ee.Geometry): The field polygon geometry in Earth Engine format.
        id (int): The id of the EOMI to be calculated (from 1 to 4).
        
    Returns:
        float: the calculated EOMIx value, for the specified date and polygon.
    """
    # Filter image collection to get the image for the date
    image = ee.Image(image.filterDate(date.strftime('%Y-%m-%d'), (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')).first())

    # Calculate EOMI (different with respect to the passed id)
    if (id == 1):
        eomi = image.normalizedDifference(['B11', 'B8A']).rename('EOMI1')
    if (id == 2):
        eomi = image.normalizedDifference(['B12', 'B4']).rename('EOMI2')
    if (id == 3):
        b11 = image.select('B11')
        b8a = image.select('B8A')
        b12 = image.select('B12')
        b04 = image.select('B4')
        eomi = ((b11.subtract(b8a)).add(b12.add(b04))).divide(b11.add(b8a).add(b12).add(b04)).rename('EOMI3')
    if (id == 4):
        eomi = image.normalizedDifference(['B11', 'B4']).rename('EOMI4')

    # Mask out clouds and shadows
    eomi = eomi.updateMask(image.select('QA60').bitwiseAnd(2).neq(2))

    # Calculate the mean EOMI for the field polygon
    return eomi.reduceRegion(reducer=ee.Reducer.mean(), geometry=polygon).getInfo()['EOMI' + str(id)]


def calculate_savi(image, date, polygon, type=""):
    """
    Calculate the xSAVI index for a specific date and polygon in a Sentinel-2 image collection
    
    This function calculates a specified vegetation index, such as SAVI, MSAVI, OSAVI, or TSAVI, for a specific date and 
    polygon in a Sentinel-2 image collection.
    - SAVI (Soil Adjusted Vegetation Index) was developed to minimize the influence of soil brightness on vegetation indices. 
      SAVI uses a soil adjustment factor to reduce the noise caused by soil brightness. It is particularly useful in areas 
      with sparse vegetation.
    - OSAVI (Optimized Soil Adjusted Vegetation Index) is similar to SAVI, but it has been optimized to better handle areas
      with dense vegetation. OSAVI was developed to reduce the saturation effect seen in SAVI at high vegetation densities.
    - MSAVI (Modified Soil Adjusted Vegetation Index) is a modification of SAVI that is designed to reduce the noise and saturation
      issues in areas with dense vegetation. MSAVI is often used in agricultural applications.
    - TSAVI (Transformed Soil Adjusted Vegetation Index) is a variation of SAVI that uses a different soil adjustment factor to
      reduce the influence of soil brightness on vegetation indices. TSAVI is particularly useful in arid and semi-arid regions.
    
    Args:
        image (ee.ImageCollection): The Sentinel 2 image collection filtered by date and bounds.
        date (pd.Timestamp): The acquisition date in Pandas Timestamp format.
        polygon (ee.Geometry): The field polygon geometry in Earth Engine format.
        type (str): The type of vegetation index to calculate (default is 'SAVI'). Other options include 'M', 
                    'O', and 'T'.
    
    Returns:
        float: the mean value of the specified xSAVI, for the specified date and polygon.
    """
    # Filter image collection to get the image for the date
    image = ee.Image(image.filterDate(date.strftime('%Y-%m-%d'), (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')).first())

    # Select useful bands
    nir = image.select('B8')
    red = image.select('B4')

    # Calculate the specified vegetation index
    if type == '':
        L = 0.428
        savi = (nir.subtract(red)).divide(nir.add(red).add(L)).multiply(1 + L).rename('SAVI')
    elif type == 'M':
        savi = nir.multiply(2.0).add(1.0).subtract(nir.multiply(2.0).add(1.0).pow(2).subtract(nir.subtract(red).multiply(8.0)).sqrt()).divide(2.0).rename('MSAVI')
    elif type == 'O':
        savi = nir.subtract(red).multiply(1.0 + 0.16).divide(nir.add(red).add(0.16)).rename('OSAVI')
    elif type == 'T':
        X, A, B = 0.114, 0.824, 0.421
        savi = nir.subtract(B.multiply(red).subtract(A)).multiply(B).divide(red.add(B.multiply(nir.subtract(A))).add(X.multiply(1.0 + B.pow(2.0)))).rename('TSAVI')

    # Mask out clouds and shadows
    savi = savi.updateMask(image.select('QA60').bitwiseAnd(2).neq(2))

    # Calculate the mean vegetation index for the field polygon
    return savi.reduceRegion(reducer=ee.Reducer.mean(), geometry=polygon).getInfo()[type + 'SAVI']


def calculate_nbr2(image, date, polygon):
    """
    Calculate the NBR2 value for a specific date and polygon in a Sentinel-2 image collection
    
    The Normalized Burn Ratio 2 (NBR2) is a remote sensing index used to detect and quantify the severity of burn scars
    caused by wildfires. It is an enhancement of the original Normalized Burn Ratio (NBR) index, which was developed for 
    the same purpose. The NBR2 is calculated as follows:
        NBR2 = (NIR - SWIR2) / (NIR + SWIR2)

    The NBR2 index is sensitive to changes in the vegetation and the charred biomass resulting from a fire, as well as the 
    presence of unburned vegetation and soil background. 
    The values of NBR2 range from -1 to 1, with higher values indicating more severe burn scars. The index is particularly 
    useful in detecting the extent and severity of burn scars in heavily vegetated areas.
    The NBR2 is commonly used in wildfire monitoring and management, as well as in post-fire ecological and land use assessments.

    Args:
        image (ee.ImageCollection): The Sentinel 2 image collection filtered by date and bounds.
        date (pd.Timestamp): The acquisition date in Pandas Timestamp format.
        polygon (ee.Geometry): The field polygon geometry in Earth Engine format.
    
    Returns:
        float: the mean NBR2 value, for the specified date and polygon.
    """
    # Filter image collection to get the image for the date
    image = ee.Image(image.filterDate(date.strftime('%Y-%m-%d'), (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')).first())

    # Calculate NBR2
    nbr2 = image.normalizedDifference(['B11', 'B12']).rename('NBR2')

    # Mask out clouds and shadows
    nbr2 = nbr2.updateMask(image.select('QA60').bitwiseAnd(2).neq(2))

    # Calculate the mean NDVI for the field polygon
    return nbr2.reduceRegion(reducer=ee.Reducer.mean(), geometry=polygon).getInfo()['NBR2']


def get_band(image, date, polygon, id):
    """
    Calculate the Band x value for a specific date and polygon in a Sentinel-2 image collection
    
    Spectral bands refer to specific ranges of electromagnetic radiation (EMR) that are used in remote sensing 
    applications to capture information about the earth's surface. Spectral bands are usually defined by their
    wavelength or frequency, and are typically categorized into broad groups based on their spectral characteristics, 
    such as visible, near-infrared, shortwave infrared, and thermal infrared.
    Each spectral band provides unique information about the reflectance and absorption properties of features on the
    earth's surface. For example, visible bands are sensitive to the reflectance of green vegetation, water, and soil,
    while near-infrared bands are sensitive to the reflectance of healthy vegetation. Shortwave infrared bands can detect
    differences in moisture content and mineralogy, while thermal infrared bands can detect heat signatures.

    Args:
        image (ee.ImageCollection): The Sentinel 2 image collection filtered by date and bounds.
        date (pd.Timestamp): The acquisition date in Pandas Timestamp format.
        polygon (ee.Geometry): The field polygon geometry in Earth Engine format.
        id (int): The id of the BAND to be returned.
    
    Returns:
        float: the mean Band x value, for the specified date and polygon.
    """
    # Filter image collection to get the image for the date
    image = ee.Image(image.filterDate(date.strftime('%Y-%m-%d'), (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')).first())
    
    # Returns the mean band x value
    return image.reduceRegion(reducer=ee.Reducer.mean(), geometry=polygon).getInfo()['B' + str(id)]