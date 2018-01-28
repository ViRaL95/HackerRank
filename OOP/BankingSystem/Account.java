public abstract class Account {
    private double minimum_balance;
    private double amount;
    private Long account_no;
    private int pin_no;
    private User user;

    public User getUser() {
        return user;
    }

    public Account(Long account_no, int pin_no, User user){
        this.account_no = account_no;
        this.pin_no = pin_no;
        minimum_balance = 0;
        amount= 0;
        this.user = user;
    }

    public void withdraw_money(double amount) throws  OverDraftFee{
        this.amount -= amount;
        if (this.amount < minimum_balance) {
            throw new OverDraftFee("You have dropped below your minmium balance");
        }
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void transfer_money(Account account, double amount){
        this.amount -= amount;
        account.deposit_money(amount);
    }

    public double getAmount() {
        return amount;
    }

    public double getMinimumBalance(){
        return this.minimum_balance;
    }

    public void deposit_money(double amount){
        this.amount += amount;
    }

    public Long getAccount_no() {
        return account_no;
    }

    public int getPin_no() {
        return pin_no;
    }

    public void close_account() throws ExistingMoneyInAccount, InsufficientFunds{
        if (amount > 0){
            throw new ExistingMoneyInAccount("Inorder to close an account one " +
                    "must transfer their money to another account");
        }

        if (amount < 0){
            throw new InsufficientFunds("In order to close this account you can not have ");
        }
    }
}
