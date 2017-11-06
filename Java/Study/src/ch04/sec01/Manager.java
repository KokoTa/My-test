package ch04.sec01;

// 管理类继承员工类
public class Manager extends Employee {
    private double bonus;
    
    public Manager(String name, double salary) {
        super(name, salary); // 调用员工类的构造函数且super必须放第一行
        bonus = 0;
    }
    
    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
    
    public double getSalary() { // Overrides superclass method
        return super.getSalary() + bonus;
    }
} 