import random
import pprint
import time
import statistics
import json


# TODO include a naive approach that just divides all resources by 1/16 on the board and adds them together
#       That could also be done by just rolling a ton of ones (as long as the REVERSE doesn't exist)!

# Global variables
# Note: Multiplying TRIALS and ROLLS to 1,000,000 (10^6) is quick, 10,000,000 (10^7) takes up to 10 seconds
NUM_TRIALS = 10**3
NUM_ROLLS = 10**3
ROUND_PRECISION = 2 # Round to this many decimal places for the means
STATUS_CHECK_FREQUENCY = 20 # Check progress by 5% each time, making 20 checks in 100% of progress
PRINT_PERCENT = False
BOARD_NAMES = [
    "BoardAFree", "BoardBFree", "BoardCFree",
    "BoardAPremium", "BoardBPremium", "BoardCPremium"
    ]
DICE_BOARDS_FILE = "dice_boards.json"
DICE_RESULTS_FILE = "results_all_boards.json"

ALL_RESOURCE_LIST = [
    "Coins",
    "Bux",
    "Ad Chest",
    "Tier 1 Chest",
    "Tier 2 Chest",
    "Tier 3 Chest",
    "Tier 4 Chest",
    "Bronze Key",
    "Silver Key",
    "Gold Key",
    "Golden Dice",
    "Golden Ticket",
    "Legendary Ticket",
    "???"
]


def json_read(board_name, file_name=DICE_BOARDS_FILE):
    data = None
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print("Error: The file 'example.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file. Check for malformed JSON.")

    tile_list = data[board_name]
    mystery_name = board_name + "_Mystery"
    mystery_list = data[mystery_name]

    return tile_list, mystery_list


def simulate_dice(board_name, calc_mystery = True):
    resource_list = {
        "Coins": 0,
        "Bux": 0,
        "Ad Chest": 0,
        "Tier 1 Chest": 0,
        "Tier 2 Chest": 0,
        "Tier 3 Chest": 0,
        "Tier 4 Chest": 0,
        "Bronze Key": 0,
        "Silver Key": 0,
        "Gold Key": 0,
        "Golden Dice": 0,
        "Golden Ticket": 0,
        "Legendary Ticket": 0,
        "???": 0
    }

    # current state vs. next state is constant - 1/6 chance for each of [1,2,3,4,5,6]
    rand_list=[random.randint(1, 6) for _ in range(NUM_ROLLS)]
    
    # other options for testing with just rolling ones, etc.
    # NOTE: Rolling all ones on a board with "REVERSE" tiles(s) will result getting the same tile many times
    # rand_list=[1 for _ in range(NUM_ROLLS)]
    # rand_list=[6 for _ in range(NUM_ROLLS)]
    # print(rand_list[:10])

    tile_list, mystery_list = json_read(board_name=board_name)
    total_steps = -1 # If rolling a 1 to start, the array index should be zero
    for roll in rand_list:
        debug_str = ""
        total_steps += roll
        total_steps = total_steps%len(tile_list) # if total_steps exceeds the length of the list
        tile = tile_list[total_steps]

        # Check if FORWARD or REVERSE Tile
        if tile == "REVERSE":
            total_steps -= roll # subtract the roll we just took
            total_steps = total_steps % len(tile_list) # if total_steps goes negative
            tile = tile_list[total_steps]
            debug_str = debug_str + "REVERSE \n"
        
        elif tile == "FORWARD":
            total_steps += roll
            total_steps = total_steps%len(tile_list) # if total_steps exceeds the length of the list
            tile = tile_list[total_steps]
            debug_str = debug_str + "FORWARD \n"

        # Ok, we've now landed on a regular resource after checking for Forward or Reverse Tiles      
        regular_resource = False # That said, let's be sure with a quick check
        for tile_type in resource_list.keys():
            if tile_type in tile: # add to the resource counter
                regular_resource = True
                quantity_resource = tile.split(" ")[0]
                resource_list[tile_type] += int(quantity_resource)
                
                debug_str = debug_str+str(roll)+" "+str(total_steps)+" "+str(tile_type)+" "+str(quantity_resource)
                # print(debug_str)
                # time.sleep(0.5)
                break
        
        if regular_resource == False: # This trips if the tile type is not listed in our overall resource catalog
            print("RESOURCE NOT RECOGNIZED") # (usually due to a typo in the JSON)
            print_str = "\t"+tile
            print(print_str)
    
    if calc_mystery: # Now, we'll replace the "???" resource with the appropriate resources. 
        # Set this conditional to "false" to see how many ??? tiles are expected
        total_mystery_landings = resource_list["???"]
        resource_list["???"] = 0 # Set this to zero to show they've been counted

        proportional_mystery = False
        if proportional_mystery: # Add proportional amount of each resource instead of simulating chance
            # print("\n\nTODO - sorry!\n\n")
            proportional_mystery = True

        else:
            mystery_weights = []
            mystery_prizes = []
            for key, value in mystery_list.items():
                # NOTE - EXAMPLE:  "Reward1": ["40% chance", "1 Tier 1 Chest"]
                chance_string = value[0]
                reward_string = value[1]
                
                chance_num = chance_string.split(" ")[0] # Get first part of "40% chance" to "40%"
                chance_num = int(chance_num.replace("%", "")) # Get to integer by removing "%" and int casting

                mystery_weights.append(chance_num)
                mystery_prizes.append(reward_string)

            prizes_won = random.choices(mystery_prizes, weights=mystery_weights, k=total_mystery_landings)

            for prize in prizes_won:
                # With this list of prizes, add them to the resource list
                regular_resource = False # Remember to check the resources
                for tile_type in resource_list.keys():
                    if tile_type in prize: # add to the resource counter
                        regular_resource = True
                        quantity_resource = prize.split(" ")[0]
                        resource_list[tile_type] += int(quantity_resource)
                        
                        debug_str = debug_str+str(roll)+" "+str(total_steps)+" "+str(tile_type)+" "+str(quantity_resource)
                        # print(debug_str)
                        # time.sleep(0.5)
                        break
                
                if regular_resource == False: # This trips if the prize type is not listed in our overall resource catalog
                    print("RESOURCE NOT RECOGNIZED") # (usually due to a typo in the JSON)
                    print_str = "\t"+prize
                    print(print_str)
            

    for key in resource_list.keys(): # Normalize to 100 rolls
        resource_list[key] = resource_list[key]/(NUM_ROLLS/100)
    # pprint.pprint(resource_list)
    
    return resource_list


