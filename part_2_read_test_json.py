import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):

    game_library = test_data.GameLibrary()




    ### Begin Add Code Here ###
    #Loop through the json_data
    json_library = json_data["GameLibrary"];
    for game in json_library:
        new_platform = test_data.Platform(game["Platform"]["name"], game["Platform"]["launch_year"]);
        new_game = test_data.Game(game["title"], new_platform, game["Year"]);
        game_library.add_game(new_game);



        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
#load the JSON data and store it in the variable family_json_data
    json_data = json.load(reader)
#Use the json module to load the data from the file
print(make_game_library_from_json(json_data));

#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
