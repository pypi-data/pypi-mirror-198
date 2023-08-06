from .blocks import create_grid, spatial_blocks, spatial_kfold_blocks
from .clusters import spatial_kfold_clusters
from .plotting import spatial_kfold_plot, spatial_kfold_autoplot
from .stats import spatial_kfold_stats
from pkg_resources import resource_filename

ames_data = resource_filename(__name__, 'data/ames.geojson')