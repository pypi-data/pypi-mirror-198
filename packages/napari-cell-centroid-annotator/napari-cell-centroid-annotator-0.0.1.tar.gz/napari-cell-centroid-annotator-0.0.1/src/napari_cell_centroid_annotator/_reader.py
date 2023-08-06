"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the Reader specification, but your plugin may choose to
implement multiple readers or even other plugin contributions. see:
https://napari.org/stable/plugins/guides.html?#readers
"""
from pathlib import Path

import numpy as np
import pandas as pd
import tifffile


def napari_get_reader(path):
    """A basic implementation of a Reader contribution.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    if isinstance(path, str):
        path = Path(path)

    # if we know we cannot read the file, we immediately return None.
    if path.suffix in [".tif", ".tiff"]:
        return img_reader_function
    elif path.suffix in [".npy", ".csv"]:
        return points_reader_function
    else:
        return None


def img_reader_function(path):
    """Reader function for our supported image types."""
    path = Path(path)
    if path.suffix not in [".tif", ".tiff"]:
        raise ValueError("File must be a tiff file")

    data = tifffile.imread(path)

    # optional kwargs for the corresponding viewer.add_* method
    add_kwargs = {
        "name": path.stem,
        "colormap": "gray",
        "blending": "additive",
    }

    layer_type = "image"  # optional, default is "image"
    return [(data, add_kwargs, layer_type)]


def points_reader_function(path):
    """Reader function for our supported point types."""
    path = Path(path)
    if path.suffix not in [".npy", ".csv"]:
        raise ValueError("File must be a numpy array or csv file")
    if path.suffix == ".csv":
        df = pd.read_csv(path, header=0)
        data = df[["axis-0", "axis-1", "axis-2"]].values
        data = data.astype(float)
    else:
        data = np.load(path).astype(float)

    # optional kwargs for the corresponding viewer.add_* method
    add_kwargs = {
        "name": path.stem,
        "size": 10,
        "symbol": "disc",
        "face_color": np.random.random((data.shape[0], 3)),
        "edge_color": "black",
        "out_of_slice_display": True if data.shape[1] == 3 else False,
    }

    layer_type = "points"  # optional, default is "image"
    return [(data, add_kwargs, layer_type)]
