#!/usr/bin/env python3
"""ガーデナー管理システム"""


# ----３世代植物----
class Plant:
    """植物クラス"""

    def __init__(self, name, height) -> None:
        """
        植物属性を初期化
        """
        self.name: str = name
        self.height: int = height
        self.growth = 0

    def grow(self) -> None:
        """
        植物の高さを1cm増加させる
        """
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す
        """
        return f"{self.name}: {self.height}cm"

    def get_type(self) -> None:
        return "Plant"


class FloweringPlant(Plant):
    """花クラス"""

    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す
        """
        return (
            f"{super().get_info()}, "
            f"{self.color} flowers ({self.is_bloom()})"
        )

    def is_bloom(self) -> str:
        if 0 < self.growth:
            return "blooming"
        else:
            return "not in bloom"

    def get_type(self) -> None:
        return "FloweringPlant"


class PrizeFlower(FloweringPlant):
    """育てる難易度の高い花クラス"""

    def __init__(self, name, height, color, point) -> None:
        super().__init__(name, height, color)
        self.point = point

    def get_info(self) -> str:
        """
        植物の情報を整形した文字列として返す
        """
        return f"{super().get_info()}, Prize point: {self.point}"

    def get_type(self) -> None:
        return "PrizeFlower"


# ----ガーデンマネージャー----
class GardenManager:
    """庭のアドミニストレータ"""

    class GardenStats:
        """計算用関数"""

        @staticmethod
        def calculate_plants(plants: list[Plant], target_class: str) -> int:
            count = 0
            for plant in plants:
                if plant.get_type() == target_class:
                    count += 1
            return count

        @staticmethod
        def calculate_score(plants: list["Plant"]) -> int:
            point = 0
            for plant in plants:
                point += plant.height
                point += plant.growth * 10
                if plant.get_type() == "PrizeFlower":
                    point += plant.point
            return point

        @staticmethod
        def put_calculate_gardeners(gardenaers: list["GardenManager"]) -> None:
            count = 0
            for _ in gardenaers:
                count += 1
            print(f"\nTotal gardens managed: {count}")

        @staticmethod
        def put_garden_score(gardeners: list["GardenManager"]):
            stats = GardenManager.GardenStats
            print("Garden score - ", end="")
            for target_gardener in gardeners:
                print(
                    f"{target_gardener.gardener}: "
                    f"{stats.calculate_score(target_gardener.plants)}",
                    end=" ")

    def __init__(self, gardener) -> None:
        """
        ガーデナーとその庭の空データを作成
        """
        self.gardener = gardener  # 誰のガーデンかを設定
        self.plants: list[Plant] = []  # ここに植物が入る

    @classmethod
    def create_garden_network(cls, *names: str) -> list["GardenManager"]:
        """
        ガーデナーごとに庭管理ツールを作成
        """
        gardeners = [cls(name) for name in names]
        print("creat gardens for", *names)
        return gardeners

    @staticmethod
    def validate_height(plants: list[Plant]) -> bool:
        """
        庭からはみ出してる植物がないか確認
        """
        for plant in plants:
            if plant.height < 1 or 5000 < plant.height:
                return False
        return True

    def add_plant(self, plant_data) -> None:
        """
        庭に植物を植える
        """
        count = 0
        for _ in plant_data:
            count += 1
        if count == 2:
            plant = Plant(*plant_data)
        elif count == 3:
            plant = FloweringPlant(*plant_data)
        elif count == 4:
            plant = PrizeFlower(*plant_data)
        else:
            print("Error")
        self.plants += [plant]
        print(f"Added {plant.name} to {self.gardener}'s garden")

    def grow_all_plans(self):
        """
        ガーデナーが植物が育つのを助ける
        """
        print(f"\n{self.gardener} is helping all plants grow ...")
        for plant in self.plants:
            plant.grow()

    def put_report(self):
        """
        自身の庭をレポートする
        """
        stats = GardenManager.GardenStats
        print(f"\n=== {self.gardener}'s Garden Report ===")
        print("Plants in garden:")
        growth = 0
        for plant in self.plants:
            print(f"- {plant.get_info()}")
            growth += plant.growth
        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {growth}cm"
            )
        print(
            f"Plant types: "
            f"{stats.calculate_plants(self.plants, 'Plant')} regular, "
            f"{stats.calculate_plants(self.plants, 'FloweringPlant')} "
            "flowering, "
            f"{stats.calculate_plants(self.plants, 'PrizeFlower')} "
            "prize flowers"
            )
        print(
            "\nHeight validation test: "
            f"{GardenManager.validate_height(self.plants)}"
            )


def main():
    """ガーデンマネージャーデモ実行関数"""

    print("=== Garden Management System Demo ===\n")

    # 1.ガーデンマネージャーにガーデナーを登録
    gardeners = GardenManager.create_garden_network("Alice", "Bob")

    alice = gardeners[0]
    bob = gardeners[1]

    # 2.庭に植物を植えた
    bob.add_plant(("test", 92))
    plants = (
        ("Oak", 100),
        ("Rose", 25, "red"),
        ("Sunflower", 50, "yellow", 10),
    )
    for plant in plants:
        alice.add_plant(plant)

    # 3.植物を成長させた
    alice.grow_all_plans()

    # 4.庭のレポートを出力
    alice.put_report()

    # 5.ガーデンマネージャのグローバル関数を使用する
    stats = GardenManager.GardenStats
    stats.put_garden_score(gardeners)
    stats.put_calculate_gardeners(gardeners)


if __name__ == "__main__":
    main()
