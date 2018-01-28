import java.util.HashMap;

public class Bank {
    HashMap<Long, Account> Accounts;

    public Bank(){
        Accounts = new HashMap<Long, Account>();
    }

    public void transfer_money_cross_users(Account sender, Account reciever, double amount){
        try {
            sender.withdraw_money(amount);
            reciever.deposit_money(amount);
        }
        catch (OverDraftFee ex){
            System.out.println(ex.getMessage());
        }
    }

    public void add_account(Account account){
        Accounts.put(account.getAccount_no(), account);
    }

    public HashMap<Long, Account> get_accounts(){
        return Accounts;
    }

    public Account get_account(Long account_no, int pin_no){
        Account account = Accounts.get(account_no);
        return account;
    }

    public static void main (String [] args){
        try {
            Bank bank = new Bank();

            User customer1 = new User("Varun", "Rao", 22);
            User customer2 = new User("Meghna", "Rao", 27);

            HashMap<Long, Account> accounts = bank.get_accounts();

            Account account = customer1.create_checking_account(11750);
            accounts.put(account.getAccount_no(), account);
            //50.00 in account1
            customer1.set_current_account(account.getAccount_no(), account.getPin_no());
            try {
                DebitCard debitCard = customer1.create_debit_card();
                customer1.set_current_card(debitCard.getCardNo());
            }
            catch (MustHaveACheckingAccount ex){
                System.out.println(ex.getMessage());
            }

            customer1.deposit_money(50.00);

            Account account2 = customer1.create_checking_account(78342);
            accounts.put(account2.getAccount_no(), account2);
            //10 dollars in account 2, 40 dollars in account 1
            customer1.transfer_money_from_accounts(account2.getAccount_no(), 10.00);

            Account account3 = customer2.create_checking_account(99999);
            accounts.put(account3.getAccount_no(), account3);

            customer2.set_current_account(account3.getAccount_no(), account3.getPin_no());
            try {
                DebitCard debitCard = customer2.create_debit_card();
                customer2.set_current_card(debitCard.getCardNo());
            }
            catch (MustHaveACheckingAccount ex){
                System.out.println(ex.getMessage());
            }
            //20 dollars in account 3
            customer2.deposit_money(20.00);
            //0 dollars in account2, 30 dollars in account 3
            bank.transfer_money_cross_users(account2, account3, 10.00);
            try {
                SavingsAccount account4 = customer2.create_saving_account(91111);
                accounts.put(account4.getAccount_no(), account4);
                account4.deposit_money(300.56);
                account4.withdraw_money_from_savings(10.00);
                account4.withdraw_money_from_savings(10.00);
                account4.withdraw_money_from_savings(10.00);
                account4.withdraw_money_from_savings(10.00);
                account4.withdraw_money_from_savings(12.00);
                //this should throw an exception because one can not draw from a savings account
                //more than 6 times
                account4.withdraw_money_from_savings(8.00);
            }
           catch(OnlyOneSavingsAccount | TooManyWithdrawals | OverDraftFee ex){
                System.out.println(ex.getMessage());
           }


        }
        catch (WrongCardInfo | WrongAccountInfo ex){
            System.out.println(ex.getMessage());
        }
    }
}
