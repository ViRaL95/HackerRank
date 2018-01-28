public abstract class Card {
    private String owner_first_name;
    private String owner_last_name;
    long card_number;

    public Card(Long card_number, String owner_first_name, String owner_last_name){
        this.card_number = card_number;
        this.owner_first_name = owner_first_name;
        this.owner_last_name = owner_last_name;
    }

    public String getOwner_first_name() {
        return owner_first_name;
    }

    public String getOwner_last_name() {
        return owner_last_name;
    }

    public void setOwner_first_name(String owner_first_name) {
        this.owner_first_name = owner_first_name;
    }

    public void setOwner_last_name(String owner_last_name) {
        this.owner_last_name = owner_last_name;
    }


    public Long getCardNo(){
        return this.card_number;
    }
}
