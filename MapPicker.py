import random
from types import MappingProxyType
from typing import Final

class MapPicker:

    MAPS: Final = MappingProxyType(
        {
            1: "BIND",
            2: "HAVEN",
            3: "SPLIT",
            4: "ASCENT",
            5: "ICEBOX",
            6: "BREEZE",
            7: "FRACTURE",
            8: "PEARL",
            9: "LOTUS",
            10: "SUNSET",
            11: "ABYSS",
            12: "CORRODE",
        }
    )

    def __init__(self, ban_maps = None):

        self.maps = dict(self.MAPS)
        if ban_maps:
            self.remove_maps(ban_maps)

    def remove_maps(self, ban_maps: list[int | str]) -> None:
        for target in ban_maps:
            delete_key = None

            # 数字指定の場合
            if isinstance(target, int):
                if target in self.maps:
                    delete_key = target

            # 文字列指定の場合
            elif isinstance(target, str):
                target = target.strip()

                # "1" のような数字文字列なら番号として扱う
                if target.isdigit():
                    key = int(target)
                    if key in self.maps:
                        delete_key = key
                else:
                    # マップ名として比較（大文字小文字無視）
                    for k, v in self.maps.items():
                        if v.lower() == target.lower():
                            delete_key = k
                            break
            if delete_key is not None:
                del self.maps[delete_key]

    def add_maps(self, add_maps_list: list[int | str]) -> None:
        for target in add_maps_list:
            if isinstance(target, int):
                if 1 <= target <= len(self.MAPS):
                    self.maps[target] = self.MAPS[target]
            elif isinstance(target, str):
                target = target.strip()
                if target.isdigit():
                    key = int(target)
                    if 1 <= key <= len(self.MAPS):
                        self.maps[key] = self.MAPS[key]
                else:
                    for k, v in self.MAPS.items():
                        if v.lower() == target.lower():
                            self.maps[k] = v
                            break

    def pick_random_maps(self, count: int = 1) -> dict[int, str]:
        if not self.maps:
            raise ValueError("選択可能なマップがありません。")

        selected_keys = random.sample(list(self.maps.keys()), min(count, len(self.maps)))

        selected_maps = {}
        for key in selected_keys:
            selected_maps[key] = self.maps[key]

        return selected_maps
    
    def get_maps(self) -> dict[int, str]:
        return self.maps.copy()

    def init(self) -> None:
        self.maps = dict(self.MAPS)
