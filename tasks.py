# =====================================
# CASE FILE 09 - INVESTIGATION TASKS
# =====================================

tasks = {

    "1": [
        {
            "name": "Investigate financial records",
            "question": "Which transaction is suspicious?",
            "options": [
                "A. RM500 - Office supplies",
                "B. RM25,000 - Unknown recipient",
                "C. RM300 - Staff meals"
            ],
            "answer": "B",
            "evidence": "Suspicious bank transaction"
        },

        {
            "name": "Search Richard's office",
            "question": "Which document should be investigated?",
            "options": [
                "A. Financial report",
                "B. Lunch menu",
                "C. Music playlist"
            ],
            "answer": "A",
            "evidence": "Missing financial document"
        },

        {
            "name": "Check Richard's alibi",
            "question": "Richard says he left at 9 PM. CCTV shows him at 9:45 PM. What is the contradiction?",
            "options": [
                "A. He left early",
                "B. He was still inside at 9:45 PM",
                "C. CCTV was recorded in the morning"
            ],
            "answer": "B",
            "evidence": "Richard's inconsistent alibi"
        }
    ],


    "2": [
        {
            "name": "Investigate email records",
            "question": "Which email looks suspicious?",
            "options": [
                "A. Weekly Meeting",
                "B. Delete the appointment records",
                "C. Office Lunch"
            ],
            "answer": "B",
            "evidence": "Deleted email correspondence"
        },

        {
            "name": "Search Evelyn's desk",
            "question": "A note shows 10:15 PM, but the meeting was scheduled for 9:30 PM. What should you investigate?",
            "options": [
                "A. The time difference",
                "B. Office furniture",
                "C. Lunch menu"
            ],
            "answer": "A",
            "evidence": "Suspicious appointment note"
        },

        {
            "name": "Interview Evelyn",
            "question": "Evelyn says she went home at 9 PM. What is the best question?",
            "options": [
                "A. What did you eat?",
                "B. Can anyone confirm when you left?",
                "C. Do you like your job?"
            ],
            "answer": "B",
            "evidence": "Evelyn's inconsistent statement"
        }
    ],


    "3": [
        {
            "name": "Check access card logs",
            "question": "Who entered the office at 10:05 PM?",
            "options": [
                "A. Richard Cole",
                "B. Evelyn Hart",
                "C. Thomas Reed"
            ],
            "answer": "C",
            "evidence": "Thomas entered the office at 10:05 PM"
        },

        {
            "name": "Search confidential documents",
            "question": "Decode this clue: T H O M A S. Who is mentioned?",
            "options": [
                "A. Richard",
                "B. Evelyn",
                "C. Thomas"
            ],
            "answer": "C",
            "evidence": "Thomas's confidential report"
        },

        {
            "name": "Verify Thomas's alibi",
            "question": "Thomas claims he was outside at 10 PM. His access card shows entry at 10:05 PM. What does this suggest?",
            "options": [
                "A. His statement may be inconsistent",
                "B. He was at home",
                "C. His card was never used"
            ],
            "answer": "A",
            "evidence": "Thomas's inconsistent alibi"
        }
    ]
}


# =====================================
# MINI-GAME FUNCTION
# =====================================

def play_task(task):

    print("\n========== MINI GAME ==========")

    print("\nTASK:", task["name"])

    print("\n" + task["question"])

    for option in task["options"]:
        print(option)

    answer = input("\nYour answer (A/B/C): ").strip().upper()

    if answer == task["answer"]:

        print("\nCorrect answer!")
        print("Evidence successfully discovered.")

        return True

    else:

        print("\nWrong answer!")
        print("Try again, Detective.")

        return False
    