def process_ind_trials_dict(independent_trials):
    # simple way to print independent trials dictionary
    last_key = None
    for key, value in independent_trials.items():
        if last_key != key[-4:]:
            print("\n")
            last_key = key[-4:]

        str_to_print = str(key)+": "+str(value)
        print(str_to_print)
    return


def process_ind_trials_matrix(trials_matrix, board_name):
    trials_matrix_means = {}

    print_str = "Board: " + board_name + "\n| Resource | Mean | Standard Deviation |\n| ------- | ------- | ------- |\n"
    for key, resource_list in trials_matrix.items():
        mean_value = round(statistics.mean(resource_list),ROUND_PRECISION)
        stdev_value = round(statistics.stdev(resource_list),ROUND_PRECISION)
        trials_matrix_means[key] = mean_value
        
        # temp_row = f"| Coins | 1300 | 30|\n"
        temp_row = f"| {key} | {mean_value} | {stdev_value} |\n"
        print_str = print_str + temp_row
    # print(print_str)
    print(print_str.split("|")[0])
    pprint.pprint(trials_matrix_means)
    
    return trials_matrix_means


def run_trials(board_name):
    # Runs a set number of trials on a given board, and appends the data to results_all_boards.json
    independent_trials = {}
    trials_matrix = {}

    print(f"\nNumber of trials: {NUM_TRIALS}.   Number of rolls per trial: {NUM_ROLLS}\n")

    for i in range(NUM_TRIALS):
        if i % (NUM_TRIALS/STATUS_CHECK_FREQUENCY) == 0: 
            if (PRINT_PERCENT):
                percent_str = str(round(i/NUM_TRIALS*100)) + "% complete..."
                print(percent_str)
            else:
                print(".",end="", flush=True)

        new_trial = simulate_dice(board_name)
        for key, value in new_trial.items():
            if value == 0:
                continue # skip zero resources
            ind_key = str(key)+" -- Trial "+str(i+1)
            independent_trials[ind_key] = value

            if key in trials_matrix:
                trials_matrix[key].append(value)
            else:
                trials_matrix[key] = []
                trials_matrix[key].append(value)

    print("100%% complete!\n\n")

    # process_ind_trials_dict(independent_trials)
    trials_means = process_ind_trials_matrix(trials_matrix, board_name)

    write_board_results(board_name, trials_means)
    return


def write_board_results(board_name, trials_means):
    # pprint.pprint(trials_means)

    filename = DICE_RESULTS_FILE

    # First, read the JSON file to a Python Dict
    with open(filename, 'r') as file:
        old_means_dict = json.load(file)

    # Second, update the dictionary from the file with this new means calculated
    old_means_dict[board_name] = trials_means

    # Third, overwrite the file
    try:
        with open(filename, 'w') as f:
            json.dump(old_means_dict, f, indent=4)  # indent for pretty-printing
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
    except TypeError as e:
        print(f"Error serializing data: {e}. Ensure all data types are JSON-serializable.")
    return


