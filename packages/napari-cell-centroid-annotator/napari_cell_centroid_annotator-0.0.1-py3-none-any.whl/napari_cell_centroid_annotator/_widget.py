"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    import napari


# Uses the `autogenerate: true` flag in the plugin manifest
# to indicate it should be wrapped as a magicgui to autogenerate
# a widget.
def annotate_centroids_widget(points_layer: "napari.layers.Points"):
    points_layer.out_of_slice_display = (
        True if points_layer.data.shape[1] == 3 else False
    )
    points_layer.point_size = 10
    points_layer.current_face_color = np.random.random((1, 3))
    points_layer.metadata["n_points"] = points_layer.data.shape[0]

    @points_layer.events.set_data.connect
    def on_data_change():
        if points_layer.metadata["n_points"] + 1 == points_layer.data.shape[0]:
            points_layer.metadata["n_points"] += 1
            points_layer.current_face_color = np.random.random((1, 3))
        elif (
            points_layer.metadata["n_points"] - 1 == points_layer.data.shape[0]
        ):
            points_layer.metadata["n_points"] -= 1
