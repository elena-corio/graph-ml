from topologicpy.Topology import Topology
from topologicpy.Dictionary import Dictionary

#====================================================
# Utility functions to reset the face dictionaries and transfer dictionaries by key
#====================================================

def reset_dictionaries(shell):
    faces = Topology.Faces(shell)
    for i, f in enumerate(faces):
        d = Topology.Dictionary(f)
        keys = Dictionary.Keys(d)
        for key in keys:
            if not key == "face_id":
                d = Dictionary.RemoveKey(d, key)
        f = Topology.SetDictionary(f, d)

def transfer_dicts_by_key(topologies, selectors, key):
    dicts = {}
    for t in topologies:
        d = Topology.Dictionary(t)
        value = Dictionary.ValueAtKey(d, key, None)
        if value:
            dicts[str(value)] = t
    
    for s in selectors:
        d = Topology.Dictionary(s)
        value = Dictionary.ValueAtKey(d, key, None)
        if value:
            f = dicts[str(value)]
            f = Topology.SetDictionary(f, d)