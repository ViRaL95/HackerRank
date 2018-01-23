/* Abstract Employee Class, If you were to create an Employee you should create an instance of one of the subclasses. This class should be able to handle phone calls. 
 *
 * @param employee_id a unique an employee id
 * @param first_name the first name of an employee
 * @param last_name the last name of an employee 
*/

public abstract class Employee{
    private String first_name;
    private String last_name;
    private int employee_id;
    private boolean busy;
    
    public boolean get_busy(){
        return this.busy;
    }
    
    public void set_busy(boolean busy){
        this.busy = busy;
    }

    public String get_first_name(){
        return this.first_name;
    }    

    public String get_last_name(){
        return this.last_name;
    }

    public int get_employee_id(){
        return this.employee_id;
    }

    public Employee(String first_name, String last_name, int employee_id, boolean busy){
        this.first_name = first_name;
        this.last_name = last_name;
        this.employee_id = employee_id;
        this.busy = busy;
    }

}
