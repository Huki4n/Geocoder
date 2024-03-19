from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _recursion_enumeration_tree(self, node: TreeNode, area_id: str, path: list[TreeNode] = list):

      path.append(node)

      for region in node.areas:
        new_path = self._recursion_enumeration_tree(region, area_id, path.copy())
        if new_path is not None:
          return new_path

    def _apply_geocoding(self, area_id: str) -> str:

      for node in self.__data:

        if node.parent_id is None:
          return node.name

        path = self._recursion_enumeration_tree(node, area_id, [])
        if path:
          address = " ".join([part_path.name for part_path in path])
          return address


