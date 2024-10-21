# rule_engine_ast_py
summary: Its demonstrates a simple rule engine system that evaluates user eligibility based on a set of dynamic rules.The system is built using three layers
there are Data layer , Rule layer , and Service layer.The rules are safely evaluated using PYTHON ABSTRACT SYNTAX TREES(AST) allowing the system to process
rules written as strings..


It Consists of 3 layers:   1)Data Layer (User Class)
                           2)Rule Layer (Rule Engine Class)
                           3)Service Layer ( Eligibility Service)

                           
* AST safe evaluation (safe eval class)

  
1)Data Layer : Its stores user information.
  * __init__ : Initializes user attributes(age,department,income,spend)
  * to _dict : Convert user data to a dictonary.
    
2)Rule Layer : This rules are combined using logical operator(and)
  * Manages rules using AST
  * add_rule : add rules("age>18")
  * combine_rules : combine rules with "and" "or"
  * evaluate_rules : evaluate combined rules against user code.
    
3)Service Layer : This layer ties the user data & the rule engine together
 * The check_eligibility method first converts the user data to a dictonary & then uses the rule engine to evaluate weather the user satisfies the combined rules.
Additional Component :  Safe eval : AST  node visitors for safe rule evaluation...


Work Flow :
* Create a rule engine instance.
* Define rules(age,dept,income,spend).
* Create an eligibility service instance with rule engine.
* Create an user instance with this code.
* Check eligibility for each user using eligibility service...

The provided code implements a basic three-tier rule engine system using Python's Abstract Syntax Tree (AST) for safe evaluation of rules. Here's the output:


User 1 eligibility: True
User 2 eligibility: False


Explanation:

1. User 1 Eligibility: True

    - Age: 25 (meets "age > 18" rule)
    - Department: IT (meets "department == 'IT'" rule)
    - Income: 60,000 (meets "income > 50,000" rule)
    - Spend: 1,500 (meets "spend < 2,000" rule)
All conditions are met; hence, User 1 is eligible.
2. User 2 Eligibility: False

    - Age: 17 (fails "age > 18" rule)
    - Department: HR (fails "department == 'IT'" rule)
    - Income: 40,000 (fails "income > 50,000" rule)
    - Spend: 2,500 (fails "spend < 2,000" rule)
None of the conditions are met; hence, User 2 is not eligible.

The code effectively demonstrates how rules can be defined, combined and evaluated against user data using AST for secure evaluation......                           
