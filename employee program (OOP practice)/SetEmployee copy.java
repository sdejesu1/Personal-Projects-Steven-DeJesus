public class SetEmployee {
    public static void main(String[] args)
    {
        Employee susan = new Employee("Susan Meyer", 47899, "Accounting", "Vice President");

        Employee mark = new Employee("Mark Jones", 39119, "IT", "Programmer");

        Employee joy = new Employee("Joy Rogers", 81774, "Manufacturing", "Engineer");


        System.out.printf("%25s %25s %25s %25s", "Name", "ID Number", "Department", "Position\n\n");
        System.out.printf("%25s %25s %25s %25s", susan.getName(), susan.getInt(), susan.getDept(), susan.getPos() + "\n");
        System.out.printf("%25s %25s %25s %25s", mark.getName(), mark.getInt(), mark.getDept(), mark.getPos() + "\n");
        System.out.printf("%25s %25s %25s %25s", joy.getName(), joy.getInt(), joy.getDept(), joy.getPos() + "\n");

    }
}
