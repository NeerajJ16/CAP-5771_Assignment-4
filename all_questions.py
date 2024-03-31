# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Some instances can trigger more than one rule, for example a person could be a home owner and have a low annual income, hence they are not mutually exclusive."
    answers["(b) explain"] = "The rule set is non-exhaustive, missing coverage for certain combinations like high income and employment status."
    answers["(c) explain"] = "Rule ordering is critical as it influences classification outcomes, especially in cases of overlapping rules, such as when being a homeowner and single could trigger multiple rules."
    answers["(d) explain"] = "A default class ensures that every instance can be classified even if it does not meet any of the specific rule's requirements."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Each rule applies to a specific set of characteristics that do not overlap with the others, rendering them mutually exclusive."
    answers["(b) example"] = "The rules do not address all possible combinations, such as animals that give birth but are not warm-blooded, indicating that they are not exhaustive."
    answers["(c) example"] = "Because the rules are mutually exclusive and do not overlap, applying them in any order has no effect on the outcome, so ordering is unnecessary."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Gradients are propagated backward from the output to input layer, making computations dependent on subsequent layers."
    answers["(b) explain"] = "Activations of nodes in any layer depend on the activations of the preceding layer, following the feedforward process."
    answers["(c) explain"] = "The vanishing gradient problem refers to gradients becoming smaller as error is backpropagated, not to the discrepancy between training and test errors."
    answers["(d) explain"] = "Perfect classification does not imply gradients are 0; it indicates no error in classification but not necessarily the global minimum of the loss function."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}
    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28
    
    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"
    
    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "no"
    
    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16
    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"
    # float between 0 and 1
    answers["(d) Training error rate"] = 0.3
    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Assuming the classes are well separated, a smaller K=1 is chosen to minimize bias while closely following the class boundaries."
    answers["(b) explain"] = "K=5 provides a balance that reduces variance without noticeably raising bias, making it appropriate for datasets with some degree of overlap or noise."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # Conditional probabilities calculated from the dataset
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # Explanation for conditional probabilities
    answers["(a) P(A=1|+) explain your answer"] = "Calculated by dividing the number of positive instances where the feature is 1 by the total number of positive instances."
  
    # Probabilities for the sample R = (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857  
    answers["(b) P(R|+)"] = 0.12
    answers["(b) P(R|-)"] = 0.02

    # Predicted class label for the sample
    answers["(b) class label"] = "+"

    # Explanation for the prediction
    answers["(b) Explain your reasoning"] = "The class label '+' has a higher posterior probability for the sample than the class label '-'."
  
    # Marginal and joint probabilities for independence check
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # Checking independence between A and B
    answers["(c) A independent of B?"] = "yes"
  
    # For part (d), repeating the analysis with B=0
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6  
    answers["(d) P(A=1,B=0)"] = 0.55

    # Checking independence for part (d)
    answers["(d) A independent of B?"] = "yes"
  
    # Conditional independence given class "+"
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.5

    # Checking conditional independence given class "+"
    answers["(e) A independent of B given class +?"] = "yes"

    # Explanation for conditional independence
    answers["(e) A and B conditionally independent given class +, explain"] = "Naive Bayes assumes features are conditionally independent given the class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
