import numpy as np

from napari_cell_centroid_annotator import annotate_centroids_widget


# make_napari_viewer is a pytest fixture that returns a napari viewer object
def test_annotate_centroids_widget(make_napari_viewer):
    viewer = make_napari_viewer()
    n_points = 100
    ndim = 3
    layer = viewer.add_points(np.random.random((n_points, ndim)))

    # this time, our widget will be a MagicFactory or FunctionGui instance
    annotate_centroids_widget(layer)

    # test if we get the expected number of points
    assert layer.metadata["n_points"] == n_points

    # test if the face color changes when we add a point
    first_face_color = layer.current_face_color
    layer.add(np.random.random((1, ndim)))
    assert layer.current_face_color != first_face_color
