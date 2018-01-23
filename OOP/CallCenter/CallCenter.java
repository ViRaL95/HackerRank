import java.util.Stack;
/*This is a call center class. Its purpose is to find the first available employee.
 *Respondents should be the first type of employee that should take the calll, then the manager, then the dirctors. 
 * */
public class CallCenter{
    private Stack <Respondent> respondent_stack;
    private Stack <Manager>  manager_stack;
    private Stack <Director> director_stack;

    public CallCenter(){
        this.respondent_stack = new Stack<Respondent> ();
        this.manager_stack = new Stack<Manager> ();
        this.director_stack = new Stack <Director>();
    } 

    public Respondent search_respondents(){
        for (Respondent respondent: this.respondent_stack){
            if (!respondent.get_busy()){
                return respondent;
            }
        }
        return null;
    }
    
    public Manager search_managers(){
        for (Manager manager: this.manager_stack){
            if(!manager.get_busy()){
                return manager;
            }
        }
        return null;
    }


    public Director search_directors(){
        for (Director director: this.director_stack){
            if(!director.get_busy()){
                return director;
            }
        }
        return null;
    }


    public void dispatch_call(PhoneCall call) throws EveryoneBusy{
        /*
 * If one wants to avoid these if statements another subclass could be made from Employee,
 * Which is a type of employee that can make phone calls. Respondent, Manager, and Director
 *could then be subclasses of this class. This will allow us to make a call from any given
 * employee. The search_respondents, search_managers, and search_directors methods could also
 * be removed with only one method which simply searches through the three stacks. We can then
 * an object of this new suclass type!
     */
        Respondent respondent = search_respondents();
        Manager manager = search_managers();
        Director director = search_directors();
        if (respondent != null){
            respondent.handle_phone_call(call);
            return;
        }
        if (manager != null){
            manager.handle_phone_call(call);
            return;
        }
        if (director != null){
            director.handle_phone_call(call);
            return;
        }
        throw new EveryoneBusy("Everyone is too busy to answer this phone call");
    }

     
    public void add_respondent(Respondent respondent){
        this.respondent_stack.push(respondent);
    }
    
    public void add_manager(Manager manager){
        this.manager_stack.push(manager);
    }

    public void add_director(Director director){
        this.director_stack.push(director);
    }

    public static void main (String [] args){
        /*
 *      In this case everyone is too busy to respond to the phone call. 
 *
 *
 *      */
        Respondent respondent1 = new Respondent("Varun", "Rao", 1, true);
        Respondent respondent2 = new Respondent("Nakul", "Rao", 2, true);
        Manager manager1= new Manager("Meghna", "Rao", 3, true);
        Manager manager2= new Manager("Vadeesh", "Rao", 4, true);
        Director director1 = new Director("Drake", "Bell", 4, true);
        Director director2 = new Director("Guy", "Hi", 5, false);
        CallCenter call_center = new CallCenter();
        call_center.add_respondent(respondent1);
        call_center.add_respondent(respondent2);
        call_center.add_manager(manager1);
        call_center.add_manager(manager2);
        call_center.add_director(director1);
        call_center.add_director(director2);
        PhoneCall call = new PhoneCall("718-479-4539", "Sudha", "Rao");
        try{
            call_center.dispatch_call(call);
        }
        catch(EveryoneBusy ex){
            System.out.println(ex.getMessage());
        }
        
        /*
 *      In this case there should be no available workers to answer the call
 *      */
        try{
            call_center.dispatch_call(call);
        }
        catch(EveryoneBusy ex){
            System.out.println(ex.getMessage());
        }

        director2.set_busy(false);

        /*
 *      In this case the phone call has already been answered so an error will be printed
 *
 * 
        */

        try{
            call_center.dispatch_call(call);
        }
        catch(EveryoneBusy ex){
            System.out.println(ex.getMessage());
        }
   
    } 
}
