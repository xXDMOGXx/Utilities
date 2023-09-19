desired_tier = int(input("What tier blood tank do you want to make? "))

COST_T1_GLASS = 2
COST_TANK_RUNE = 5
COST_RUNE_SLATE = 2
COST_RUNE_STONE = 6
COST_SLATE_BLOOD = 1000

total_t1 = 2**(desired_tier - 1)
total_runes = total_t1*COST_TANK_RUNE+((total_t1-2)*COST_TANK_RUNE)+COST_TANK_RUNE
total_glass = 2**desired_tier
total_slate = total_runes * COST_RUNE_SLATE
rune_stone = total_runes * COST_RUNE_STONE
total_blood = total_slate * COST_SLATE_BLOOD
total_tiles = int(total_runes / 5)
total_shards = total_tiles // 16 + 1
leftover_tiles = (total_shards * 16) - total_tiles
total_stone = rune_stone + total_slate + total_shards
total_sales_cost = (total_tiles * 10000) + 30000

print("A Tier", desired_tier, "Blood Tank will take:")
print("Glass:", total_glass, "or", total_glass // 64, "Stacks and", total_glass % 64)
print("Blank Runes:", total_runes, "or", total_runes // 64, "Stacks and", total_runes % 64)
print("- Blank Slates:", total_slate, "or", total_slate // 64, "Stacks and", total_slate % 64)
print("- Stone:", rune_stone, "or", rune_stone // 64, "Stacks and", rune_stone % 64)
print("Bloodstone Tiles:", total_tiles, "or", total_tiles // 64, "Stacks and", total_tiles % 64)
print("- Stone:", total_shards)
print("- Weak Blood Shards:", total_shards, "leaving", leftover_tiles, "leftover tiles")
print("")
print("For a total resource requirement of:")
print("- Stone:", total_stone, "or", total_stone // 64, "Stacks and", total_stone % 64)
print("- Glass:", total_glass, "or", total_glass // 64, "Stacks and", total_glass % 64)
print("- Weak Blood Shards:", total_shards)
print("- Blood:", total_blood)
print("")
print("You will make the Tier", desired_tier, "tank by merging", total_t1, "Tier 1 tanks")
print("This sells for ", total_sales_cost, "RELs")
