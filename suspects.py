# =====================================
# CASE FILE 09 - SUSPECT DATABASE
# =====================================

suspects = {
    "1": {
        "name": "Richard Cole",
        "position": "Business Partner",
        "motive": "Financial disputes with Daniel"
    },

    "2": {
        "name": "Evelyn Hart",
        "position": "Personal Assistant",
        "motive": "She knew Daniel's private schedule"
    },

    "3": {
        "name": "Thomas Reed",
        "position": "Senior Manager",
        "motive": "He wanted to hide company secrets"
    }
}


def show_suspects():

    print("\n========== THE SUSPECTS ==========")

    for number, suspect in suspects.items():

        print(f"\n{number}. {suspect['name']}")
        print(f"   Position: {suspect['position']}")
        print(f"   Motive: {suspect['motive']}")
        