
public class TruckDriver
{
    public static void main(String[] args) 
    {
        System.out.printf("***Testing Person***\n");
        Person p = new Person("Hamid Singh", "39A Oak Circle, Austin TX", "512-283-9911"); 
        Person p2 = new Person("Hamid Singh", "39A Oak Circle, Austin TX", "512-283-9911");
        Person p3 = p;
        Person p4 = new Person("Hannah Singh", "39A Oak Circle, Austin TX", "512-283-9911");
        System.out.printf("%s\n",p);
        System.out.printf("p.equals(p2) = %b\n", p.equals(p2)); 
        System.out.printf("p.equals(p3) = %b\n", p.equals(p3)); 
        System.out.printf("p.equals(p4) = %b\n", p.equals(p4)); 
        
        System.out.printf("\n***Testing Vehicle***\n");
        
        Vehicle v = new Vehicle(p,"Chevy","Tahoe",2015, 87098);
        Vehicle v2 = new Vehicle(v.getOwner(),"Chevy","Tahoe",2015,87098);
        Vehicle v3 = new Vehicle(p,"Chevy","Tahoe",2015);
        Vehicle v4 = v;
        
        System.out.printf("%s\n",v);
        System.out.printf("v.equals(v2) = %b\n", v.equals(v2));
        System.out.printf("v.equals(v3) = %b\n", v.equals(v3));
        System.out.printf("v.equals(v4) = %b\n", v.equals(v4));

        System.out.printf("\n***Testing Truck***\n");
 
        Truck t = new Truck(p, "Ford","F250", 2018, 15450,1, 2);
        Truck t2 = new Truck("Hamid Singh", "39A Oak Circle, Austin TX", "512-283-9911","Ford","F250", 2018, 15450);
        Truck t3 = new Truck(p,"Ford","F250", 2018, 15450,1, 3);
        Truck t4 = t;
        
        System.out.printf("%s\n",t);
        System.out.printf("t.equals(t2) = %b\n", t.equals(t2));
        System.out.printf("t.equals(t3) = %b\n", t.equals(t3));
        System.out.printf("t.equals(t4) = %b\n", t.equals(t4));
        
    }


}