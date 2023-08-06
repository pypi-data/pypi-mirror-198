import pkg_resources

dirpath = pkg_resources.resource_filename(__name__, 'assets')

PANDA_URDF = dirpath + "/urdfs/panda/franka_panda.urdf"
HAND_URDF = dirpath + "/urdfs/panda/hand.urdf"
