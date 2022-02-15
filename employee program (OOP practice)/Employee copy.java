public class Employee
{
    // private fields
    private String name;

    private int idNumber;

    private String department;

    private String position;

// constructor (all values)
    public Employee(String empName, int empId, String empDept, String empPos)
    {
        name = empName;
        idNumber = empId;
        department = empDept;
        position = empPos;
    }
// constructor (name and id)
    public Employee(String empName, int empId)
    {
        name = empName;
        idNumber = empId;
        department = "";
        position = "";
    }

// constructor (no arg)
    public Employee()
    {
        name = "";
        idNumber = 0;
        department = "";
        position = "";
    }

// assign void method (set)
    public void setName(String n)
    {
        name = n;
    }

    public void setInt(int n)
    {
        idNumber = n;
    }

    public void setDept(String n)
    {
        department = n;
    }

    public void setPos(String n)
    {
        position = n;
    }
// return methods (get)
    public String getName()
    {
        return name;
    }

    public int getInt()
    {
        return idNumber;
    }

    public String getDept()
    {
        return department;
    }

    public String getPos()
    {
        return position;
    }
}