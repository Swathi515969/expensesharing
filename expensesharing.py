import pandas as pd
import numpy as np

class Expensesharing:
    def __init__(self,friends):
        self.friends=friends
        self.balances={friend:0 for friend in friends}
        self.history=[]

    def add_expense(self,payer,amount,participants):
        split_amount = amount/len(participants)

        self.history.append({
            "payer":payer,
            "amount":amount,
            "participants_count":len(participants)
        })

        for participant in participants:
            self.balances[participant] -= split_amount
        self.balances[payer] += amount

    def show_analytics(self):
        df=pd.DataFrame(self.history)
        print("Dataset")
        print(df)
        print(f"\nTotal spent : Rs.{np.sum(df['amount'])}")
        print(f"Average expense: Rs.{np.mean(df['amount']):.2f}")
        print(f"Max expense:Rs.{np.max(df['amount'])}")
        print("\n who paid how much:")
        print(df.groupby('payer')['amount'].sum())

    def calculate_settlement(self):
        creditors = []
        debtors = []
        for friend, balance in self.balances.items():
            if balance >0:
                creditors.append((friend,balance))
            elif balance <0:
                debtors.append((friend,-balance))
        print("\n final settlement")
        while debtors and creditors:
            debtor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()
            payment = min(debt_amount,credit_amount)
            print(f"{debtor} owes {creditor}:Rs.{payment:.2f}")

            if debt_amount > payment:
                debtors.append((debtor, debt_amount - payment))
            if credit_amount > payment:
                creditors.append((creditor,credit_amount-payment))

   
friends = ["Arul","Jyo","Kavin"]
Expense_sharing= Expensesharing(friends)

Expense_sharing.add_expense("Arul",1900,["Arul","Jyo","Kavin"])# paid for accomodation
Expense_sharing.add_expense("Jyo",900,["Arul","Jyo","Kavin"])# paid for meals
Expense_sharing.add_expense("Kavin",300,["Arul","Kavin"])# paid for fuel-uneven case

Expense_sharing.show_analytics()
Expense_sharing.calculate_settlement()
        
    
friends = input("Enter the names of friends, separated by commas:").split(",")
friends = [friend.strip()for friend in friends]
expense_sharing = Expensesharing(friends)

while True:
    payer = input("Enter the name of the person who paid (of 'done' to finish):")
    if payer.lower()=="done":
        break
    amount = float(input("Enter the amount paid:"))
    participants = input("Enter the names of participants for this expense:").split(",")
    participants = [participant.strip() for participant in participants]
    expense_sharing.add_expense(payer,amount,participants)
expense_sharing.calculate_settlement()


