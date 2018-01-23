public class Manager extends Employee{
    public void handle_phone_call(PhoneCall call){
        try{
            call.answer_call(this);
            super.set_busy(true);        
        }
        catch(PhoneCallHasBeenAnswered ex){
            System.out.println(ex.getMessage());
        }
    }
    public Manager(String first_name, String last_name, int employee_id, boolean busy){
        super(first_name, last_name, employee_id, busy);
    }   
}
