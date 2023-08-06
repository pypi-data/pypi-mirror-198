from CASpy_ReactionEquilibria import caspy

def test_results_for_A_B_case():
    """This function tests the results for a basic test case
    mu^0 and mu^ex of A and B = 0.0
    Initial conditions = 20 and 5 mol/dm3 for A and B, respectively
    Reaction --> A <--> B
    lnK for the reaction = 0.0"""
    caspy.main("tests/basic_test_A_B.txt")
    with open("caspy_output.log", 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in data:
            if "Solution =" in i:
                solution = i
    assert float(solution.split()[3]) == 15, 'Test for the basic case failed!'

