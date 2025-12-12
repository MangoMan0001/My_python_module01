#!/usr/bin/env python3
"""
File: ft_garden_data.py
Plantクラスを使用して複数の植物データを管理します
"""


class Plant:
    """
    庭の植物を表すクラスです

    Attributes:
        name (str): 植物の名前
        height (int): 植物の高さ (cm)
        age (int): 植物の年齢 (日数)
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        新しい植物インスタンスを初期化します

        Args:
            name (str): 植物の名前
            height (int): 植物の高さ (cm)
            age (int): 植物の年齢 (日数)
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def main() -> None:
    """
    Plantクラスを表示するためのメイン関数です。
    3つの植物インスタンスを作成し、それぞれの情報を表示します。
    """
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")


if __name__ == "__main__":
    main()
