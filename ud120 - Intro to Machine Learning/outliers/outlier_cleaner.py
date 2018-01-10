#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for age, net_worth, pred in zip(ages, net_worths, predictions):
        cleaned_data.append((age, net_worth, (pred - net_worth)**2))
    cleaned_data.sort(key=lambda x:x[2])
    
    return cleaned_data[:len(cleaned_data)*9/10]

