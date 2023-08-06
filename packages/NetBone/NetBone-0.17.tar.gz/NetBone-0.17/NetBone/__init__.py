
"""
NetBone - Easy Backbone extraction library
==================

A Library that simplifies Extracting backbones from networks.
and graphs.
"""

from NetBone.Statistical.disparity import disparity
from NetBone.Structural.h_backbone import h_backbone
from NetBone.Statistical.noise_corrected import noise_corrected
from NetBone.Structural.doubly_stochastic import doubly_stochastic
from NetBone.Structural.high_salience_skeleton import high_salience_skeleton
from NetBone.Statistical.marginal_likelihood import MLF
from NetBone.Statistical.lans import lans
from NetBone.Structural.ultrametric_distance_backbone import ultrametric_distance_backbone
from NetBone.Structural.metric_distance_backbone import metric_distance_backbone
from NetBone.Statistical.global_threshold import global_threshold
from NetBone.Structural.modulairy_backbone import modularity_backbone
from NetBone.Structural.maximum_spanning_tree import maximum_spanning_tree
from NetBone import Compare
from NetBone import Filters
from NetBone import Visualize
from NetBone.Backbone import Backbone
try:
    from NetBone.Statistical.maxent_graph.ecm_main import ecm
except ImportError:
    print("Can't load ECM Model in windows, try using it on linux")


def marginal_likelihood(data):
    mlf = MLF(directed=False)
    return Backbone(mlf.fit_transform(data), name="Marginal Likelihood Filter", column="p_value", ascending=True)




# logger = logging.getLogger()
# logger.setLevel('DEBUG')



