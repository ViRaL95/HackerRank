public class CheckingAccount extends Account{

    public CheckingAccount(Long account_no, int pin_no, User user){
        super(account_no, pin_no, user);
    }

    public void withdraw_money(double amount) throws OverDraftFee{
        super.withdraw_money(amount);
        double minimum_balance = super.getMinimumBalance();
        double account_amount = super.getAmount();
        if (account_amount < minimum_balance){
            throw new OverDraftFee("Your balance goes below minimum balance ");
        }
    }
}
