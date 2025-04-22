# define a function to calculate the recommended dosage of a drug for children 
# based on their weight and the drug concentration:
def drug_dosage_calculator(children_weight, drug_concentration):
    # check if the weight is within the valid range
    if children_weight < 10 or children_weight > 100:
        return "Please enter a valid weight between 10 and 100"
    elif drug_concentration not in [120, 250]:
        return "Please enter a valid drug concentration of 120 or 250"
    else:
        # calculate the recommended dosage based on the formula
        mass = 15*children_weight
        volume = mass / drug_concentration *5
        return f"Recommended dosage for children of weight {children_weight} kg is {volume} ml"

# test the function with some sample inputs
print(drug_dosage_calculator(130,120))
print(drug_dosage_calculator(50,100))
print(drug_dosage_calculator(60,250))