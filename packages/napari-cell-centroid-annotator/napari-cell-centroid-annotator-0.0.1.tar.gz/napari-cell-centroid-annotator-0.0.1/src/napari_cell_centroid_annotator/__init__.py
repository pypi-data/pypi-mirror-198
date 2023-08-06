try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._reader import napari_get_reader
from ._widget import annotate_centroids_widget

__all__ = ("napari_get_reader", "annotate_centroids_widget")
