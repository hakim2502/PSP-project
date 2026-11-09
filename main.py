
# CASE FILE 09 - MAIN PROGRAM


from suspects import suspects, show_suspects

from tasks import tasks, play_task

from evidence import (
    collect_evidence,
    view_evidence,
    get_evidence_count
)

from accusation import final_accusation


# TRACK COMPLETED TASKS

completed_tasks = {
    "1": [],
    "2": [],
    "3": []
}


# =====================================
# GAME INTRODUCTION
# =====================================

def introduction():

    print("\n" + "=" * 45)

    print("             CASE FILE 09")

    print("         THE LAST APPOINTMENT")

    print("=" * 45)

    print("\nA murder has occurred at Whitmore Industries.")

    print("Victim: Daniel Whitmore (CEO)")

    print("Time of death: 10:15 PM")

    print("\nYour mission is to investigate the case,")

    print("collect evidence and identify the murderer.")

    print("\nGood luck, Detective!")


# =====================================
# INVESTIGATION SYSTEM
# =====================================

def investigate_suspect():

    show_suspects()

    choice = input("\nChoose a suspect (1-3): ").strip()

    if choice not in suspects:

        print("\nInvalid suspect selection.")

        return

    suspect_name = suspects[choice]["name"]

    while True:

        print("\n========== INVESTIGATION TASKS ==========")

        for number, task in enumerate(tasks[choice], start=1):

            if number in completed_tasks[choice]:

                status = "COMPLETED"

            else:

                status = "NOT COMPLETED"

            print(f"{number}. {task['name']} [{status}]")

        print("0. Return to Main Menu")

        task_choice = input("\nChoose a task (0-3): ").strip()

        if task_choice == "0":

            break

        if task_choice not in ["1", "2", "3"]:

            print("\nInvalid task selection.")

            continue

        task_number = int(task_choice)

        if task_number in completed_tasks[choice]:

            print("\nYou already completed this task.")

            continue

        selected_task = tasks[choice][task_number - 1]

        success = play_task(selected_task)

        if success:

            completed_tasks[choice].append(task_number)

            collect_evidence(
                suspect_name,
                selected_task["evidence"]
            )


# =====================================
# MAIN MENU
# =====================================

def main():

    introduction()

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Investigate Suspects")

        print("2. View Collected Evidence")

        print("3. Make Final Accusation")

        print("4. Exit Game")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":

            investigate_suspect()

        elif choice == "2":

            view_evidence()

        elif choice == "3":

            final_accusation(
                suspects,
                get_evidence_count()
            )

        elif choice == "4":

            print("\nThank you for playing!")

            print("Case File 09 - Investigation Closed.")

            break

        else:

            print("\nInvalid choice. Please try again.")


# =====================================
# START GAME
# =====================================

if __name__ == "__main__":

    main()
    
