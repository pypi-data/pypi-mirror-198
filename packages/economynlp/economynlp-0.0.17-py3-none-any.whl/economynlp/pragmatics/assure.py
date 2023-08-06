def assure_decorator(speaker):
    """
    ### Example:
    ```
    @assure_decorator("John")
    def get_loan_approval(name, income):
        if income >= 50000:
            return f"{name}, congratulations! Your loan application has been approved."
        else:
            return f"Sorry, {name}. Your income of {income} is not sufficient for the loan."
            
    # Call the decorated function with name and income parameters
    result = get_loan_approval("Mary", 60000)
    print(result)
    ```
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"{speaker} assures you that {result}"
        return wrapper
    return decorator
