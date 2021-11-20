Instructions:

1.Clone the whole folder 'game1' to your local computer.

2.Open your terminal, type 'pip install PyQt5'.

3. Please use pycharm to open the whole folder 'game1'.

4. Read the instructions on the top input box in the interface or watch the video named 'game_demo' to see how it works.

# If this still does not work, please contact me via email, so I could share an exe file with you, which could not be uploaded to Git due to its size.


Contents about the project:

The game consists of 10 heros that will form 2 groups, with team one (hero1-5) and team two (hero6-10). By running the 'main.py', you will first see the roles that are assigned to each group member randomly with the adjusted attributes. Then the members from two teams will attact each other, which could be seen by clicking on each hero's profile. As the hero being attacked and the skill (with different damages) selected are random choices, so after each attack the one who is attacked loses different amount of blood. Once a hero dies, his profile changes to another picture and he can not take any further actions. Once all members of a team are killed and game over.

The game demo was created with Python programming language and an interface called PyQt5.

The file named 'main.py' is the main part for the frontend codes of the output interface, which was generated from PyQt5 and adjusted according to the backend codes..

The file 'character_game.py' presents the main part of the class 'characters' including its initial attributes and the functions to adjust attributes of hero after being assigned with a role.

The file 'process_game.py' presents all the main actions and interactions the characters would take eg. randomly assigning roles and selecting a specific skill to attack others.


