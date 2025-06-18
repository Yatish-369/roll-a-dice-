import random
import mysql.connector
from datetime import datetime

# MySQL configuration (You can load from .env or config file in real applications)
DB_CONFIG = {
    "host": "localhost",
    "user": "yourUsername",      # Replace with your MySQL username
    "passwd": "yourPassword",    # Replace with your MySQL password
    "database": "databaseName"   # Replace with your database name
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✅ Database connection successful.")
        return connection
    except mysql.connector.Error as err:
        print("❌ Error: Could not connect to the database.")
        print("Details:", err)
        exit()

def get_user_choice():
    try:
        return int(input("Choose any one (1 to play, 2 to exit): "))
    except ValueError:
        print("❌ Invalid input. Please enter 1 or 2.")
        return get_user_choice()

def roll_dice_task():
    dice_value = random.randint(1, 6)
    print(f"🎲 You rolled a {dice_value}!")
    answer = ""

    if dice_value == 1:
        print("Task: Name your favourite movie.")
        answer = input("Your answer: ")
        print("Woaah! Cool")

    elif dice_value == 2:
        print("Task: What would you prefer, Mountains or Beach?")
        answer = input("Your answer: ")
        print("Nice choice!")

    elif dice_value == 3:
        print("Task: Name 3 of your favourite Indian foods.")
        answer = input("Your answer: ")
        print(random.choice(["Sounds Delicious", "Yummy", "Tasty", "I got watery mouth 🍉"]))

    elif dice_value == 4:
        print("Task: Joe is 40. His brother John is half his age when Joe was 6. How old is John now?")
        try:
            answer_input = int(input("Your answer: "))
            answer = str(answer_input)
            if answer_input == 37:
                print("✅ Viola! You are right.")
            else:
                print("❌ Oops! The correct answer is 37.")
        except ValueError:
            answer = "Invalid number"
            print("❌ Please enter a valid number.")

    elif dice_value == 5:
        print("Task: What has two banks but no money? 🤔")
        answer = input("Your answer: ")
        if answer.lower() == "river bank":
            print("✅ Viola! You are right.")
        else:
            print("❌ Oops! The correct answer is 'River bank'.")

    elif dice_value == 6:
        print("Task: Name any 6 continents of the world.")
        continents = []
        for i in range(6):
            continent = input(f"Enter continent {i+1}: ")
            continents.append(continent)
        answer = ", ".join(continents)
        print("You entered:", answer)

    return dice_value, answer

def save_to_database(name, dice_value, answer, connection):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO tableName (name, dice_value, answer, time_played) VALUES (%s, %s, %s, %s)"
        data = (name, dice_value, answer, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(query, data)
        connection.commit()
        print("✅ Your response has been recorded!")
    except mysql.connector.Error as err:
        print("❌ Failed to insert data into the database.")
        print("Details:", err)

def main():
    print("🎲 Welcome to the Roll A Dice Game!")
    name = input("Your name: ")
    print(f"Hey {name}, welcome! Let's play! 🥳\n")

    print("""Rules: 
1. Roll a dice to get a random task. 
2. Perform the task and enjoy. 
3. Your answer will be recorded.
4. Let's have fun!
""")

    choice = get_user_choice()
    if choice == 1:
        dice_value, answer = roll_dice_task()
        connection = connect_to_db()
        save_to_database(name, dice_value, answer, connection)
        connection.close()
        print("👋 Have a great day, see you soon!")
    else:
        print("👋 Sayonara! Come back to play again.")
        exit()

if __name__ == "__main__":
    main()
