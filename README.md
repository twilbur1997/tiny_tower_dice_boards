### Table of Contents  

[Intro](#intro)  

[Results](#results) 

[Board Images](#board-images)

[Board Tables](#board-tables)


---



# Intro

This is the start of this project. This project will simulate 100 dice rolls across 10,000 trials for the Tiny Tower Dice Boards and publish the results.

For now there are just images and tables for the dice boards.

The code is being developed and is expected to be published on or around 8:00pm USA Pacific time on Tuesday, November 25, 2025.


---

# Statistic Intro (or Refresher!)

*See below for basics of the statistics used in the project*


## Expected Value Problem

Let's say I offer you a game based on dice rolls. Each roll costs you $3, but there are potential rewards. 

1. $1 per pip on the resulting dice face (i.e. rolling a 6 is worth $6)
2. $5 if an even number is rolled 
3. $20 per #6 rolled


Which should you take?


*Some assumptions:*
1. *You are rolling using a standard 6-sided dice*
2. *The dice is evenly weighted (uniform distribution)*
3. *Each face has pips numbering 1, 2, 3, 4, 5, and 6*


**Note*: a "pip" is the word for a single dot on the side of a dice.


The answer is below, but take a second to think on it yourself.

<details>
  <summary>Answer and Explanation</summary>
  
1. $1 per pip:
    - This is the same as $1 per 1, $2 per 2, […], $6 per 6 rolled
    - Expected value: =SUM($1,$2,$3,$4,$5,$6)/6 = $21/6 = $3.50 per roll
2. $5 per even number:
    - This is the same as $0 per 1, $5 per 2, [...] $5 per 6
    - Expected value: =SUM($0,$5,$0,$5,$0,$5)/6 = $15/6 = $2.50 per roll
3. $20 per #6:
    - This is the same as $0 per 1, $0 per 2, [...], $20 per 6
    - Expected value: =SUM($0,$0,$0,$0,$0,$20)/6 = $20/6 = $3.33 per roll


So, we have found that the expected value is highest for Option #1
  
</details>


<br /> 

The above results are easy to use math to reason through hypothetically. However, you can also simulate this using computer programming. Using many, many rolls, you can arrive at an answer that matches the above!

This is how we will determine how valuable each roll is for the Tiny Tower's dice minigame. By using thousands or millions of rolls, we don't have to have exact formulas, we can simply approximate the average value. 

For easier to understand numbers, the results below assume you roll the dice 100 times. This means (for example) instead of earning 0.15 chests per roll, you earn 15 chests per 100 rolls, which is easier to compare between boards.

---

# Results

This will be filled out by the date/time above.

---

# Board Images

The following boards are organized (A, B, C, Event (if applicable))

Note that Coins are not standardized between screenshots, and Coin rewards are directly related to how many floors are in the current tower.

To standardize Coins, the tables below list Coin rewards as a percentage of the cost of a new floor.

## Free Boards:


| Board A | Board B | Board C | Thanksgiving 2025 |
|----------|----------|----------|----------|
| <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_a_free_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_b_free_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_c_free_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_thksgvg2025_free_tiles.png" width="200"> | 
| <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_a_free_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_b_free_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_c_free_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_thksgvg2025_free_special.png" width="200"> |


## Premium Boards:

| Board A | Board B | Board C | Thanksgiving 2025 | 
|----------|----------|----------|----------|
| <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_a_premium_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_b_premium_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_c_premium_tiles.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_thksgvg2025_premium_tiles.png" width="200"> |
| <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_a_premium_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_b_premium_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_c_premium_special.png" width="200"> | <img src="https://github.com/twilbur1997/tiny_tower_dice_boards/blob/main/pictures_dice_boards/board_thksgvg2025_premium_special.png" width="200"> |


---


# Board Tables

The following tables describe the tables 

Please note the following:
1. Tokens are listed as a description of their icon 
    - Bronze Key = Regular Token
2. Coins are listed as a percentage of how much it costs to build a floor
    - If a new floor in your tower costs 10,000 coins, a "10% Coins" will give 1,000 coins
3. The "???" tile is also referred to as "Mystery" in some places since the code wouldn't let me use "???" in some variable names. 
4. There may be errors in the following table!! Let me know in the Tiny Tower Discord @ToadTruck




|   | AFree | BFree | CFree | Thanksgiving2025Free |
| ------- | ------- | ------- | ------- | ------- |
| Tile 1 | 250 Bux | 250 Bux | REVERSE | 300 Bux | 
| Tile 2 | 1 Bronze Key | 1 Bronze Key | 1 ??? | 13 % Coins | 
| Tile 3 | 200 Bux | 200 Bux | 400 Bux | REVERSE | 
| Tile 4 | 12 % Coins | 12 % Coins | 1 Golden Dice | 1 Tier 1 Chest | 
| Tile 5 | REVERSE | REVERSE | FORWARD | 20 % Coins | 
| Tile 6 | 250 Bux | 1 Golden Dice | 1 Silver Key | 1 Ad Chest | 
| Tile 7 | 10 % Coins | 10 % Coins | 500 Bux | 5 Bronze Keys | 
| Tile 8 | 1 Ad Chest | 1 Ad Chest | 13 % Coins | REVERSE | 
| Tile 9 | 300 Bux | 1 Tier 1 Chest | 1 Tier 1 Chest | 2 Silver Keys | 
| Tile 10 | 16 % Coins | 16 % Coins | 1 Tier 1 Chest | 1 Tier 1 Chest | 
| Tile 11 | 1 Tier 1 Chest | 1 Tier 1 Chest | 10 % Coins | FORWARD | 
| Tile 12 | 1 ??? | 1 ??? | REVERSE | 1 Golden Dice | 
| Tile 13 | FORWARD | FORWARD | 3 Bronze Keys | 500 Bux | 
| Tile 14 | 12 % Coins | 12 % Coins | 1 Ad Chest | 1 ??? | 
| Tile 15 | 300 Bux | 500 Bux | 300 Bux | 10 % Coins | 
| Tile 16 | 10 % Coins | 10 Legendary Ticket? | 20 % Coins? | 5 Bronze Keys? | 
| Mystery 1 | <sub>40% : 1 Tier 1 Chest</sub> | <sub>40% : 1 Tier 1 Chest</sub> | <sub>50% : 1500 Bux</sub> | <sub>50% : 40 Pies (40 Bux)</sub> | 
| Mystery 2 | <sub>30% : 1 Bronze Keys</sub> | <sub>30% : 3 Golden Dice</sub> | <sub>25% : 1 Tier 3 Chest</sub> | <sub>30% : 1 Tier 2 Chest</sub> | 
| Mystery 3 | <sub>20% : 1 Golden Ticket</sub> | <sub>20% : 1 Golden Ticket</sub> | <sub>15% : 5 Gold Keys</sub> | <sub>15% : 5 Golden Dice</sub> | 
| Mystery 4 | <sub>10% : 3 Silver Keys</sub> | <sub>10% : 10 Legendary Ticket</sub> | <sub>10% : 1 Golden Ticket</sub> | <sub>5% : 30 Legendary Tickets</sub> | 





|   | APremium | BPremium | CPremium | Thanksgiving2025Premium |
| ------- | ------- | ------- | ------- | ------- |
| Tile 1 | 90 % Coins | 33 % Coins | FORWARD | 25 Bronze Keys | 
| Tile 2 | 1 Tier 2 Chest | 1 Tier 1 Chest | 10 Legendary Ticket | 3 Legendary Tickets | 
| Tile 3 | 1 Legendary Ticket | 1 Legendary Ticket | 5 Silver Key | 67 % Coins | 
| Tile 4 | 300 Bux | 500 Bux | 1 ??? | REVERSE | 
| Tile 5 | REVERSE | REVERSE | 750 Bux | 10 Silver Keys | 
| Tile 6 | 5 Bronze Keys | 1 Tier 1 Chest | 3 Silver Keys | 1 Gold Key | 
| Tile 7 | 300 Bux | 100 Bux | 58 % Coins | 1 Tier 2 Chest | 
| Tile 8 | 1 Legendary Ticket | 10 Legendary Ticket | 5 Legendary Ticket | FORWARD | 
| Tile 9 | 5 Bronze Keys | 1 Silver Key | 15 Bronze Keys | 25 Bronze Keys | 
| Tile 10 | 90 % Coins | 133 % Coins | 500 Bux | 10 Legendary Tickets | 
| Tile 11 | 1 Tier 2 Chest | 15 Silver Keys | 5 Silver Keys | 1 Tier 2 Chest | 
| Tile 12 | 1 ??? | 1 ??? | 3 Legendary Ticket | 1 ??? | 
| Tile 13 | FORWARD | FORWARD | 44 % Coins | 5 Legendary Tickets | 
| Tile 14 | 3 Silver Keys | 1 Silver Key | REVERSE | 67 % Coins | 
| Tile 15 | 90 % Coins | 33 % Coins | 5 Silver Keys | 15 Silver Keys | 
| Tile 16 | 10 Legendary Tickets | 10 Legendary Ticket? | 1 Tier 2 Chest | 500 Bux | 
| Mystery 1 | <sub>50% : 1 Tier 3 Chest</sub> | <sub>50% : Tier 3 Chest</sub> | <sub>55% : 30 Silver Keys</sub> | <sub>40% : 100 Pies (100 Bux)</sub> | 
| Mystery 2 | <sub>30% : 3 Golden Tickets</sub> | <sub>30% : 5 Golden Dice</sub> | <sub>25% : 3 Golden Tickets</sub> | <sub>30% : 25 Legendary Tickets</sub> | 
| Mystery 3 | <sub>15% : 1 Tier 4 Chest</sub> | <sub>15% : 100 Bronze Keys</sub> | <sub>15% : 1 Tier 4 Chest</sub> | <sub>20% : 1 Tier 4 Chest</sub> | 
| Mystery 4 | <sub>5% : 100 Legendary Tickets</sub> | <sub>5% : 110 Silver Keys</sub> | <sub>5% : 100 Legendary Tickets</sub> | <sub>10% : 5 Golden Tickets</sub> | 


