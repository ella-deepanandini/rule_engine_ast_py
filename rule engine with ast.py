import ast

# Data Layer - Holds user data
class User:
    def __init__(self, age, department, income, spend):
        self.age = age
        self.department = department
        self.income = income
        self.spend = spend

    def to_dict(self):
        return {
            "age": self.age,
            "department": self.department,
            "income": self.income,
            "spend": self.spend,
        }


# Rule Layer - Manages rule creation and evaluation using AST
class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule_string):
        """Adds a new rule to the rule engine."""
        self.rules.append(rule_string)

    def combine_rules(self, operator="and"):
        """Combines all rules into a single rule."""
        if not self.rules:
            raise ValueError("No rules to combine.")
        
        combined_rule = f" {operator} ".join([f"({rule})" for rule in self.rules])
        return combined_rule

    def evaluate_rule(self, combined_rule, context):
        """Evaluates the combined rule against the user context using AST."""
        try:
            # Parse the rule into an AST
            tree = ast.parse(combined_rule, mode='eval')
            evaluator = SafeEval(context)
            # Evaluate the parsed tree
            return evaluator.visit(tree.body)
        except Exception as e:
            print(f"Error evaluating rule: {e}")
            return False


# Service Layer - Ties the data and rules together
class EligibilityService:
    def __init__(self, rule_engine):
        self.rule_engine = rule_engine

    def check_eligibility(self, user):
        """Determines if a user is eligible based on the defined rules."""
        context = user.to_dict()
        combined_rule = self.rule_engine.combine_rules()
        result = self.rule_engine.evaluate_rule(combined_rule, context)
        return result


# AST Node Visitor for safe evaluation of rules
class SafeEval(ast.NodeVisitor):
    def __init__(self, context):
        self.context = context
    
    def visit_Name(self, node):
        # If the variable is in the context, return its value
        if node.id in self.context:
            return self.context[node.id]
        raise NameError(f"Undefined variable: {node.id}")
    
    def visit_Constant(self, node):
        # Return constant values like numbers or strings directly
        return node.value
    
    def visit_Compare(self, node):
        left = self.visit(node.left)
        for op, comparator in zip(node.ops, node.comparators):
            right = self.visit(comparator)
            if isinstance(op, ast.Gt):
                return left > right
            elif isinstance(op, ast.Lt):
                return left < right
            elif isinstance(op, ast.Eq):
                return left == right
            elif isinstance(op, ast.NotEq):
                return left != right
        return False
    
    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            return all(self.visit(value) for value in node.values)
        elif isinstance(node.op, ast.Or):
            return any(self.visit(value) for value in node.values)

    def visit_Expr(self, node):
        return self.visit(node.value)


# Test the 3-tier rule engine system
if __name__ == "__main__":
    # Create a rule engine instance
    rule_engine = RuleEngine()

    # Define some rules
    rule_engine.add_rule("age > 18")
    rule_engine.add_rule("department == 'IT'")
    rule_engine.add_rule("income > 50000")
    rule_engine.add_rule("spend < 2000")

    # Create a service instance
    eligibility_service = EligibilityService(rule_engine)

    # Create user data
    user1 = User(age=25, department="IT", income=60000, spend=1500)
    user2 = User(age=17, department="HR", income=40000, spend=2500)

    # Check eligibility for user1 and user2
    print(f"User 1 eligibility: {eligibility_service.check_eligibility(user1)}")  
    print(f"User 2 eligibility: {eligibility_service.check_eligibility(user2)}") 