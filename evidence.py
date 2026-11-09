# =====================================
# CASE FILE 09 - EVIDENCE MANAGEMENT
# =====================================

evidence = []


def collect_evidence(suspect_name, evidence_name):

    evidence.append({
        "suspect": suspect_name,
        "evidence": evidence_name
    })

    print("\n========== EVIDENCE COLLECTED ==========")

    print("Suspect:", suspect_name)
    print("Evidence:", evidence_name)


def view_evidence():

    print("\n========== COLLECTED EVIDENCE ==========")

    if len(evidence) == 0:

        print("No evidence collected yet.")

    else:

        for number, item in enumerate(evidence, start=1):

            print(f"\n{number}. {item['evidence']}")
            print("   Related suspect:", item["suspect"])

    print("\nTotal evidence:", len(evidence))


def get_evidence_count():

    return len(evidence)
