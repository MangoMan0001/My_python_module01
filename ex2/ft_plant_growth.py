#!/usr/bin/env python3
"""成長シミュレーター"""


class Plant:
    """
    成長機能を持つ庭の植物を表すクラスです

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

    def grow(self, size: int) -> None:
        """
        植物の高さを増加させます。

        Args:
            size (int): 成長する高さ (cm)
        """
        self.height += size

    def age(self, day: int) -> None:
        """
        植物の年齢を増加させます。

        Args:
            day(int): 増加する日数
        """
        self.plant_age += day

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す。

        Returns:
            str: /整形した植物情報（Name、Height、Age）
        """
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


def main() -> None:
    """
    植物の１週間をシミュレートするメイン関数
    """
    # 1.植物作成(配列として初期化)
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    # 2.成長前のinfoを記録して標準出力
    init_height = {p.name: p.height for p in plants}
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    # 3.成長日数を設定
    growth_days = 6
    days = 0
    while days < growth_days:
        for plant in plants:
            plant.age(1)
            plant.grow(1)
        days += 1

    # 4.成長後のinfoを出力
    print(f"=== Day {1 + growth_days} ===")
    for plant in plants:
        print(plant.get_info())

        growth = plant.height - init_height[plant.name]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
