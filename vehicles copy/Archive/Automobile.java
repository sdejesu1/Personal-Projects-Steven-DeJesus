/** header
 * Steven De Jesus
 * CS110 - Assignment 8
 * 04/08/2022
 */
public class Automobile extends Vehicle {
    /**
     * @param numPassengers - integer instance variable that holds number of passengers
     * @param isSUV         - boolean instance variable that checks whether it is an suv or not
     */

    private int numPassengers;
    private boolean isSUV;

    /** single constructor */
    public Automobile(Person owner, String make, String model, int year, int mileage, int numPassengers,
            boolean isSUV) {
        super(owner, make, model, year, mileage);
        this.numPassengers = numPassengers;
        this.isSUV = isSUV;
    }

    /** getters */
    public int getNumPassengers() {
        return numPassengers;
    }

    public boolean getsisSUV() {
        return isSUV;
    }

    /** setters */
    public void setNumPassengers(int n) {
        this.numPassengers = n;
    }

    public void setisSUV(Boolean n) {
        this.isSUV = n;
    }

    /**
     * toString - display in the following format:
     * Julia Connors, 145 Maple St, St Louis, MO, 314-769-3923
     * Subaru Impreza 2018 12000 miles 4 passengers SUV
     * if not SUV, leave out the SUV
     */

    public String toString() {
        String str;
        if (isSUV)
            str = super.toString() + " " + numPassengers + " passengers SUV";
        else 
            str = super.toString() + " " + numPassengers + " passengers";
        
        return str;

    }

    /**
     * equals - Two Automobile objects are equal if their Vehicle parts are the same
     * and numPassengers and isSUV are the same
     */

    public boolean equals(Automobile other){
        return super.equals(other) && this.numPassengers == other.numPassengers &&  this.isSUV == other.isSUV;
    }
}
