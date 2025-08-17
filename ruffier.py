

# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''there is no data for that age'''

txt_res = []
txt_res.append('''low. Go see your doctor ASAP!''')
txt_res.append('''satisfactory. Go see your doctor!''')
txt_res.append('''average. It might be worth additional tests at the doctor.''')
txt_res.append('''higher than average''')
txt_res.append('''high''')

# Calculation:  https://docs.google.com/presentation/d/1sMfJFMMEFs-KGf1Zen3aRXihxcWQP54aP6_lbbkqjJ8/edit#slide=id.p7
def ruffier_index(P1, P2, P3):
    '''it returns the index value according to the three pulse calculations for comparison with the table'''
    return (4 * (P1+P2+P3) - 200) / 10


def neud_level(age):
    ''' the options with an age of less than 7 and with adults have to be processed separately,
    here we select the level “unsatisfactory” only within the table:
    for the age of 7, “unsatisfactory” is an index of 21, then onwards 
    every 2 years it decreases by 1.5 until the level of 15 at age 15–16 '''

    # every two years the from age seven turns into one unit, all the way to age 15
    norm_age = (min(age, 15) - 7) // 2  

    # every two years multiply the difference by 1.5, that's how the levels are arranged in the table
    result = 21 - norm_age * 1.5 

    return result

def ruffier_result(r_index, level):
    ''' the function obtains a Ruffier index and interprets it,
    we return the readiness level: a number from 0 to 4
    (the higher the readiness level, the better).  '''

    if r_index >= level:
        return 0
    level = level - 4 # this will not run if we already returned the answer “unsatisfactory”
    if r_index >= level:
        return 1
    level = level - 5 # analogously, we end up here if the level is, at minimum, “satisfactory”
    if r_index >= level:
        return 2
    level = level - 5.5 # next level
    if r_index >= level:
        return 3
    
    return 4 # we end up here if the index is less than all the intermediate levels, that is, the tested circle.


def test(P1, P2, P3, age):
    ''' this function can be used from outside the module for calculating the Ruffier index.
    We return the ready texts that just need to be written in the necessary place
    We use the constants used at the beginning of this module for texts. '''

    if age < 7:
        # this is a mystery beyond this test
        return (txt_index + "0", txt_nodata) 
    
    else:
        ruff_index = ruffier_index(P1, P2, P3) # calculation

        # the interpretation and conversion of the numeric preparation level into text data
        result = txt_res[ruffier_result(ruff_index, neud_level(age))] 
        
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        
        return res

