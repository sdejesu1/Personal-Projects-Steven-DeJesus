
public class Vehicle {
    /**
     * @param owner - person object that represents the owner of the vehicle
     * @param make - string that represents make of vehicle
     * @param model - string that represents model of vehicle
     * @param year - int variable that represents year of vehicle
     * @param mileage - int variable that represents the mileage of the vehicle
     */
    
    private Person owner;
     private String make;
     private String model;
     private int year;
     private int mileage;

     /** constructor (all params) 
      * @param o - owner parameter for owner variable to be set to
      * @param m - string parameter for make to be set to
      * @param mo - string parameter for model to be set to
      * @param y - int parameter for year to be set to
      * @param mil - int parameter for mileage to be set to
     */
     public Vehicle(Person o, String m, String mo, int y, int mil){
         owner = o;
         make = m;
         model = mo;
         year = y;
         mileage = mil;
     }

     /** constructor (all params except mileage) 
      * @param o - owner parameter for owner variable to be set to
      * @param m - string parameter for make to be set to
      * @param mo - string parameter for model to be set to
      * @param y - int parameter for year to be set to
     */
    public Vehicle(Person o, String m, String mo, int y){
         owner = o;
         make = m;
         model = mo;
         year = y;
         mileage = 0;
    }

    /** getters 
     * @return owner
     * @return make
     * @return model
     * @return year
     * @return mileage
    */
    public Person getOwner(){
        return owner;
    }

    public String getMake(){
        return make;
    }

    public String getModel(){
        return model;
    }

    public int getYear(){
        return year;
    }

    public int getMileage(){
        return mileage;
    }

    /** setters 
     * @param o - owner parameter for owner variable to be set to
      * @param m - string parameter for make to be set to
      * @param mo - string parameter for model to be set to
      * @param y - int parameter for year to be set to
      * @param mil - int parameter for mileage to be set to 
    */
    public void setOwner(Person o){
        owner = o;
    }

    public void setMake(String m){
        make = m;
    }

    public void setModel(String mo){
       model = mo;
    }

    public void setOwner(int y){
        year = y;
    }

    public void setMileage(int mil){
        mileage = mil;
    }

    /** toString 
     * @param str -  string variable to hold the string that is comprised of the owner, make, model, year, and milage variables
     * @return str
     */
    public String toString(){
        String str = owner.toString() + "\n" + make + " " + model + " " + year + " " + mileage + " miles";
        return str;
    }

    /** equals method 
     * @param vehicle2 - other vehicle parameter to compare to
    */
    public boolean equals(Vehicle vehicle2){
        if(this.owner.equals(vehicle2.owner) && this.make.equals(vehicle2.make) && this.model.equals(vehicle2.model) && this.year == vehicle2.year && this.mileage == vehicle2.mileage)
            return true;
        else
            return false;
    }
}