#!/usr/bin/env python3

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



if __name__ == "__main__":
    main()
