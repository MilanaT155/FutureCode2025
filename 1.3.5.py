#1
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union1 = A | B
print("Объединение через |:", union1)
union2 = A.union(B)
print("Объединение через .union():", union2)
#2
materials = {"кирпич", "дерево", "стекло"}
player_items = {"дерево", "гвозди"}
missing_materials = materials - player_items
print("Не хватает материалов:", missing_materials)
#3
all_artifacts = {"меч", "щит", "кольцо", "амулет"}
player_artifacts = {"меч", "амулет"}
is_subset = player_artifacts <= all_artifacts
print("Является ли набор игрока подмножеством всех артефактов?", is_subset)
#4
resources = {"золото", "уголь", "руда"}

resources.add("алмаз")
print("После добавления 'алмаз':", resources)

resources.add("уголь")
print("После попытки добавить 'уголь' снова:", resources)
#5
inventory = {"яблоко", "ключ", "карта"}
if "ключ" in inventory:
    print("Ключ есть в инвентаре")
else:
    print("Ключа нет в инвентаре")
inventory.add("факел")
print("После добавления факела:", inventory)
inventory.discard("яблоко")
print("После удаления яблока:", inventory)