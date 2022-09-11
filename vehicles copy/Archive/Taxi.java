/** header
 * Steven De Jesus
 * CS110 - Assignment 8
 * 04/08/2022
 */
public class Taxi extends Automobile{
    /** declare instance variables
     * @param ID - string variable that represents ID
     * @param driver - Person object variable name driver
     */

    private String ID;
    private Person driver;

    /** constructor */

    public Taxi(Person owner, String make, String model, int year, int mileage, int numPassengers, boolean isSUV, String ID, Person driver){
        super(owner, make, model, year, mileage, numPassengers, isSUV);
        this.ID = ID;
        this.driver = driver;
    }

    /** getters */
    public String getID(){
        return ID;
    }

    public Person getDriver(){
        return driver;
    }

    /** setters 
     * @param id = parameter id string variable
     * @param driver = parameter driver person variable
    */
    public void setID(String id){
        this.ID = id;
    }

    public void setDriver(Person driver){
        this.driver = driver;
    }

    /** to string
     * @param str - sting variable meant to represent full string 
     * @return str
    */

    public String toString()
   {
      String str = super.toString() + ",\nDriver: " + driver.toString() + " ID#" + ID;
      return str;
   }

   /** equals method
    * @param otherTaxi = taxi parameter that will compare this taxi to
    * @return super.equals, this.ID.equals and this.driver.equals, to simplify equals method, returning a simple true or false by utilizing other equals methods
    */

    public boolean equals(Taxi otherTaxi)
    {
       return super.equals(otherTaxi) && this.ID.equals(otherTaxi.ID) && this.driver.equals(otherTaxi.driver);
    }
}
