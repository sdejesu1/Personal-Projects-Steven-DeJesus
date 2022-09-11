
public class Person {
    /** @param name - string variable representing name
     * @param address - string variable representing  person's address
     * @param phone - string variable representing person's phone number
     */

     private String name;
     private String address;
     private String phone;

     /** constructor : takes all string params
      * @param n - string parameter that is assigned to name
      * @param a - string parameter that is assigned to address
      * @param p - string parameter that is assigned to phone
      */

     public Person(String n, String a, String p){
         name = n;
         address = a;
         phone = p;
     }

     /** getters 
      * @return name
      * @return address
      * @return phone
     */
     public String getName(){
         return name;
     }

     public String getAddress(){
         return address;
     }

     public String getPhone(){
         return phone;
     }

     /** setters
      * @param n - string parameter that is assigned to name
      * @param a - string parameter that is assigned to address
      * @param p - string parameter that is assigned to phone
      */
     public void setName(String n){
         name = n;
     }

     public void setAddress(String a){
        address = a;
    }

    public void setPhone(String p){
        phone = p;
    }

    /** toString method 
     * @param str - string variable to hold the string that is comprised of the name, address, and phone variables
     * @return str
    */
    public String toString(){
        String str = name + ", " + address + ", " + phone;
        return str;
    }

    /** equals method
     * @param person2 - object parameter that will be used to compare
     */
    public boolean equals(Person person2){
        if (this.name.equals(person2.name) && this.address.equals(person2.address) && this.phone.equals(person2.phone))
            return true;
        else
            return false;
    }
}