def generate_table_of_tiles(board_names):
    # Takes the dictionaries of tiles from and makes a markdown equivalent
    # print_str = "| <BLANK> | Board A | Board B | Board C |\n| ------- | ------- | ------- |\n"
    print_str = "|   "
    print_str_2 = "|\n| ------- |"
    print_str_2_part = " ------- |"

    file_name = "dice_boards.json"
    try:
        with open(file_name, 'r') as file:
            boards_json = json.load(file)

            # First, add the Board Names to the print string
            for key in board_names:
                print_str = print_str + "| " + key.replace("Board","") + " "
                print_str_2 = print_str_2 + print_str_2_part
            print_str = print_str + print_str_2 + "\n"
            
            # Second, iterate a row counter while running through the lists
            for i in range(16):
                print_str = print_str + "| Tile " + str(i+1) + " | "
                for key in board_names:
                    tile_list = boards_json[key]
                    tile = tile_list[i]
                    print_str = print_str +str(tile)+ " | "
                print_str = print_str + "\n"

            # Third, iterate a row counter while running through the mystery lists
            for j in range(4):
                print_str = print_str + "| Mystery " + str(j+1) + " | "
                for key in board_names:
                    mystery_name = key + "_Mystery"
                    mystery_list = boards_json[mystery_name]
                    mystery_index = "Reward"+str(j+1)
                    tile = mystery_list[mystery_index][0].replace("chance","")
                    tile = tile + ": " + mystery_list[mystery_index][1]

                    print_str = print_str + "<sub>" + str(tile)+ "</sub> | "
                print_str = print_str + "\n"

        print(print_str)

    except FileNotFoundError:
        print("Error: The file 'dice_boards.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file. Check for malformed JSON.")

    return


def build_print_string_for_table(board_names):
    # Set up the header row 
    print_str = "| Resource | "
    for board_name in board_names:
        print_str = print_str+board_name+" | "
    print_str = print_str +  "\n| ------- |"
    # and the dashes just below it
    for _ in board_names:
        print_str = print_str+" ------- |"
    print_str = print_str +  "\n"

    filename = DICE_RESULTS_FILE
    # First, read the JSON file to a Python Dict
    with open(filename, 'r') as file:
        means_dict = json.load(file)
        
    # Run through the full resource dictionary and add resources per board
    for resource_name in ALL_RESOURCE_LIST:
        print("\n\n")

        print_str = print_str + "| "+resource_name+" | "
        resource_line = ""
        for board_name in board_names:
            if resource_name in means_dict[board_name]:
                resource_mean_for_board = means_dict[board_name][resource_name]
                print(f"Resource Mean for {resource_name} board {board_name} is {resource_mean_for_board}")
            else:
                resource_mean_for_board = 0
            resource_line = resource_line+str(resource_mean_for_board)+" | "
        print_str = print_str + resource_line
        print_str = print_str + "\n"
    
    return print_str
    

def generate_tables_of_results():
    # Takes the dictionaries of resources from results_all_boards.json and makes a markdown equivalent
    # NOTE: This makes two tables. One for Free Boards, and one for Premium Boards.

    free_table = build_print_string_for_table(BOARD_NAMES[:4])
    premium_table = build_print_string_for_table(BOARD_NAMES[4:])

    free_table_str = "### Free Table\n\n\n" + free_table +"\n\n\n\n"
    premium_table_str = "### Premium Table\n\n\n" + premium_table + "\n\n"
    print_str = free_table_str + premium_table_str
    print(print_str)

    try:
        file_name = "resources_by_board.txt"
        with open(file_name, 'w') as file_object:
            file_object.write(print_str)
        print(f"Content successfully written to '{file_name}'")
    except IOError as e:
        print(f"Error writing to file: {e}")
    
    return


def print_tables():
    print("\n\n\nGenerating a table of all board tiles...\n\n")
    
    print("## Free Board Tables\n\n")
    generate_table_of_tiles(BOARD_NAMES[:4])
    print("\n\n\n")
    print("## Premium Board Tables\n\n")
    generate_table_of_tiles(BOARD_NAMES[4:])
    print("\n")


def all_boards_trials():
    for board in BOARD_NAMES:
        run_trials(board)

    generate_tables_of_results()
    return


def main():
    start_time = time.time()  

    # run_trials() # run on one board
    all_boards_trials() # run on all boards
    # print_tables()
    
    end_time = time.time() 
    elapsed_time = end_time - start_time
    print(f"\nElapsed time: {elapsed_time:.4f} seconds")
    return


if __name__ == "__main__":
    main()
