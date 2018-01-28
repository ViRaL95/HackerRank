public class DebitCard extends Card {

    public DebitCard(Long card_number, String first_name, String last_name) {
        super(card_number, first_name, last_name);
    }

    public void withdrawMoney(Account account, double amount_to_spend) {
        try {
            account.withdraw_money(amount_to_spend);
        } catch (OverDraftFee ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void transfer_money(Account transferring_acount, Account recieving_account, double amount) {
        transferring_acount.transfer_money(recieving_account, amount);
    }

    public void deposit_money(Account account, double amount) {
        account.deposit_money(amount);
    }

    public void printReceipt(Account account, double amount) {
        String receipt = String.format("Bill amount is %f, and current amount in bank is ", amount, account.getAmount());
        System.out.println(receipt);
    }
}
