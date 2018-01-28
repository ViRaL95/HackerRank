import javax.swing.plaf.synth.SynthDesktopIconUI;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

public class User {
    private String first_name;
    private String last_name;
    private int age;
    private Date date_user_joined;
    private HashMap <Long, Account> Accounts;
    private SavingsAccount savingsAccount;
    private HashMap <Long, Card> cards;
    private Account current_account;
    private Card current_card;

    public User(String first_name, String last_name, int age){
        this.first_name = first_name;
        this.last_name = last_name;
        this.age = age;
        this.date_user_joined = new Date();
        Accounts = new HashMap <Long, Account>();
        cards = new HashMap<Long, Card>();
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public Account get_account(Long account_no){
        return Accounts.get(account_no);
    }

    public DebitCard create_debit_card() throws WrongCardInfo, MustHaveACheckingAccount{
        if (current_account instanceof SavingsAccount){
            throw new WrongCardInfo("You can not create a debit card using a Savings Account. Switch to a Checkings Account ");
        }
        if (current_account == null){
            throw new MustHaveACheckingAccount("You must have a checking account in order to create a debit card");
        }
        Long card_no = create_card_number();
        DebitCard debitCard = new DebitCard(card_no, first_name, last_name);
        cards.put(card_no, debitCard);
        return debitCard;
    }

    public CreditCard create_credit_card() throws WrongCardInfo, MustHaveACheckingAccount{
        if (current_account instanceof SavingsAccount){
            throw new WrongCardInfo("You can not create a debit card using a Savings account. Switch to a checkings account");
        }
        if (current_account == null){
            throw new MustHaveACheckingAccount("You must have a checking account in order to create a credit card");
        }
        Long card_no = create_card_number();
        CreditCard creditCard = new CreditCard(card_no, first_name, last_name);
        cards.put(card_no, creditCard);
        return creditCard;
    }

    private Long create_account_number(){
        Long account_no = 100000000L + (long) (Math.random() * (900000000L - 100000000L));
        return account_no;
    }

    private Long create_card_number(){
        Long card_no = 1000000000000000L + (long) (Math.random() * (9000000000000000L - 1000000000000000L));
        return card_no;
    }

    public CheckingAccount create_checking_account(int pin_no){
        Long account_no = create_account_number();
        CheckingAccount checkingAccount = new CheckingAccount(account_no, pin_no, this);
        Accounts.put(account_no, checkingAccount);
        return checkingAccount;
    }

    public SavingsAccount create_saving_account(int pin_no) throws OnlyOneSavingsAccount{
        Long account_no = create_account_number();
        if (savingsAccount != null){
            throw new OnlyOneSavingsAccount("Only One Savings Account Is Allowed");
        }
        SavingsAccount savingsAccount = new SavingsAccount(account_no, pin_no, this);
        Accounts.put(account_no, savingsAccount);
        return savingsAccount;
    }

    public void set_current_account(long desired_account_no, int pin_no) throws WrongAccountInfo{
        for (Long account_no: Accounts.keySet()) {
            if (account_no == desired_account_no && Accounts.get(account_no).getPin_no() == pin_no) {
                current_account = Accounts.get(account_no);
                return;
            }
        }
        throw new WrongAccountInfo("Wrong account information entered");
    }

    public void set_current_card(long desired_card_no){
        for(Long card_no: cards.keySet()){
            if (card_no == desired_card_no){
                current_card = cards.get(card_no);
            }
        }
    }

    public void close_account(){
        try {
            current_account.close_account();
        }
        catch (ExistingMoneyInAccount | InsufficientFunds ex){
            System.out.println(ex.getMessage());
        }
    }

    public void deposit_money(double amount) throws WrongCardInfo{
        try{
            check_if_card_exists();
        }
        catch (MustChooseACard ex){
            System.out.println(ex.getMessage());
        }
        if (current_card == null){
            throw new WrongCardInfo("You can not deposit money into a credit card");
        }
        Receipt receipt = new Receipt(current_account);
        if (current_card instanceof DebitCard){
            ((DebitCard) current_card).deposit_money(current_account, amount);
            receipt.toString();
        }
    }

    public void clean_account() throws WrongCardInfo{
        try {
            check_if_card_exists();
        }
        catch (MustChooseACard ex){
            System.out.println(ex.getMessage());
            return;
        }
        if (current_card instanceof CreditCard){
            throw new WrongCardInfo("You can not remove money from a credit card");
        }
        if (current_card instanceof DebitCard){
            double amount = current_account.getAmount();
            Receipt receipt = new Receipt(current_account);
            receipt.toString();
        }
    }

    public void use_credit_card(long desired_card_no){
        for (long card_no: cards.keySet()){
            if (card_no == desired_card_no){
                current_card = cards.get(card_no);
            }
        }
    }

    public void check_if_card_exists() throws MustChooseACard{
        if (current_card == null){
            throw new MustChooseACard("You must choose a card");
        }
    }

    public void transfer_money_from_accounts(Long account_no, double amount) throws WrongCardInfo{
        try {
            check_if_card_exists();
        }
        catch(MustChooseACard ex){
            System.out.println(ex.getMessage());
            return;
        }
        if (current_card instanceof CreditCard){
            throw new WrongCardInfo("You can not transfer money from accounts using a CreditCard");
        }
        if (current_card instanceof DebitCard){
             Account transfer_to_this_account = Accounts.get(account_no);
            ((DebitCard) current_card).transfer_money(current_account, transfer_to_this_account, amount);
            ((DebitCard) current_card).printReceipt(current_account, amount);
            Receipt receipt = new Receipt(current_account);
            receipt.toString();
        }
    }

    public void transfer_from_checkings_to_savings(double amount) throws WrongCardInfo, WrongAccount{
        try{
            check_if_card_exists();
        }
        catch (MustChooseACard ex){
            System.out.println(ex.getMessage());
        }
        if (current_account instanceof SavingsAccount){
            throw new WrongAccount("You must select the checkings account to transfer money to your savings account");
        }
        if (current_card instanceof CreditCard){
            throw new WrongCardInfo("You can not transfer money using a Credit Card");
        }
        if (current_card instanceof DebitCard){
            ((DebitCard) current_card).transfer_money(current_account, savingsAccount, amount);
            Receipt receipt = new Receipt(current_account);
        }
    }
}
