public class Receipt {
    private Account account;

    public Receipt(Account account){
        this.account = account;
    }

    public String toString(){
        String receipt_information = String.format("Current account amount is %f, owned by %s %s ", account.getAmount(), account.getUser().getFirst_name(), account.getUser().getLast_name());
        return receipt_information;
    }
}
