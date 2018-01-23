public class PhoneCall{
    private String phone_number;
    private String caller_first_name;
    private String caller_last_name;
    private boolean answered;

    public void answer_call(Employee employee) throws PhoneCallHasBeenAnswered{
        System.out.printf("The phone call status is %b", this.answered);
        if (this.answered){
            throw new PhoneCallHasBeenAnswered("This phone call has already been Answered!");
        }
        else{
            System.out.printf("The employees name is %s %s, employee id is %d ", employee.get_first_name(), employee.get_last_name(), employee.get_employee_id());
            this.answered = true;
        }
    }

    public PhoneCall(String phone_number, String first_name, String last_name){
        this.phone_number = phone_number;
        this.caller_first_name = first_name;
        this.caller_last_name = last_name;
        this.answered = false;
    }
}
