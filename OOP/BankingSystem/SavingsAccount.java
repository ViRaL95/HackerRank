public class SavingsAccount extends Account{
    int number_of_withdrawals ;

    public SavingsAccount(Long account_no, int pin_no, User user){
        super(account_no, pin_no, user);
        number_of_withdrawals = 0;
    }

    public void withdraw_money_from_savings(double withdrawal_amount) throws TooManyWithdrawals, OverDraftFee{
        this.number_of_withdrawals ++;
        if (number_of_withdrawals >= 6){
            throw new TooManyWithdrawals("You have tried to withdraw from your " +
                    "Savings Account too many times");
        }
        super.withdraw_money(withdrawal_amount);
    }

}
