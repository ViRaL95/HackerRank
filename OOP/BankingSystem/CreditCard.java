import java.util.Date;

public class CreditCard extends Card {
    double money_owed;
    Date next_payment_due;

    public CreditCard(Long card_number, String first_name, String last_name){
        super(card_number, first_name, last_name);
        money_owed = 0;
        next_payment_due = new Date();
        next_payment_due.setMonth(next_payment_due.getMonth());
    }

    public void spendMoney(double amount_to_spend){
        money_owed += amount_to_spend;
    }

    public void payCard(double amount_to_pay) throws NothingToPay{
        if (money_owed == 0){
            throw new NothingToPay("There is nothing to pay");
        }
        this.money_owed -= amount_to_pay;
    }

    public void print_receipt(Account account, double amount){
        Receipt receipt = new Receipt(account);
        System.out.println(receipt.toString());
    }
}
