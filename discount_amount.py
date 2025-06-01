'''
Consider this scenario:

You run a store where customers get a 10% discount on the portion of their purchase above $100.

For example, if the total amount is $150, they get a 10% discount on $50, saving $5. The final amount to pay is $145.

To solve this problem:

1. Input the total amount: Ask the user for the purchase total.
2. Check the condition: If the total is greater than $100, calculate a 10% discount on the amount exceeding $100.
3. Update and display: Subtract the discount and display the final amount.
'''
total_amount = int(input("Enter your purchase:"))
discount = 10
if total_amount > 100:
    exceed_amount = total_amount - 100
    print(f"Your exceed amount is {exceed_amount}")
    final_discount = (discount / 100) * exceed_amount
    final_amount = total_amount - final_discount
    print(f"final_amount is {final_amount}")
