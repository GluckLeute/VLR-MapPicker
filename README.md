# VLR-MapPicker

VALORANTのマッププールから、ランダムにマップを選ぶためのシンプルなPythonライブラリです。  
マップの除外、再追加、リセットに対応。



## 動作環境

- Python 3.10 以上


## 使い方

### 1. そのままランダムで 1 マップ選ぶ

```python
from MapPicker import MapPicker

picker = MapPicker()
result = picker.pick_random_maps()
print(result)
```

出力例:

```python
{4: 'ASCENT'}
```

### 2. 特定のマップを除外して選ぶ

インスタンス化時、番号または名前で除外。

```python
from MapPicker import MapPicker

picker = MapPicker(ban_maps=[1, "HAVEN", "10"])
result = picker.pick_random_maps(3)
print(result)
```

インスタンス化後の除外。

```python
from MapPicker import MapPicker

picker = MapPicker()
picker.remove_maps(ban_maps=[1, "HAVEN", "10"])
result = picker.pick_random_maps(3)
print(result)
```

### 3. 除外したマップを再追加する

```python
from MapPicker import MapPicker

picker = MapPicker(ban_maps=["BIND", "ICEBOX"])
picker.add_maps(["BIND"])

print(picker.get_maps())
```

### 4. 現在のマッププールを確認する

```python
from MapPicker import MapPicker

picker = MapPicker(ban_maps=["BIND", "HAVEN"])
print(picker.get_maps())
```

### 5. マッププールを初期状態に戻す

```python
from MapPicker import MapPicker

picker = MapPicker(ban_maps=["BIND", "HAVEN"])
picker.init()

print(picker.get_maps())
```

## 詳細

### `MapPicker(ban_maps=None)`

マッププールを初期化します。`ban_maps` を渡すと、指定したマップを除外した状態で開始します。

### `remove_maps(ban_maps)`

指定したマップを現在のプールから削除します。

- `int`: マップ番号
- `str`: マップ名または数字文字列

### `add_maps(add_maps_list)`

指定したマップを現在のプールへ再追加します。

### `pick_random_maps(count=1)`

現在のプールからランダムにマップを選びます。戻り値は `{番号: 名前}` の辞書です。  
指定数が現在のマップ数を超える場合は、存在する分だけ返します。

選択可能なマップが 0 件の場合は `ValueError` を送出します。

### `get_maps()`

現在のマッププールを辞書で返します。

### `init()`

マッププールを初期状態に戻します。

## 登録マップ

現在の実装では、以下の 12 マップが登録されています。

| 番号 | マップ名 |
| --- | --- |
| 1 | BIND |
| 2 | HAVEN |
| 3 | SPLIT |
| 4 | ASCENT |
| 5 | ICEBOX |
| 6 | BREEZE |
| 7 | FRACTURE |
| 8 | PEARL |
| 9 | LOTUS |
| 10 | SUNSET |
| 11 | ABYSS |
| 12 | CORRODE |
