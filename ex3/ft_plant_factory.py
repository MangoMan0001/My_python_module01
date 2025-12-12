#!/usr/bin/env python3
"""
データリストに基づき、工場（Factory）のように連続して植物を作成する。
"""


class Plant:
    """
    庭の植物を表すクラスです

    Attributes:
        name (str): 植物の名前
        height (int): 植物の高さ (cm)
        age (int): 植物の年齢 (日数)
    """

    def __init__(self, name: str, init_height: int, init_age: int) -> None:
        """
        新しい植物インスタンスを初期化します

        Attributes:
            name (str): 植物の名前
            init_height (int): 植物の高さ (cm)
            init_age (int): 植物の年齢 (日数)
        """
        self.name: str = name
        self.height: int = init_height
        self.plant_age: int = init_age

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す。

        Returns:
            str: /整形した植物情報（Name、Height、Age）
        """
        return f"{self.name} ({self.height}cm, {self.plant_age} days)"


def main() -> None:
    """
    植物工場のmain関数
    データリストから植物を生成し、その詳細を出力する。
    """
    # 1.作成データ（タプル）
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    # 2.植物の作成と情報の出力
    count = 0
    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        print(f"Created: {new_plant.get_info()}")
        count += 1

    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
