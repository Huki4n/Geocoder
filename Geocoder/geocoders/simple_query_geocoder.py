from api import API
from geocoders.geocoder import Geocoder


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:

      node = API.get_area(area_id)
      path = node.name

      if node.parent_id is None:
        return path

      while node == API.get_area(node.parent_id):
        node = API.get_area(node.parent_id)
        path = node.name + ' ' + path

        if node.parent_id is None:
          break
      return path
