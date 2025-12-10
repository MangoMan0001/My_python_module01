#!/usr/bin/env python3
"""
File: ft_garden_intro.py
このスクリプトは、基本的な植物情報表示システムを導入するものです
"""


def main() -> None:
    """
    スクリプトを実行するメイン関数です

    Description:
        植物の情報を変数に格納し、整形して表示します
    """
    name = "Rose"
    height = "25"
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
