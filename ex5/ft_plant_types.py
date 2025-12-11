#!/usr/bin/env python3
"""
File: ft_plant_types.py
継承（Inheritance）を使用して、植物の専門クラスを作成するプログラム。
"""


class Plant:
    """
    すべての植物の共通機能を持つ親クラスです

    Attributes:
        name (str): 植物の名前
        height (int): 植物の高さ (cm)
        age (int): 植物の年齢 (日数)
    """

    def __init__(self, name, height, age) -> None:
        """
        共通の属性を初期化
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す
        """
        return f"{self.name} ({self.height}cm, {self.age} days)"


class Flower(Plant):
    """
    Plantの継承として花を表すクラス

    Unique Attributes:
        color（str): 花の色
    """

    def __init__(self, name, height, age, color) -> None:
        """
        属性を初期化
        """
        # 1.親の初期化
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        花が咲く
        """
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> str:
        """
        情報を整形した文字列として返す
        """
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """
    Plantの継承として木を表すクラス

    Unique Attributes:
        trunk_diameter（int): 幹の直径
    """
    def __init__(self, name, height, age, trunk_diameter) -> None:
        """
        属性を初期化
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def gen_shade(self) -> int:
        """
        日陰を生成する
        """
        radius = self.trunk_diameter // 10

        shade = (radius * radius * 314) // 100
        return shade

    def get_info(self) -> str:
        """
        情報を整形した文字列として返す
        """
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    Plantの継承として野菜を表すクラス

    Unique Attributes:
        harvest_season（str): 収穫する季節
        nutritional_value (int): 栄養価
    """
    def __init__(
            self,
            name,
            height,
            age,
            harvest_season,
            nutritional_value
            ) -> None:
        """
        属性を初期化
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """
        情報を整形した文字列として返す
        """
        return (
            f"{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
            )


def main():
    """
    継承したクラスから２つずつインスタンスを作成する
    """

    print("=== Garden Plant Types ===")

    # 1.植物を生成
    plants = [
        Flower("Rose", 25, 30, "Red"),
        Flower("Lily", 40, 15, "White"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1500, 40),
        Vegetable("Tomato", 80, 90, "Summer", "Vitamin C"),
        Vegetable("Carrot", 10, 45, "Autumn", "Beta-carotene"),
    ]

    # 2.情報を出力
    for plant in plants:
        print(plant.get_info())

        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            print(
                f"{plant.name} provides {plant.gen_shade()} "
                f"square meters of shade\n"
                )
        elif isinstance(plant, Vegetable):
            print(f"{plant.name} is rich in {plant.nutritional_value}\n")


if __name__ == "__main__":
    main()
