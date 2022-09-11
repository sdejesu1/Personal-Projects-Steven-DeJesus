
public class Truck extends Vehicle {
    /**
     * @param capacity - int variable representing capacity
     * @param numAxles - int variable representing numAxles
     * @param DEF_CAPACITY - final int constant value 1
     * @param DEF_AXLES - final int constant value 2
     */

     private int capacity;
     private int numAxles;
     private final int DEF_CAPACTITY = 1;
     private final int DEF_AXLES = 2;

     /** constructors */
     public Truck(Person o, String m, String mo, int y, int mil, int cap, int axle){
        super(o,m,mo,y,mil);
        capacity = cap;
        numAxles = axle;
     }
     public Truck(String n, String a, String p, String m, String mo, int y, int mil){
        super(new Person(n, a, p), m, mo, y, mil);
        capacity = DEF_CAPACTITY;
        numAxles = DEF_AXLES;
     }

     /** getters */
     public int getCapacity(){
         return capacity;
     }
     public int getNumAxles(){
         return numAxles;
     }
     /** setters */
     public void setCapacity(int cap){
        capacity = cap;
    }
    public void setNumAxles(int axle){
        numAxles = axle;
    }

    @Override
    /** to string */
    public String toString(){
        return getOwner() + "\n" + getMake() + " " + getModel() + " " + getYear() + " " + getMileage() + " " + getCapacity() + " ton " + getNumAxles() + " axles";
    }

    public boolean equals(Truck truck2){
        if(this.toString().equals(truck2.toString())) 
            return true;
        else
            return false;
    }

}