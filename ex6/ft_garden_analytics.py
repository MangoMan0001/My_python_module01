#!/usr/bin/env python3

class Plant:
    """
    すべての植物の共通機能を持つ親クラスです
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



if __name__ == "__main__":
