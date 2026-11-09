# =====================================
# CASE FILE 09 - FINAL ACCUSATION
# =====================================

killer = "3"


def final_accusation(suspects, evidence_count):

    print("\n========== FINAL ACCUSATION ==========")

    if evidence_count < 3:

        print("\nInsufficient evidence!")

        print("You need at least 3 pieces of evidence.")

        print("Current evidence:", evidence_count)

        return

    print("\nWho is the murderer?")

    for number, suspect in suspects.items():

        print(f"{number}. {suspect['name']}")

    choice = input("\nEnter your accusation (1-3): ").strip()

    if choice not in suspects:

        print("\nInvalid selection.")

        return

    if choice == killer:

        print("\n" + "=" * 40)

        print("          CASE SOLVED!")

        print("=" * 40)

        print("\nThe murderer is Thomas Reed.")

        print("Congratulations, Detective!")

    else:

        print("\nWrong accusation!")

        print("The case remains unresolved.")
        