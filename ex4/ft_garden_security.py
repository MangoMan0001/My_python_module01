#!/usr/bin/env python3
"""
File: ft_garden_security.py
データの整合性を守るために、GetterとSetterを実装しています。
負の値などの不正なデータをブロックするセキュリティ機能を持っています。
"""


class SecurePlants:
    """
    セキュリティ機能（カプセル化）を持つ植物クラス

    Attributes:
        _name (str): 植物の名前（内部変数）。
        _height (int): 植物の高さ（内部変数）。
        _age (int): 植物の年齢（内部変数）。
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        植物インスタンスの初期化
        初期化時にセキュリティチェックを行う。

        Args:
            name（str）: 植物の名前
            height（int）: 植物の高さ
            age（int）: 植物の年齢
        """
        self._name = name
        # 1.内部変数として宣言し、初期化
        self._height = 0
        self._age = 0

        # 2.setterを通す
        self.set_height(height)
        self.set_age(age)

    # ---　nameメソッド　---

    def get_name(self) -> str:
        """
        nameを返す。
        """
        return self._name

    # ---　heightメソッド　---

    def get_height(self) -> int:
        """
        heightを返す。
        """
        return self._height

    def set_height(self, height: int) -> None:
        """
        heightを安全に設定する（負の値は入らない）
        """
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = height

    # ---　ageメソッド　---

    def get_age(self) -> int:
        """
        ageを返す。
        """
        return self._age

    def set_age(self, age: int) -> None:
        """
        ageを安全に設定する（負の値は入らない）
        """
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = age

    # ---　メインメソッド　---

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
        return f"{self._name} ({self._height}cm, {self._age} days)"


def main():
    """
    セキュリティシステムの動作テストを行います。
    """
    print("=== Garden Security System ===")

    # 1.Roseを作成
    rose = SecurePlants("Rose", 25, 30)
    print(f"Plant created: {rose.get_name()}")

    # 2.正常なupdate
    rose.set_height(25)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]\n")

    # 3.不正なupdate
    print("Invalid operation attempted: height -5cm [REJECTED]")
    rose.set_age(-5)

    # 4.現在の情報を出力
    print(f"Current plant: {rose.get_info()}")


if __name__ == "__main__":
    main()
