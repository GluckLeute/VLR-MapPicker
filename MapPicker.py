import random
from collections.abc import Iterable
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
        self._validate_targets(ban_maps, "ban_maps")

        for target in ban_maps:
            delete_key = self._resolve_map_key(target)
            if delete_key in self.maps:
                del self.maps[delete_key]

    def add_maps(self, add_maps_list: list[int | str]) -> None:
        self._validate_targets(add_maps_list, "add_maps_list")

        for target in add_maps_list:
            add_key = self._resolve_map_key(target)
            self.maps[add_key] = self.MAPS[add_key]

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

    def _validate_targets(self, targets: Iterable[int | str], argument_name: str) -> None:
        if not isinstance(targets, Iterable) or isinstance(targets, (str, bytes)):
            raise TypeError(f"{argument_name} には int または str のリストを渡してください。")

    def _resolve_map_key(self, target: int | str) -> int:

        if isinstance(target, int):
            if target in self.MAPS:
                return target
            raise ValueError(f"無効なマップ番号です: {target}")

        if isinstance(target, str):
            normalized_target = target.strip()
            if not normalized_target:
                raise ValueError("空文字列はマップ指定として使用できません。")

            if normalized_target.isdigit():
                key = int(normalized_target)
                if key in self.MAPS:
                    return key
                raise ValueError(f"無効なマップ番号です: {target}")

            for key, map_name in self.MAPS.items():
                if map_name.lower() == normalized_target.lower():
                    return key
            raise ValueError(f"無効なマップ名です: {target}")

        raise TypeError(f"int または str でマップを指定してください: {target}")
