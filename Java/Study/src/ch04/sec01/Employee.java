package ch04.sec01;

// 这只是一个普通的员工类
public class Employee {
    private String name;
    private double salary;
        
    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    public void raiseSalary(double byPercent) {
        double raise = salary * byPercent / 100;
        salary += raise;    
    }
    
    public final String getName() {
        return name;
    }
    
    public double getSalary() {
        return salary;
    }
}
